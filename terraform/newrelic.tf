module "newrelic-aws-cloud-integrations" {
  source = "github.com/newrelic/terraform-provider-newrelic/examples/modules/cloud-integrations/aws"

  newrelic_account_id     = var.new_relic_account_id
  newrelic_account_region = "US"
  name                    = "clp"
}