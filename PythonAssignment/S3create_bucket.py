#!/usr/bin/env python3    
def S3create_Bucket():
    import sys
    import boto3
    from S3list_bucket import S3list_Bucket
    s3 = boto3.resource('s3')
    S3list_Bucket()
    bname = input("Enter Bucket Name: ")
    fullName = ("wit-aggys" + bname) 
    try:
        response = s3.create_bucket(Bucket=fullName, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'}, ACL="public-read")
        print (response)
    except Exception as error:
        print (error)