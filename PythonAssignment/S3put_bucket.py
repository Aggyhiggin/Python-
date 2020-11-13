#!/usr/bin/env python3
def S3put_Bucket():
    import sys
    import boto3
    s3 = boto3.resource("s3")
    from S3list_bucket import S3list_Bucket
    S3list_Bucket()
    bucket_name = input("Please Enter the Bucket You'd Like to add Contents to: ")
    object_name = input("Please Enter Object you'd Like: ")
    try:
        response = s3.Object(bucket_name, object_name).put(Body=open(object_name, 'rb'), ACL = "public-read")
        print (response)
    except Exception as error:
        print (error)

