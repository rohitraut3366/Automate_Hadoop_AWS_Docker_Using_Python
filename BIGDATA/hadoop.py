import os
import subprocess


# installing hadoop and required software
def LocalHadoopInstall():
    status = 1
    print("Please wait")
    if not subprocess.getstatusoutput("sudo yum install initscripts -y")[0]:
        if not subprocess.getstatusoutput("pip3 install gdown")[0]:
            if not os.system("sudo wget https://rohitraut04.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm") and 0 == os.system("sudo wget https://rohitraut04.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm"):
                os.system("sudo rpm -ihv  jdk-8u171-linux-x64.rpm")
                status = os.system("sudo rpm -ihv hadoop-1.2.1-1.x86_64.rpm --force")
 
    if status == 0:
        print("Hadoop successfully installed  in your system")
    else:
        print("something went wrong please contact support team")


# Configure NameNode
def LocalNodeConfigure(current_type):


    # hdfs-site.xml for NameNode
    if current_type == "NameNode":
        os.system("sudo cp BIGDATA/templates/core-site/namenode/core-site.xml /etc/hadoop/core-site.xml")
        folder = input("Enter Directory: ")
        subprocess.getstatusoutput("sudo mkdir {}".format(folder))
        if not os.system("sudo cp BIGDATA/templates/hdfs-site/namenode/hdfs-site.xml /etc/hadoop/hdfs-site.xml"):
            return True

    elif current_type == "DataNode":
        os.system("sudo cp BIGDATA/templates/core-site/datanode/core-site.xml /etc/hadoop/core-site.xml")
        folder = input("Enter Directory: ")
        subprocess.getstatusoutput("sudo mkdir {}".format(folder))
        if not os.system("sudo cp BIGDATA/templates/hdfs-site/datanode/hdfs-site.xml /etc/hadoop/hdfs-site.xml"):
            return True

    else:
        os.system("sudo cp BIGDATA/templates/core-site/datanode/core-site.xml /etc/hadoop/core-site.xml")
        if not os.system("sudo cp BIGDATA/templates/hdfs-site/client/hdfs-site.xml /etc/hadoop/hdfs-site.xml"):
            return True
    return False


# Start service of Current Node
def LocalCurrentNode():
    print("""
    Current system is.....
    Enter 1 For NameNode
    Enter 2 For DataNode
    Enter 3 For Client  
    Enter 4 to return back  
    """)
    choice = input("Enter your Choice: ")
    if choice == "1":
        if LocalNodeConfigure("NameNode"):
            print("completed")
        else:
            print("Something went Wrong")

    elif choice == '2':
        if LocalNodeConfigure("DataNode"):
            print("completed")
        else:
            print("Something Went Wrong")
    elif choice == '3':
        if LocalNodeConfigure("Client"):
            print("Client Started.....")
        else:
            print("Something Went Wrong")
    elif choice == '4':
        return
    else:
        print("Something Went Wrong")

#############################################################################################################################


def RemoteHadoopInstall(username, password, Ip):
    status = None
    if 0 == subprocess.getstatusoutput("sudo yum install initscripts -y")[0]:
        if 0 == os.system("sshpass -p {}  ssh {}@{} yum install wget -y".format(password, username, Ip)):
            if 0 == os.system("sshpass -p {}  ssh {}@{} sudo wget https://rohitraut04.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm".format(password, username, Ip)) and 0 == os.system("sshpass -p {}  ssh {}@{} sudo wget https://rohitraut04.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm".format(password, username, Ip)):
                if 0 == os.system("sshpass -p {}  ssh {}@{} rpm -ihv  jdk-8u171-linux-x64.rpm".format(password, username, Ip)):
                    status = os.system("sshpass -p {}  ssh {}@{} rpm -ihv hadoop-1.2.1-1.x86_64.rpm --force".format(password, username, Ip))
    if status == 0:
        print("Hadoop successfully installed  in your system")
    else:
        print("something went wrong please contact support team")

 
