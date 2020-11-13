
#!/usr/bin/env python3 
def ec2SSH ():
    import sys 
    import boto3
    import subprocess
    from ec2list_instances import ec2list_Instances
    ec2 = boto3.resource('ec2')
    print("yes")
    ec2list_Instances()
    print("This is remote instance access")
    print("please enter the Id of the Instance youd like to remotley access: ") 
    ids = input() #adding in user input 
    print("your password from your laptop")
    for instance in ec2.instances.all():
        if instance.id == ids:
            ids = (instance.id)
            dns = instance.public_dns_name

    ssh_cmd = 'sudo ssh -i Douglas_key.pem ec2-user@'+ dns  #ssh with sudo to be able to use ssh and add an image onto my instance 
    subprocess.run(ssh_cmd, shell = True)

