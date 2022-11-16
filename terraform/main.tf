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