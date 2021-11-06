# **AWS CloudFormationを使ったインフラ構築**

## **構築されるサービス**
- AWS CloudTrail
- EC2 インスタンス（AmazonLinux2)　×1  
　※SSM接続可能
- AWS config
- AWS Systems Manager Patch Manager
- httpd
- php(7.4)

## **Stack作成コマンド**

1.AWS CloudTrail開始

```
aws cloudformation deploy --stack-name <stack-name> --template-file cloudtrail.yml --no-execute-changeset
```


2.VPC EC2インスタンス作成

```
aws cloudformation deploy --stack-name <stack-name> --template-file template.yml --capabilities CAPABILITY_NAMED_IAM --no-execute-changeset
```

3.AWS Config開始

```
aws cloudformation deploy --stack-name <stack-name> --template-file config.yml --capabilities CAPABILITY_NAMED_IAM --no-execute-changeset
```

4.AWS Patch Manager ※毎日AM3:00開始

```
aws cloudformation deploy --stack-name <stack-name> --template-file patchscan.yml --no-execute-changese
```
