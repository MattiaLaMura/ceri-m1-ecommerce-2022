terraform {
  cloud {
    organization = "team-purplepig"

    workspaces {
      name = "ceri-m2-ecommerce"
    }
  }
}

provider "google" {
    project = "ceri-m1-ecommerce-2022"
    region = "europe-west1"
}

data "google_secret_manager_secret" "host" {
  secret_id = "mysql-address"
}

data "google_secret_manager_secret" "user" {
  secret_id = "mysql-user-purplepig"
}

data "google_secret_manager_secret" "password" {
  secret_id = "mysql-password-purplepig"
}

data "google_secret_manager_secret" "dbname" {
  secret_id = "mysql-database-purplepig"
}

resource "google_cloud_run_service" "backend" {
  name     = "purplepig-backend"
  location = "europe-west1"

  template {
    spec {
      service_account_name = "terraform-purplepig@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
      containers {
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/purplepig/backend:0.0.1"
        env {
          name = "USER"
          value_from {
            secret_key_ref{
              name = data.google_secret_manager_secret.user.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "PASSWORD"
          value_from {
            secret_key_ref{
              name = data.google_secret_manager_secret.password.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "HOST"
          value_from {
            secret_key_ref{
              name = data.google_secret_manager_secret.host.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "PORT"
          value = 3306
        }
        env {
          name = "DBNAME"
          value_from {
            secret_key_ref{
              name = data.google_secret_manager_secret.dbname.secret_id
              key = "latest"
            }
          }
        }
      }
    }
    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "1"
      }
    }
  }

  traffic {
    percent = 100
    latest_revision = true
  }

}

output "cloud_run_instance_url"{
  value = google_cloud_run_service.backend.status.0.url
}

resource "google_cloud_run_service" "frontend" {
  name     = "purplepig-frontend"
  location = "europe-west1"

  template {
    spec {
      service_account_name = "terraform-purplepig@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
      containers {
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/purplepig/frontend:0.0.1"
        env {
          name = "BACKEND_URL"
          value = module.root.cloud_run_instance_url
        }
      }
    }
    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "1"
      }
    }
  }

  traffic {
    percent = 100
    latest_revision = true
  }
}

resource "google_cloud_run_service_iam_member" "invokers-backend" {
  location = google_cloud_run_service.backend.location
  service = google_cloud_run_service.backend.name
  role    = "roles/run.invoker"
  member  = "allUsers"
}

resource "google_cloud_run_service_iam_member" "invokers-frontend" {
  location = google_cloud_run_service.frontend.location
  service = google_cloud_run_service.frontend.name
  role    = "roles/run.invoker"
  member  = "allUsers"
}