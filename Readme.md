
# AWS Cloudformation(CFn)&Lambda Knowledge

## リポジトリの主旨
AWS CFnおよびLambdaを使って作成したコードをKnowledge化します。

## フォルダ構成

<pre>
hanju-dev
├── ec2-atutoscaling EC2をオートスケールさせるためのコード群
 └── lambda Lambda関数
 　├──  autoscaling-judge.yaml CFn + Lambdaによる自動構築
 　└──  index.py オートスケールの実行判断
 ├── alarm.yaml WEBインスタンスのCPU使用率の閾値を超えるとAlarmを発報。Lambdaのトリガー
 ├── ec2.yaml EC2インスタンス構成
 ├── README.md このリポジトリのREADME
 └── vpc.yaml ネットワーク構成
</pre>


## 使用方法


```
$ git clone https://github.com/hanju8810github/AWS-CFn.git
```
コードを全てローカルにダウンロードしてエディタなどで編集し、AWS CFn Lambdaでデプロイして使用します。 

### ブランチ

* hanju-dev:
