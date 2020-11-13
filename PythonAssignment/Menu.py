#!/usr/bin/env python3
def menu():
    import boto3
    import sys 
    import subprocess
    import ec2create_instance
    import ec2list_instances
    import S3create_bucket
    import S3put_bucket
    import S3list_bucket
    import ec2create_cloudwatch
    import S3delete_bucket
    import ec2delete_instance
    import ec2list_instances
    import S3deletecontents_bucket
    import ec2ssh
    import addImgtoec2
    import urladdpictureto

    s3 = boto3.resource('s3')
    ec2 = boto3.resource('ec2')  
    menu_text = '''
𝓜𝓪𝓲𝓷 𝓜𝓮𝓷𝓾
'''
    print(menu_text)
    print("1. Launch a new Instance")
    print("2. List instances")
    print("3. Create S3 Bucket") 
    print("4. add contents inside bucket")
    print("5. List Buckets")
    print("6. Create Cloudwatch")
    print("7. Delete Bucket")
    print("8. Delete Instance")
    print("9. Delete Contents Of The Bucket")
    print("10. SSH on to an Instance")
    print ("11. Add a Url to Bucket")
    print ("12. Add Image to Instance")
    print("0. Exit")
    print("Please select an option")
    choice = input()
    
    
        
    if choice=='1':
        print("")
        ec2create_instance.ec2create_Instance()

    if choice=='2':
        ec2list_instances.ec2list_Instances()

    if choice=='3':
        S3create_bucket.S3create_Bucket()
            
    if choice=='4':
        S3put_bucket.S3put_Bucket()


    if choice=='5': 
        S3list_bucket.S3list_Bucket()

    if choice=='6':
        ec2create_cloudwatch.ec2create_Cloudwatch()
        

    if choice=='7':
        S3delete_bucket.S3Delete_Bucket()

    if choice=='8':
        ec2delete_instance.ec2delete_Instance()

    if choice=='9':
        S3deletecontents_bucket.S3deletecontents_Bucket()

    if choice=='10':
        ec2ssh.ec2SSH()

    if choice == '11':
        urladdpictureto.Urladdpictureto()



    if choice =='12':
       addImgtoec2.addImgtoEc2()

    if choice=='0':
        print ("You have left ec2Instance maker")
        exit()

menu()