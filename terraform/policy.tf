resource "aws_iam_policy" "serverless_deploy" {
  name        = "serverless_deploy_policy"
  description = "Serverless Framework Deploy Policy"

  policy = data.aws_iam_policy_document.serverless_deploy.json

}

data "aws_iam_policy_document" "serverless_deploy" {
  statement {
    sid       = 1
    effect    = "Allow"
    resources = ["*"]

    actions = [
      "lambda:CreateFunction",
      "logs:DeleteSubscriptionFilter",
      "s3:CreateBucket",
      "iam:CreateRole",
      "lambda:GetFunctionConfiguration",
      "cloudformation:DescribeStackResource",
      "iam:PutRolePolicy",
      "s3:GetObject*",
      "cloudformation:DescribeStackEvents",
      "s3:DeleteBucketWebsite",
      "logs:GetLogEvents",
      "cloudformation:UpdateStack",
      "lambda:ListLayerVersions",
      "lambda:ListLayers",
      "lambda:DeleteFunction",
      "events:RemoveTargets",
      "logs:FilterLogEvents",
      "lambda:GetAlias",
      "s3:DeleteObject",
      "s3:ListBucket",
      "apigateway:GET",
      "cloudformation:ListStackResources",
      "iam:GetRole",
      "events:DescribeRule",
      "lambda:ListFunctions",
      "lambda:InvokeFunction",
      "lambda:GetEventSourceMapping",
      "lambda:ListAliases",
      "iam:DeleteRole",
      "iam:UpdateAssumeRolePolicy",
      "s3:DeleteBucketPolicy",
      "logs:CreateLogGroup",
      "logs:TagResource",
      "cloudformation:DescribeStacks",
      "lambda:UpdateFunctionCode",
      "s3:PutObject",
      "cloudformation:DeleteStack",
      "lambda:ListEventSourceMappings",
      "lambda:PublishVersion",
      "logs:PutSubscriptionFilter",
      "apigateway:POST",
      "cloudformation:ValidateTemplate",
      "lambda:ListVersionsByFunction",
      "lambda:GetLayerVersion",
      "s3:DeleteObjectVersion",
      "events:PutRule",
      "lambda:GetAccountSettings",
      "lambda:GetLayerVersionPolicy",
      "s3:PutEncryptionConfiguration",
      "apigateway:DELETE",
      "iam:PassRole",
      "lambda:ListTags",
      "iam:DeleteRolePolicy",
      "apigateway:PATCH",
      "s3:DeleteBucket",
      "logs:DescribeLogGroups",
      "logs:DeleteLogGroup",
      "apigateway:PUT",
      "lambda:GetFunction",
      "lambda:UpdateFunctionConfiguration",
      "events:PutTargets",
      "lambda:AddPermission",
      "cloudformation:CreateStack",
      "s3:PutBucketPolicy",
      "sts:GetCallerIdentity",
      "lambda:RemovePermission",
      "s3:GetBucketLocation",
      "lambda:GetPolicy",
    ]
  }
}
