import os, subprocess

# from menu import mainMenu


def Key():
    while True:
        #os.system("clear")
        print("""
        Enter 1 to create Key
        Enter 2 to delete Key
        Enter 3 to describe key pairs
        Enter 4 to exit
        """)
        choice = input("        Enter your choice : ")
        if choice == "1":
            key_name = input("Enter Key-name: ")
            os.system("aws ec2 create-key-pair --key-name {} --query KeyMaterial --output text >  {}.pem".format(key_name, key_name))
        elif choice == "2":
            key_name = input("Enter Key-name")
            os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
        elif choice == "3":
            os.system("aws ec2 describe-key-pairs")
        elif choice == "4":
            return
        else:
            print("Wrong Choice")
        input("Enter to continue..")
        os.system("clear")


def securityGroup():
    while True:
        print("""
        Enter 1 To create security Group
        Enter 2 To describe security Group
        Enter 3 To delete security Group
        Enter 4 To add rule of security Group
        Enter 5 To delete rule of security Group
        Enter 6 To exit
        """)
        choice = int(input("Enter your choice"))
        if choice == 1:
            description = input("Enter Description of sg : ")
            Group_name = input("Enter sg group Name : ")
            os.system("aws ec2  create-security-group --description {} --group-name {}".format(description,Group_name))
        elif choice == 2:
            os.system("aws ec2 describe-security-groups")
        elif choice == 3:
            id = input("Enter sg Id: ")
            os.system(" aws ec2 delete-security-group --group-id {}".format(id))
        elif choice == 4:
            print("     Enter 1 for ingress \n      Enter 2 for egress")
            add = input("Enter your choice : ")
            security_id = input("            Enter security id: ")
            protocol = input("          Enter protocol: ")
            port = input("          Enter Port: ")
            cidr = input("          Enter Cidr: ")
            if add == "1":
                os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(security_id,protocol,port,cidr))
            elif add == "2":
                os.system("aws ec2 authorize-security-group-egress --group-id {} --protocol {} --port {} --cidr {}".format(security_id, protocol, port, cidr))
            else:
                print("Wrong Choice")
        elif choice == 5:
            print("Enter 1 for ingress \nEnter 2 for egress")
            delete = input("Enter your choice : ")
            security_id = input("            Enter security id: ")
            protocol = input("          Enter protocol: ")
            port = input("          Enter Port: ")
            cidr = input("          Enter Cidr: ")
            if delete == "1":
                os.system("aws ec2 revoke-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(security_id,protocol,port,cidr))
            elif delete == "2":
                os.system("aws ec2 revoke-security-group-egress --group-id {} --protocol {} --port {} --cidr {}".format(security_id, protocol, port, cidr))
            else:
                print("Wrong Choice")
        elif choice == 6:
            break
        else:
            print("Wrong Choice")
        input("Enter to continue..")
        os.system("clear")


def volume():
    while True:
        print("""
        Enter 1 To describe volumes
        Enter 2 To create volumes
        Enter 3 To delete volume
        Enter 4 To attach volume
        Enter 5 To detach volume
        Enter 6 To modify volume
        Enter 7 To exit
            """)
        choice=input("Enter your Choice: ")
        if choice == "1":
            os.system("aws ec2 describe-volumes")
        elif choice == "2":
            az = input("Enter AZ : ")
            size = input("size: ")
            os.system("aws ec2 create-volume --availability-zone {} --size {}".format(az,size))
        elif choice == "3":
            volume_id = input("Enter Volume ID : ")
            os.system("aws ec2 delete-volume --volume-id {}".format(volume_id))
        elif choice == "4":
            device = input("Enter  device Name: ")
            instance_id = input("Instance ID: ")
            volume_id = input("Volume ID: ")
            os.system("aws ec2 --device{} --instance-id {} --volume-id {} ".format(device,instance_id,volume_id))
        elif choice == "5":
            volume_id = input("Volume ID: ")
            os.system("aws ec2 detach-volume --volume-id {} --force".format(volume_id))
        elif choice == "6":
            print("modify size only support others comming soon")
            size = input("Enter size: ")
            os.system("aws ec2 modify-volume --volume-id --size {}".format(size))
        elif choice == "7":
            return
        else:
            print("Wrong Choice")
        input("Enter to continue..")
        os.system("clear")


def ec2():
    while (True):
        print("""
            Enter 1 To get information about your instances
            Enter 2 To launch an EC2 instance
            Enter 3 To Start an instance
            Enter 4 To Stop an instance
            Enter 5 To exit
            """)
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("aws ec2 describe-instances")
        elif choice == "2":
            image_id =  input("Enter image-id : ")
            cnt = int(input("How many instance you want to launch: "))
            key_name = input("Enter your keyname: ")
            subnet_id = input("Enter subnet-id : ")
            instance_type = input("Enter instagnce type")
            security_group_id = input("Security Group: ")
            os.system(
                "aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --key-name {} --security-group-ids {}".format(
                    image_id,instance_type ,cnt, subnet_id, key_name,security_group_id))
            print("Instance Launched !!!")
        elif choice == "3":
            id2 = input("Enter your instance id :")
            os.system("aws ec2 start-instances --instance-ids {}".format(id2))
        elif choice == "4":
            id3 = input("Enter your instance id :")
            os.system("aws ec2 stop-instances --instance-ids {}".format(id3))
        else:
            print("Wrong Choice")
            return


def s3():
    while (True):
        print('''
                    Press 1: for creating bucket
                    Press 2: for adding object	
                    Press 3: for bucket list
                    Press 4: for deleting bucket
                    Press 5: for deleting object of bucket
                    ''')
        choice = input("Enter your choice :")
        if choice == "1":
            bn = input("ENTER BUCKET NAME: ")
            r = input("ENTER REGION: ")
            os.system(
                " aws s3api create-bucket --bucket {bucket}  --region {region} --create-bucket-configuration  LocationConstraint=ap-south-1".format(
                    bucket=bn, region=r))
        elif choice == "2":
            bn = input("\n ENTER BUCKET NAME: ")
            print("LIST OF OBJECTS PRESENT IN {bucket}".format(bucket=bn))
            os.system("aws s3 ls s3://{bucket} ".format(bucket=bn))
            op = input("ADD AN OBJECT (Y/N):")
            if op == "Y":
                lc = input("ENTER location: ")
                os.system("aws s3 ls s3://{bucket} ")
                os.system("aws s3 sync {location} s3://{bucket} --acl public-read".format(location=lc, bucket=bn))
        elif choice == "3":
            os.system('aws s3api list-buckets --query "Buckets[].Name"')
        elif choice == "4":
            bn = input("\n ENTER BUCKET NAME: ")
            r = input("\n ENTER REGION:")
            os.system("aws s3api delete-bucket --bucket {bucket} --region {region}".format(bucket=bn, region=r))
        elif choice == "5":
            bn = input("\n ENTER BUCKET NAME: ")
            on = input("\n ENTER OBJECT NAME: ")
            os.system("aws s3 rm s3://{bucket}/{oname}".format(bucket=bn, oname=on))
        else:
            print("Wrong choice")
            return


def cloudFront():
    while (True):
        cf = input('Press 1: for creating distribution')
        if cf == "1":
            bucketnm = input("\n ENTER RESPECTIVE BUCKET NAME:")
            objectnm = input("\n ENTER THE OBJECT NAME YOU WANT TO DISTRIBUTE [optional]:")
            os.system(
                "aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(
                    bucketnm, objectnm))
        else:
            print("Exit")
            return



