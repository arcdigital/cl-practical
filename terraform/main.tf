provider "aws" {
  region     = "us-east-1"
}

provider "newrelic" {
  account_id = var.new_relic_account_id
  api_key = var.new_relic_api_key
  region = "US"
}
