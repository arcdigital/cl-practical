terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.6.2"
    }
    newrelic = {
      source = "newrelic/newrelic"
      version = "~> 3.25.0"
    }
  }

  required_version = "~> 1.5.0"
}