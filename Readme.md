# **AWS CloudFormationを使ったインフラ構築**

## **構築されるサービス**
- EC2 インスタンス（AmazonLinux2)　×1  
　※SSM接続可能
- config
- httpd
- php(7.4)

## **Stack作成コマンド**

1.VPC EC2インスタンス作成
``
aws cloudformation deploy --stack-name <stack-name> --template-file template.yml --capabilities CAPABILITY_NAMED_IAM --no-execute-changeset
``

2.AWS Config開始
``
aws cloudformation deploy --stack-name <stack-name> --template-file config.yml --capabilities CAPABILITY_NAMED_IAM --no-execute-changeset
``
