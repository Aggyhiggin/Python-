#!/usr/bin/env python3
def ec2delete_Instance():
    import sys
    import boto3
    from ec2list_instances import ec2list_Instances #importing list instance so you dont have to search on aws
    ec2 = boto3.resource('ec2')
    ec2list_Instances()
    print("please Enter the Instance you'd like to delete: ") 
    ids=(input(), ) 
    ec2.instances.filter(InstanceIds = ids).terminate()
    print("instance was deleted")