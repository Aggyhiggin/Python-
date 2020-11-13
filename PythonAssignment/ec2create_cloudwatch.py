#!/usr/bin/  python3

def ec2create_Cloudwatch():

    import boto3
    from datetime import datetime, timedelta
    from ec2list_instances import  ec2list_Instances
    cloudwatch = boto3.resource('cloudwatch')
    ec2 = boto3.resource('ec2')
    ec2list_Instances()

    instid = input("Please enter instance ID: ")   
    instance = ec2.Instance(instid)
    instance.monitor()       

    metric_iterator = cloudwatch.metrics.filter(Namespace='AWS/EC2',
                                            MetricName='CPUUtilization',
    Dimensions=[{'Name':'InstanceId', 'Value': instid}]) 
    metric = list(metric_iterator)[0] 
    response = metric.get_statistics(StartTime = datetime.utcnow() - timedelta(minutes=5), EndTime=datetime.utcnow(),
                                    Period=300,
                                    Statistics=['Average'])

    print ("Average CPU utilisation:", response['Datapoints'][0]['Average'], response['Datapoints'][0]['Unit']) 