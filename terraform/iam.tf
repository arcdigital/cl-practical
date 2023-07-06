resource "aws_iam_user" "serverless_deploy" {
  name = "serverless-deploy"
}

resource "aws_iam_user_policy_attachment" "serverless_deploy" {
  user       = aws_iam_user.serverless_deploy.name
  policy_arn = aws_iam_policy.serverless_deploy.arn
}

resource "aws_iam_access_key" "serverless_deploy" {
  user = aws_iam_user.serverless_deploy.name
}
