import os


##############################_AWS_######################################
def Key():
    while True:
        os.system('tput setaf 4')
        print("""
                Enter 1 to create Key
                Enter 2 to delete Key
                Enter 3 to describe key pairs
                Enter 4 to exit
            """)
        os.system('tput setaf 7')
        choice = input("        Enter your choice : ")
        if choice == "1":
            key_name = input("\t\tEnter Key-name: ")
            os.system(
                "aws ec2 create-key-pair --key-name {} --query KeyMaterial --output text >  {}.pem".format(key_name,
                                                                                                           key_name))
        elif choice == "2":
            key_name = input("\tEnter Key-name: ")
            os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
        elif choice == "3":
            os.system("aws ec2 describe-key-pairs")
        elif choice == "4":
            return
        else:
            print("Wrong Choice")
        input("Enter to continue..")
        os.system("clear")


##########################
def securityGroup():
    while True:
        os.system('tput setaf 4')
        print("""
        Enter 1 To create security Group
        Enter 2 To describe security Group
        Enter 3 To delete security Group
        Enter 4 To add rule of security Group
        Enter 5 To delete rule of security Group
        Enter 6 To exit
        """)
        os.system('tput setaf 7')
        choice = input("Enter your choice")
        if choice == '1':
            description = input("Enter Description of sg : ")
            Group_name = input("Enter sg group Name : ")
            os.system("aws ec2  create-security-group --description {} --group-name {}".format(description, Group_name))
        elif choice == '2':
            os.system("aws ec2 describe-security-groups")
        elif choice == '3':
            id = input("Enter sg Id: ")
            os.system(" aws ec2 delete-security-group --group-id {}".format(id))
        elif choice == '4':
            print("\tEnter 1 for ingress \n\tEnter 2 for egress")
            add = input("Enter your choice : ")
            security_id = input("\tEnter security id: ")
            protocol = input("\tEnter protocol: ")
            port = input("\tEnter Port: ")
            cidr = input("\tEnter Cidr: ")
            if add == "1":
                os.system(
                    "aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(
                        security_id, protocol, port, cidr))
            elif add == "2":
                os.system(
                    "aws ec2 authorize-security-group-egress --group-id {} --protocol {} --port {} --cidr {}".format(
                        security_id, protocol, port, cidr))
            else:
                print("Wrong Choice")
        elif choice == '5':
            print("Enter 1 for ingress \nEnter 2 for egress")
            delete = input("Enter your choice : ")
            security_id = input("            Enter security id: ")
            protocol = input("          Enter protocol: ")
            port = input("          Enter Port: ")
            cidr = input("          Enter Cidr: ")
            if delete == "1":
                os.system(
                    "aws ec2 revoke-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(
                        security_id, protocol, port, cidr))
            elif delete == "2":
                os.system("aws ec2 revoke-security-group-egress --group-id {} --protocol {} --port {} --cidr {}".format(
                    security_id, protocol, port, cidr))
            else:
                print("Wrong Choice")
        elif choice == '6':
            break
        else:
            print("Wrong Choice")
        input("Enter to continue..")
        os.system("clear")


#####################################################
def volume():
    while True:
        os.system('tput setaf 4')
        print("""
        Enter 1 To describe volumes
        Enter 2 To create volumes
        Enter 3 To delete volume
        Enter 4 To attach volume
        Enter 5 To detach volume
        Enter 6 To modify volume
        Enter 7 To exit
            """)
        os.system('tput setaf 7')
        choice = input("Enter your Choice: ")
        if choice == "1":
            os.system("aws ec2 describe-volumes")
        elif choice == "2":
            az = input("Enter AZ : ")
            size = input("size: ")
            os.system("aws ec2 create-volume --availability-zone {} --size {}".format(az, size))
        elif choice == "3":
            volume_id = input("Enter Volume ID : ")
            os.system("aws ec2 delete-volume --volume-id {}".format(volume_id))
        elif choice == "4":
            device = input("Enter  device Name: ")
            instance_id = input("Instance ID: ")
            volume_id = input("Volume ID: ")
            os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {} ".format(device, instance_id, volume_id))
        elif choice == "5":
            volume_id = input("Volume ID: ")
            os.system("aws ec2 detach-volume --volume-id {} --force".format(volume_id))
        elif choice == "6":
            print("modify size only supported others fetures are comming soon")
            size = input("Enter size: ")
            volume_id = input("Enter Volume ID: ")
            os.system("aws ec2 modify-volume --volume-id {} --size {}".format(volume_id, size))
        elif choice == "7":
            return
        else:
            print("Wrong Choice")
        input("Enter to continue..")
        os.system("clear")