# Configure NameNode
def RemoteNodeConfigure(current_type, username, password, Ip):
    # HDFS-Site file Configure
    if current_type == "NameNode":
        os.system("sshpass -p {} scp BIGDATA/templates/core-site/namenode/core-site.xml {}@{}:/etc/hadoop/core-site.xml".format(
            password, username, Ip))
        folder = input("Enter CurrentNode Directory: ")
        subprocess.getoutput("sshpass -p {} ssh {}@{} sudo mkdir {}".format(password, username, Ip, folder))
        if not os.system("sshpass -p {} scp BIGDATA/templates/hdfs-site/namenode/hdfs-site.xml {}@{}:/etc/hadoop/hdfs-site.xml".format(password, username, Ip)):
            return True

    elif current_type == "DataNode":
        os.system("sshpass -p {} scp BIGDATA/templates/core-site/datanode/core-site.xml {}@{}:/etc/hadoop/core-site.xml".format(
            password, username, Ip))
        folder = input("Enter CurrentNode Directory: ")
        subprocess.getoutput("sshpass -p {} ssh {}@{} sudo mkdir {}".format(password, username, Ip, folder))
        if not os.system("sshpass -p {} scp  BIGDATA/templates/hdfs-site/datanode/hdfs-site.xml {}@{}:/etc/hadoop/hdfs-site.xml".format(password, username, Ip)):
            return True

    else:
        os.system("sshpass -p {} scp BIGDATA/templates/core-site/datanode/core-site.xml {}@{}:/etc/hadoop/core-site.xml".format(
            password, username, Ip))
        if not os.system("sshpass -p {} scp  BIGDATA/templates/hdfs-site/client/hdfs-site.xml {}@{}:/etc/hadoop/hdfs-site.xml".format(password, username, Ip)):
            return True

    return False


# Start service of Current Node
def RemoteCurrentNode(username, password, Ip):
    print("""
    Current system is.....
    Enter 1 For NameNode
    Enter 2 For DataNode
    Enter 3 For Client  
    Enter 4 to return back  
    """)
    choice = input("Enter your Choice: ")
    if choice == "1":
        if RemoteNodeConfigure("NameNode", username, password, Ip):
            print("completed")
        else:
            print("Something went Wrong")
    elif choice == '2':
        if RemoteNodeConfigure("DataNode", username, password, Ip):
            print("completed")
        else:
            print("Something went Wrong")
    elif choice == '3':
        if RemoteNodeConfigure("Client", username, password, Ip):
            print("Completed")
        else:
            print("Something went Wrong")
    elif choice == '4':
        return
    else:
        print("wrong choice")


# ########################################################################################################################3


def CloudHadoopInstall(username, key_path, Ip):
    status = None
    if 0 == subprocess.getstatusoutput("ssh -i {} {}@{} sudo yum install initscripts -y".format(key_path, username, Ip))[0]:
        if 0 == os.system("ssh -i {} {}@{} sudo yum install wget -y".format(key_path, username, Ip)):
            if 0 == os.system("ssh -i {} {}@{} sudo wget https://rohitraut04.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm".format(key_path, username, Ip)) and 0 == os.system("ssh -i {} {}@{} sudo wget https://rohitraut04.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm".format(key_path, username, Ip)):
                if 0 == os.system("ssh -i {} {}@{} sudo rpm -ihv  jdk-8u171-linux-x64.rpm".format(key_path, username, Ip)):
                    status = os.system("ssh -i {} {}@{} sudo rpm -ihv hadoop-1.2.1-1.x86_64.rpm --force".format(key_path, username, Ip))
    if status == 0:
        print("Hadoop successfully installed  in your system")
    else:
        print("something went wrong")


