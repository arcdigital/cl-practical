output "serverless_deploy_id" {
  value = aws_iam_access_key.serverless_deploy.id
}

output "serverless_deploy_key" {
  value     = aws_iam_access_key.serverless_deploy.secret
  sensitive = true
}