#####################################################
def ec2():
    while (True):
        os.system('tput setaf 4')
        print("""
            Enter 1 To get information about your instances
            Enter 2 To launch an EC2 instance
            Enter 3 To Start an instance
            Enter 4 To Stop an instance
            Enter 5 To terminate an instance
            Enter 6 To exit
            """)
        os.system('tput setaf 7')
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("aws ec2 describe-instances")
        elif choice == "2":
            image_id = input("Enter image-id : ")
            cnt = int(input("How many instance you want to launch: "))
            key_name = input("Enter your keyname: ")
            subnet_id = input("Enter subnet-id : ")
            instance_type = input("Enter instance type: ")
            security_group_id = input("Security Group: ")
            os.system(
                "aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --key-name {} --security-group-ids {}".format(
                    image_id, instance_type, cnt, subnet_id, key_name, security_group_id))
            print("Instance Launched !!!")
        elif choice == "3":
            id2 = input("Enter your instance id :")
            os.system("aws ec2 start-instances --instance-ids {}".format(id2))
        elif choice == "4":
            id3 = input("Enter your instance id :")
            os.system("aws ec2 stop-instances --instance-ids {}".format(id3))
        elif choice == "5":
            id = input("Enter instance id: ")
            os.system("aws ec2 terminate-instances --instance-ids {}".format(id))
        else:
            print("Wrong Choice")
            return
        input("Enter to continue......")
        os.system("clear")


##################################################################
def s3():
    while (True):
        os.system('tput setaf 4')
        print('''
                    Press 1: for creating bucket
                    Press 2: for adding object	
                    Press 3: for bucket list
                    Press 4: for deleting bucket
                    Press 5: for deleting object of bucket
                    Press 6: to return 
                    ''')
        os.system('tput setaf 7')
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
            os.system("aws s3 rb s3://{} --force".format(bucket=bn))
        elif choice == "5":
            bn = input("\n ENTER BUCKET NAME: ")
            on = input("\n ENTER OBJECT NAME: ")
            os.system("aws s3 rm s3://{bucket}/{oname}".format(bucket=bn, oname=on))
        elif choice == '6':
            return
        else:
            print("Wrong Choice")
        input("Enter to continue......")
        os.system("clear")



##########################################################3
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
        input("Enter to continue......")
        os.system("clear")


###########################################################
def Aws():
    os.system("aws configure")
    while True:
        os.system('tput setaf 4')
        print('''
                Press 1: FOR KEY PAIR
                Press 2: FOR SECURITY GROUP	
                Press 3: FOR EC2 INSTANCES
                Press 4: FOR VOLUMES
                Press 5: FOR S3
                Press 6: FOR CLOUD FRONT
                Press 7: TO RETURN
                ''')
        os.system('tput setaf 7')
        choice = input("\n Enter Your Choice:")
        if choice == '1':
            Key()
        elif choice == '2':
            securityGroup()
        elif choice == '3':
            ec2()
        elif choice == '4':
            volume()
        elif choice == '5':
            s3()
        elif choice == '6':
            cloudFront()
        elif choice == '7':
            return
        else:
            print("Wrong choice")
        os.system("clear")