# Configure NameNode
def CloudNodeConfigure(current_type, username, key_path, Ip):

    # HDFS-Site file Configure
    if current_type == "NameNode":
        if not os.system(
                "scp -i {}  BIGDATA/templates/core-site/namenode/core-site.xml {}@{}:/home/{}/".format(key_path, username, Ip,
                                                                                              username)) and not os.system(
                "ssh -i {} {}@{} sudo cp core-site.xml /etc/hadoop/core-site.xml".format(key_path, username,
                                                                                         Ip)) and not os.system(
                "ssh -i {} {}@{} sudo rm core-site.xml".format(key_path, username, Ip)):
            pass
        else:
            return False
        folder = input("Enter Directory: ")
        subprocess.getoutput("ssh -i {} {}@{} sudo mkdir {}".format(key_path, username, Ip, folder))
        if not os.system("scp -i {} BIGDATA/templates/hdfs-site/namenode/hdfs-site.xml {}@{}:/home/{}/".format(key_path, username, Ip, username)) and not os.system("ssh -i {} {}@{} sudo cp hdfs-site.xml /etc/hadoop/hdfs-site.xml".format(key_path, username, Ip)) and not os.system("ssh -i {} {}@{} sudo rm hdfs-site.xml".format(key_path, username, Ip)):
            return True
    elif current_type == "DataNode":
        if not os.system(
                "scp -i {}  BIGDATA/templates/core-site/datanode/core-site.xml {}@{}:/home/{}/".format(key_path, username, Ip,
                                                                                              username)) and not os.system(
                "ssh -i {} {}@{} sudo cp core-site.xml /etc/hadoop/core-site.xml".format(key_path, username,
                                                                                         Ip)) and not os.system(
                "ssh -i {} {}@{} sudo rm core-site.xml".format(key_path, username, Ip)):
            pass
        else:
            return False
        folder = input("Enter Directory: ")
        subprocess.getoutput("ssh -i {} {}@{} sudo mkdir {}".format(key_path, username, Ip, folder))
        if not os.system("scp -i {} BIGDATA/templates/hdfs-site/datanode/hdfs-site.xml {}@{}:/home/{}/".format(key_path, username, Ip, username)) and not os.system("ssh -i {} {}@{} sudo cp hdfs-site.xml /etc/hadoop/hdfs-site.xml".format(key_path, username, Ip)) and not os.system("ssh -i {} {}@{} sudo rm hdfs-site.xml".format(key_path, username, Ip)):
            return True
    else:
        if not os.system(
                "scp -i {}  BIGDATA/templates/core-site/datanode/core-site.xml {}@{}:/home/{}/".format(key_path, username, Ip,
                                                                                              username)) and not os.system(
                "ssh -i {} {}@{} sudo cp core-site.xml /etc/hadoop/core-site.xml".format(key_path, username,
                                                                                         Ip)) and not os.system(
                "ssh -i {} {}@{} sudo rm core-site.xml".format(key_path, username, Ip)):
            pass
        else:
            return False
        if not os.system("scp -i {} BIGDATA/templates/hdfs-site/client/hdfs-site.xml {}@{}:/home/{}/".format(key_path, username, Ip, username)) and not os.system("ssh -i {} {}@{} sudo cp hdfs-site.xml /etc/hadoop/hdfs-site.xml".format(key_path, username, Ip)) and not os.system("ssh -i {} {}@{} sudo rm hdfs-site.xml".format(key_path, username, Ip)):
            return True
    return False


# Start service of Current Node
def CloudCurrentNode(username, key_path, Ip):
    print("""
    Current system is.....
    Enter 1 For NameNode
    Enter 2 For DataNode
    Enter 3 For Client   
    Enter 4 to return back 
    """)
    choice = input("Enter your Choice: ")
    if choice == "1":
        if CloudNodeConfigure("NameNode", username, key_path, Ip):
            print("completed")
        else:
            print("Something went Wrong")

    elif choice == '2':
        if CloudNodeConfigure("DataNode", username, key_path, Ip):
            print("Completed")
        else:
            print("Something went Wrong")

    elif choice == '3':
        if CloudNodeConfigure("Client", key_path, username, Ip):
            print("Client Started.....")
        else:
            print("Something went Wrong")
    elif choice == '4':
        return
    else:
        print(" wrong choice")
