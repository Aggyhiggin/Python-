#!/usr/bin/env python3
def ec2create_Instance():

        import sys
        import boto3
        s3 = boto3.resource("s3")
        ec2 = boto3.resource('ec2')
        user_data = '''#!/bin/bash    
                yum update -y
                yum install httpd -y
                systemctl enable httpd
                systemctl start httpd
                echo "<h2>Test page</h2>Instance ID: " > /var/www/html/index.html
                curl --silent http://169.254.169.254/latest/meta-data/instance-id/ >> /var/www/html/index.html
                echo "<br>Availability zone: " >> /var/www/html/index.html
                curl --silent http://169.254.169.254/latest/meta-data/placement/availability-zone/ >> /var/www/html /index.html
                echo "<br>IP address: " >> /var/www/html/index.html
                curl --silent http://169.254.169.254/latest/meta-data/public-ipv4 >> /var/www/html/index.html''' 

        key_pair = ec2.KeyPair('Douglas_key.pem')
        instance = ec2.create_instances(
                ImageId='ami-0713f98de93617bb4',
                MinCount=1,
                MaxCount=1,
                KeyName = 'Douglas_key',
                SecurityGroupIds = ['sg-0d4053eafb4d14599'], #adding an already made grouppair that i created an SSH and HTTP 
                InstanceType = 't2.nano',
                UserData ='''#!/bin/bash    
                yum update -y
                yum install httpd -y
                systemctl enable httpd
                systemctl start httpd
                echo
                '''
                 )
        print (instance[0].id)
        ec2.create_tags(Resources=[instance[0].id], Tags=[{'Key':'heythere', 'Value':'My-Instance'}])
 