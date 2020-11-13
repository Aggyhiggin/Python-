#!/usr/bin/env python3
def S3Delete_Bucket():
    import sys
    import boto3
    from S3list_bucket import S3list_Bucket
    s3 = boto3.resource('s3')
    S3list_Bucket()
    bname = input("Enter Bucket Name: ")
    fullName = (bname)
    bucket = s3.Bucket(fullName)
    try:
        response = bucket.delete()
        print (response)
    except Exception as error:
        print (error)