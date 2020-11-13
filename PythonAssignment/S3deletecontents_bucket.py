#!/usr/bin/env python3
def S3deletecontents_Bucket():
    import sys
    import boto3
    from S3list_bucket import  S3list_Bucket
    s3 = boto3.resource('s3')
    S3list_Bucket()
    print("Enter The Bucket that you'd like to use: ")
    bucket_name = input()
    print("Select the file you'd like to remove: ")
    file_name = input()
    try:
        response = s3.Object(bucket_name,file_name) 
        response.delete()
        print (response)
    except Exception as error:
        print (error)