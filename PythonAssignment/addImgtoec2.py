#!/usr/bin/env python3 

import sys
import boto3
import time
import subprocess

def addImgtoEc2():
    from ec2list_instances import ec2list_Instances
    from S3list_bucket import S3list_Bucket
    from addImgtoec2 import addMetaData
    ec2 = boto3.resource('ec2')
    s3 = boto3.resource('s3')
    print("running instances: ")
    print("")
    ec2list_Instances()

    ids = input("Enter Id for the instance for the server: ")
    for instance in ec2.instances.all():
        if instance.id == ids:
            try:
                ids = (instance.id)
                public_ip_address = instance.public_ip_address
                
                S3list_Bucket()
                bucket_name = input("Enter the destiontion bucket name for the img: ")
                object_name = input("Enter the name of the file you'd like to show: ")
                addMetaData(bucket_name, public_ip_address, object_name)
            except Exception as error:
                print(error)

def addMetaData(bucketName,public_ip_address,object_name ): # this will create the new methdata when the user add it ^^ to the instance that you pick
    print()
    command = 'ssh -i Douglas_key.pem -o StrictHostKeyChecking=no ec2-user@' + public_ip_address
    createIndex = " \"echo '<h2>Aggys AWS</h2>Instance ID: ' >> index.html\""
    curlInstanceId = " \"curl --silent http://169.254.169.254/latest/meta-data/instance-id/ >> index.html\""
    echoAz = """ "echo \'<br>Availability zone: \' >> index.html" """
    curlAz = """ "curl --silent http://169.254.169.254/latest/meta-data/placement/availability-zone/ >> index.html" """
    echoIp = """ "echo \'<br>IP address: \' >> index.html" """
    curlIp = """ "curl --silent http://169.254.169.254/latest/meta-data/public-ipv4 >> index.html\" """
    cpIndex = " \"sudo cp index.html /var/www/html/index.html \""
    addBucketObj = """ "echo \'<br><img src=\"https://""" + bucketName + """.s3-eu-west-1.amazonaws.com/""" +object_name+"""\">\' >> index.html" """
    
    try:
        time.sleep(30) #waits its a timer 
        subprocess.run(command + createIndex, shell=True)
        subprocess.run(command + curlInstanceId, shell=True)
        subprocess.run(command + echoAz, shell=True)
        subprocess.run(command + curlAz, shell=True)
        subprocess.run(command + echoIp, shell=True)
        subprocess.run(command + curlIp, shell=True)
        subprocess.run(command + addBucketObj, shell=True)
        print("Waiting for availability to copy index.html to /var/www/html....")
        timeToWait = 90
        while(timeToWait != 0):
            time.sleep(10)
            print(timeToWait)
            timeToWait = timeToWait - 10
        subprocess.run(command + cpIndex, shell=True)  
    except Exception as error:
        print(error)

