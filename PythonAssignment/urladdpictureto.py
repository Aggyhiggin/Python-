#!/usr/bin/env python3  
def Urladdpictureto ():
    import sys
    import boto3
    import requests
    from S3list_bucket import S3list_Bucket
    s3 = boto3.resource('s3')
    S3list_Bucket()
    
    #I used stackoverflow to get: 
    # eq_for_image = requests.get(internet_image_url, stream = True)
    #file_object_from_req = req_for_image.raw
    #req_data = file_object_from_req.read()
    #basically takes in the raw input of the file and returns a string also takes in the string and makes it readable from the keyborad 
    #https://stackoverflow.com/questions/14346065/upload-image-available-at-public-url-to-s3-using-boto/42493144
    

    bucket_name_upload_image_to=input("Name the bucket you'd like to use: ")
    file_name = input("Enter name for the file: ")
    thefilemethod = input("Would you like it to be uploaded by URL press 'h'= http://url?: ")

    if thefilemethod =='h':
        for bucket in s3.buckets.all():
            if bucket.name == bucket_name_upload_image_to:
                print("Found the Bucket")
                internet_image_url = input("please enter the url of image: ")
                req_for_image = requests.get(internet_image_url, stream = True)
                file_object_from_req = req_for_image.raw
                req_data = file_object_from_req.read()

                try:
                    s3.Bucket(bucket_name_upload_image_to).put_object(Key=file_name, Body=req_data, ACL = 'public-read')
                    print("the file " + file_name + "was added to the bucket! " + bucket_name_upload_image_to)
                except Exception as error:
                    print(error2)



