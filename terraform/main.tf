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

data "google_secret_manager_secret" "algoia_id" {
  secret_id = "algolia-purplepig-application-id"
}

data "google_secret_manager_secret" "algoia_api_key" {
  secret_id = "algolia-purplepig-api-key"
}

resource "random_string" "random" {
  length           = 16
  special          = true
  override_special = "/@£$"
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
          name = "MYSQL_PORT"
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
        env {
          name = "ALGOLIA_APPLICATION_ID"
          value_from {
            secret_key_ref{
              name = data.google_secret_manager_secret.algoia_id.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "ALGOLIA_API_KEY"
          value_from {
            secret_key_ref{
              name = data.google_secret_manager_secret.algoia_api_key.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "SECRET_KEY"
          value = random_string.random.result
        }
        env {
          name = "ALGOLIA_INDEX_NAME"
          value = "Index"
        }
        ports {
          container_port = 2222
        }
      }
    }
    metadata {
      annotations = {
        "run.googleapis.com/cloudsql-instances" = "ceri-m1-ecommerce-2022:europe-west1:mysql-primary"
        "autoscaling.knative.dev/maxScale" = "1"
        "seed" = "Si tu souhaite redeployer le service avec le même tag d'image, changer cette string :)"
      }
    }
  }

  traffic {
    percent = 100
    latest_revision = true
  }

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
          name = "VITE_BACKEND_URL"
          value = google_cloud_run_service.backend.status.0.url
        }
        ports {
          container_port = 1111
        }
      }
    }
    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "1"
        "seed" = "Si tu souhaite redeployer le service avec le même tag d'image, changer cette string :)"
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

output "back_url"{
  value = google_cloud_run_service.backend.status.0.url
}

output "front_url"{
  value = google_cloud_run_service.frontend.status.0.url
}