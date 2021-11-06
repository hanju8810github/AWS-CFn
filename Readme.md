# **AWS CloudFormationを使ったインフラ構築**

## **構築されるサービス**
- EC2 インスタンス（AmazonLinux2)　×1
- Systems Manager
- httpd
- php74

※SSM接続可能

## **Stack作成コマンド**

1.VPC EC2インスタンス作成

``
aws cloudformation deploy --stack-name <stack-name> --template-file template.yml --capabilities CAPABILITY_NAMED_IAM --no-execute-changeset
``
