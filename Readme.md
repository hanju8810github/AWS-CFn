# **AWS CloudFormationを使ったインフラ構築**

## **構築されるサービス**
- EC2 インスタンス（Wordpress)　×2
- 　※上記EC2はAutoScallingGroupに属する
- 　  ２つのAZをまたいだSubnetに作成される
- RDS　MySQl5.6
- EFSFileSystem


## **サービス(wordpress)にアクセス**
``http://${LoadBalancer.DNSName}``

## **Stack作成コマンド**
``
aws cloudformation create-stack --stack-name <stackname> --template-body file://<File Path>
``

## **Stack削除コマンド**
``aws cloudformation delete-stack --stack-name <stackname> ``
