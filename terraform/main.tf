terraform {
    cloud {
        organization = "your organization name"
        workspace {
            name = " your workspace name"
        }
    }
}

provider "google" {
    project = "ceri-m1-ecommerce-2022"
    region = "europe-west1"
}