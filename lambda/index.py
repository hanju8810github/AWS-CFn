import os
import boto3
import datetime

region_name = os.getenv('RegionName')
dbid = os.getenv('DbinstanceId')

cw_client = boto3.client('cloudwatch',region_name)
ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    describe_dbinstance_cpuutilizasion(dbinstanceid)

def describe_dbinstance_cpuutilizasion(dbid):
    dbname = os.getenv('DbinstanceName')
    print('## DB-INSTANCE-NAME',dbname)
    print('## DB-INSTANCE-ID',dbid)
    dtnow = datetime.datetime.now()

response = cw_client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': dbid,
            },
        ],
        StartTime=dtnow - datetime.timedelta(seconds=300),
        EndTime=dtnow,
        Period=300,
        Statistics=['Average'],
)
dbcpu_avg = response["Datapoints"][0]["Average"]
print('## DB-INSTANCE-CPUUTILIZATION',dbcpu_avg)
