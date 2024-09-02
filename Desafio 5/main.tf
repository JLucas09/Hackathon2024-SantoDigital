terraform {
  required_version = "0.13.0"
 
}


resource "google_compute_network" "vpc_network" {
    name = "hackathon-vpc"
    auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet1" {
  name          = "subnet1"
  ip_cidr_range = "192.168.1.0/24"
  region        = "us-central1"
  network       = google_compute_network.vpc_network.self_link
}

resource "google_compute_subnetwork" "subnet2" {
  name          = "subnet2"
  ip_cidr_range = "10.152.0.0/24"
  region        = "us-east1"
  network       = google_compute_network.vpc_network.self_link
}
