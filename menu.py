import os
import getpass
import subprocess
from AWS.aws import Key, volume, s3, securityGroup, ec2, cloudFront
from BIGDATA.hadoop import LocalHadoopInstall, LocalCurrentNode, RemoteHadoopInstall, RemoteCurrentNode, \
    CloudHadoopInstall, CloudCurrentNode
from Devops.Docker.Docker import dockerMenu
from Linux.webserver import localWbs, cloudWbs, remoteWbs

menuPass = "9a17e517"
x = getpass.getpass()
if x != menuPass:
    print("Wrong password")
    exit()


def mainMenu():
    os.system('tput setaf 3')
    print("\t\t\tWelcome to my menu !!")
    print("\t\t\t---------------------")
    os.system('tput setaf 7')

    ostype = input("Enter cloud to Work on cloud"
                   "\nEnter local to work on local operating system"
                   "\nEnter remote to work on remote operating system"
                   "\n :  ")
    if ostype == "local":
        while True:
            print("""
            Enter 1 to install hadoop
            Enter 2 to configure node
            Enter 3 to format namenode
            Enter 4 to start/stop hadoop service
            Enter 5 to get cluster report
            Enter 6 to  see all files
            Enter 7 to put/rm/read File
            Enter 8 to configure webserver
            Enter 9 to work on docker
            Enter 10 to exit
                """)
            choice = input("Enter your choice: ")
            if choice == "1":
                LocalHadoopInstall()
            elif choice == "2":
                LocalCurrentNode()
            elif choice == '3':
                os.system("hadoop namenode -format")
            elif choice == "4":
                s = input("Enter start/stop hadoop service : ")
                if s == "start":
                    service = input("service NameNode/Datanode : ")
                    if service.lower() == "namenode":
                        os.system("hadoop-daemon.sh start namenode")
                    elif service.lower() == "datanode":
                        os.system("hadoop-daemon.sh start datanode")
                elif s == "stop":
                    service = input("service NameNode/Datanode : ")
                    if service.lower() == "namenode":
                        os.system("hadoop-daemon.sh stop namenode")
                    elif service.lower() == "datanode":
                        os.system("hadoop-daemon.sh stop datanode")
                else:
                    print("wrong input ")
            elif choice == "5":
                os.system("hadoop dfsadmin -report")
            elif choice == "6":
                os.system("hadoop fs -ls /")
            elif choice == "7":
                c = input("Enter put/rm/read File")
                if c.lower() =='put':
                    file_name = input("Enter file name [PATH/filename] : ")
                    os.system("hadoop fs -put {} /".format(file_name))
                elif c.lower() == "rm":
                    file_name = input("Enter File name : ")
                    os.system("hadoop fs -rm /{}".format(file_name))
                elif c.lower() == "read":
                    file_name = input("Enter file name : ")
                    os.system("hadoop fs -cat /{}".format(file_name))
            elif choice == "8":
                output = subprocess.getoutput("cat /etc/os-release")
                localWbs(output)
            elif choice == '9':
                dockerMenu()
            elif choice == "10":
                exit()
            else:
                print("not supported")
            input("Press Enter to continue........")
            os.system('clear')

    elif ostype == "remote":
        username = input("Enter os username : ").strip()
        ip = input("Enter os ip: ").strip()
        key_or_password = input("Connect using password/Key : ").strip()
        if key_or_password.lower() == "password" or key_or_password == "pass":
            password = getpass.getpass("Enter password: ")
            os.system("yum install sshpass")
            while True:
                print("""
                Enter 1 to install hadoop
                Enter 2 for configure node
                Enter 3 to format namenode
                Enter 4 for start/stop hadoop service
                Enter 5 for get cluster report
                Enter 6 to see all files in cluster
                Enter 7 to put/rm/read File
                Enter 8 to configure webserver
                Enter 9 to exit
                """)
                choice = input("Enter you choice : ")
                if choice == "1":
                    RemoteHadoopInstall(username, password, ip)
                elif choice == "2":
                    RemoteCurrentNode(username, password, ip)
                elif choice == "3":
                    os.system(
                        "sshpass -p {} ssh {}@{} hadoop namenode -format".format(password, username, ip))
                elif choice == "4":
                    s = input("Enter start/stop hadoop service : ")
                    if s == "start":
                        service = input("service NameNode/Datanode : ")
                        if service.lower() == "namenode":
                            os.system(
                                "sshpass -p {} ssh {}@{} hadoop-daemon.sh start namenode".format(password, username,
                                                                                                 ip))
                            os.system('sleep 3')
                            service_state = subprocess.getstatusoutput(
                                "sshpass -p {} ssh {}@{} sudo jps".format(password, username, ip))
                            if service_state[0] == 0 and 'NameNode' in service_state[1]:
                                print("NameNode Started")
                            else:
                                print("failed to start service")
                        elif service.lower() == "datanode":
                            os.system(
                                "sshpass -p {} ssh {}@{} hadoop-daemon.sh start datanode".format(password, username,
                                                                                                 ip))
                            os.system('sleep 3')
                            service_state = subprocess.getstatusoutput(
                                "sshpass -p {} ssh {}@{} sudo jps".format(password, username, ip))
                            if service_state[0] == 0 and 'DataNode' in service_state[1]:
                                print("DataNode Started")
                            else:
                                print("failed to start service")
                        else:
                            print("Wrong Input")
                    elif s == "stop":
                        service = input("service NameNode/Datanode : ")
                        if service.lower() == "namenode":
                            os.system(
                                "sshpass -p {} ssh {}@{} hadoop-daemon.sh stop namenode".format(password, username, ip))
                        elif service.lower() == "datanode":
                            os.system(
                                "sshpass -p {} ssh {}@{} hadoop-daemon.sh stop datanode".format(password, username, ip))
                        else:
                            print("Wrong Input")
                    else:
                        print("wrong input ")
                elif choice == '5':
                    os.system(
                        "sshpass -p {} ssh {}@{} hadoop dfsadmin -report".format(password, username, ip))
                elif choice == '6':
                    os.system(
                        "sshpass -p {} ssh {}@{} hadoop fs -ls /".format(password, username, ip))
                elif choice == "7":
                    c = input("Enter put/rm/read File")
                    if c.lower() == 'put':
                        file_name = input("Enter file name [PATH/filename] : ")
                        os.system("sshpass -p {} ssh {}@{} hadoop fs -put {} /".format(password, username, ip, file_name))
                    elif c.lower() == "rm":
                        file_name = input("Enter File name : ")
                        os.system("sshpass -p {} ssh {}@{} hadoop fs -rm /{}".format(password, username, ip, file_name))
                    elif c.lower() == "read":
                        file_name = input("Enter file name : ")
                        os.system("sshpass -p {} ssh {}@{} hadoop fs -cat /{}".format(password, username, ip, file_name))
                elif choice == '8':
                    output = subprocess.getoutput(
                        "sshpass -p {} ssh {}@{} cat /etc/os-release".format(password, username, ip))
                    localWbs(output)
                elif choice == '9':
                    exit()
                else:
                    print("not supported")

                input("Press Enter to continue........")
                os.system('clear')
        elif key_or_password.lower() == "key":
            key = input("Enter key in this format { PATH/KeyName.pem } : ")
            while True:
                print("""
                Enter 1 to install hadoop
                Enter 2 for configure node
                Enter 3 to format namenode
                Enter 4 start/stop hadoop service
                Enter 5 to get cluster report
                Enter 6 to see all files in cluster
                Enter 7 to put/read/rm file in cluster
                Enter 8 to configure webserver
                Enter 9 to exit
                """)
                choice = input("Enter your choice: ")
                if choice == "1":
                    CloudHadoopInstall(username, key, ip)
                elif choice == "2":
                    CloudCurrentNode(username, key, ip)
                elif choice == "3":
                    os.system("ssh -i {} {}@{} sudo hadoop namenode -format".format(key, username, ip))
                elif choice == "4":
                    s = input("Enter start/stop hadoop service : ")
                    if s == "start":
                        service = input("service NameNode/Datanode : ")
                        if service.lower() == "namenode":
                            os.system(
                                "ssh -i {} {}@{} sudo hadoop-daemon.sh start namenode".format(key, username, ip))
                            os.system('sleep 3')
                            service_state = subprocess.getstatusoutput(
                                "ssh -i {} {}@{} sudo jps".format(key, username, ip))
                            if service_state[0] == 0 and 'NameNode' in service_state[1]:
                                print("NameNode Started")
                            else:
                                print("failed to start service")
                        elif service.lower() == "datanode":
                            os.system(
                                "ssh -i {} {}@{} sudo hadoop-daemon.sh start datanode".format(key, username, ip))
                            os.system('sleep 3')
                            service_state = subprocess.getstatusoutput(
                                "ssh -i {} {}@{} sudo jps".format(key, username, ip))
                            if service_state[0] == 0 and 'DataNode' in service_state[1]:
                                print("DataNode Started")
                            else:
                                print("failed to start service")
                        else:
                            print("Wrong Input")

                    elif s == "stop":
                        service = input("service NameNode/Datanode : ")
                        if service.lower() == "namenode":
                            os.system(
                                "ssh -i {} {}@{} sudo hadoop-daemon.sh stop namenode".format(key, username, ip))
                        elif service.lower() == "datanode":
                            os.system(
                                "ssh -i {} {}@{} sudo hadoop-daemon.sh stop datanode".format(key, username, ip))
                        else:
                            print("Wrong Input")
                    else:
                        print("wrong input ")
                elif choice == '5':
                    os.system(
                        "ssh -i {} {}@{} sudo hadoop dfsadmin -report".format(key, username, ip))
                elif choice == '6':
                    os.system(
                        "ssh -i {} {}@{} sudo hadoop fs -ls /".format(key, username, ip))
                elif choice == "7":
                    c = input("Enter put/rm/read File")
                    if c.lower() == 'put':
                        file_name = input("Enter file name [PATH/filename] : ")
                        os.system("ssh -i {} {}@{} hadoop fs -put {} /".format(key, username, ip, file_name))
                    elif c.lower() == "rm":
                        file_name = input("Enter File name : ")
                        os.system("ssh -i {} {}@{} hadoop fs -rm /{}".format(key, username, ip, file_name))
                    elif c.lower() == "read":
                        file_name = input("Enter file name : ")
                        os.system("ssh -i {} {}@{} hadoop fs -cat /{}".format(key, username, ip, file_name))
                elif choice == '8':
                    os.system("ssh -i {} {}@{} cat /etc/os-release".format(key, username, ip))
                    cloudWbs(key=key, username=username, ip=ip)
                elif choice == '9':
                    exit()
                else:
                    print("not supported")

                input("Press Enter to continue........")
                os.system('clear')

    elif ostype == "cloud":
        print("===============================================================")

        print("\t\t WELCOME TO AWS MENU DRIVEN PROGRAM !!!!")

        print("================================================================")

        print("""\n\n
        		Press 1: FOR CREATE KEY PAIR
        		Press 2: FOR SECURITY GROUP	
        		Press 3: FOR EC2 INSTANCES
        		Press 4: FOR VOLUMES
        		Press 5: FOR S3
        		Press 6: FOR CLOUD FRONT
        		""")
        choice = int(input("\n Enter Your Choice:"))
        if choice == 1:
            Key()
        elif choice == 2:
            securityGroup()
        elif choice == 3:
            ec2()
        elif choice == 4:
            volume()
        elif choice == 5:
            s3()
        elif choice == 6:
            cloudFront()
        else:
            print("not supported")
            exit()
        input("Press Enter to continue........")
        os.system('clear')

    else:
        print("Wrong Choice, Enter cloud/local/remote system")
mainMenu()
