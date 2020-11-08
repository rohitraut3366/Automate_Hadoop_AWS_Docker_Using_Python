import os, subprocess ,getpass


def localWbs(output):
    output = subprocess.getoutput("cat /etc/os-release")
    if "rhel" in output:
        if not os.system("yum install httpd -y"):
            if not subprocess.getstatusoutput("systemctl start httpd")[0]:
                os.system("systemctl enbale httpd")
            else:
                os.system("httpd")
        else:
            print("error")
    elif "Ubuntu" in output:
        if not subprocess.getstatusoutput("apt-get install apache2")[0]:
            if not subprocess.getstatusoutput("service apache2 start"):
                os.system("systemctl start apache2")
        else:
            print("error")
    else:
        pass
##################################################


def remoteWbs(output, usernme, password, ip):
    if "rhel" in output:
        if not os.system("sshpass -p {} ssh {}@{} yum install httpd -y".format(password, usernme, ip)):
            os.system("sshpass -p {} ssh {}@{} systemctl start httpd".format(password, usernme, ip))
            os.system("sshpass -p {} ssh {}@{} systemctl enbale httpd".format(password, usernme, ip))
    elif "Ubuntu" in output:
        if not os.system("sshpass -p {} ssh {}@{} apt-get install apache2".format(password, usernme, ip)):
            if not subprocess.getstatusoutput("sshpass -p {} ssh {}@{} service apache2 start".format(password, usernme, ip))[0]:
                os.system("sshpass -p {} ssh {}@{} systemctl start apache2".format(password, usernme, ip))
    else:
        pass
###################################################


def cloudWbs(output, username, key, ip):
    if "rhel" in output:
        if not os.system("ssh -i {} {}@{} yum install httpd -y".format(key, username, ip)):
            if not  os.system("ssh -i {} {}@{} systemctl start httpd".format(key, username, ip)):
                os.system("ssh -i {} {}@{} systemctl enbale httpd".format(key, username, ip))
    elif "Ubuntu" in output:
        if not os.system("ssh -i {} {}@{} apt-get install apache2".format(key, username, ip)):
            if not subprocess.getstatusoutput("ssh -i {} {}@{} service apache2 start".format(key, username, ip))[0]:
                os.system("ssh -i {} {}@{} systemctl start apache2".format(key, username, ip))
    else:
        pass
##################################################

def LocalwebDocker(output,name):
    if "CentOS" in output:
        os.system("docker exec {} yum install httpd -y".format(name))
        os.system("docker exec {} /usr/sbin/httpd".format(name))
    else:
        print("This code only support CENTOS")
def PasswordwebDocker(username,password,IP,output,name):
    if "CentOS" in output:
        os.system("sshpass -p {} ssh {}@{} sudo docker exec {} sudo yum install httpd -y".format(password,username,IP,name))
        os.system("sshpass -p {} ssh {}@{} sudo docker exec {} sudo /usr/sbin/httpd".format(password,username,IP,name))
    else:
        print("This code only support CENTOS")
def KeywebDocker(path,username,IP,output,name):
    if "CentOS" in output:
        os.system("ssh -i {} {}@{} sudo docker exec {} sudo yum install httpd -y".format(path,username,IP,name))

        os.system("ssh -i {} {}@{} sudo docker exec {} sudo /usr/sbin/httpd".format(path,username,IP,name))
    else:
        print("This code only support CENTOS")


#############################################




def webserverMain():
    while True:
        print("""
        Enter 1 to Configure on Local System
        Enter 2 to Configure on remote system
        Enter 3 to configure on docker container
        Enter 4 to return
        """)
        choice = input("Enter  your choice: ")
        if choice == "1":
            output = os.system("cat /etc/release-os")
            LocalwebDocker(output)



        elif choice == "2":
            ip = input("Enter IP address: ")
            username = input("Enter username: ")
            key_or_pass = input("Login in VM using key/password: ")
            if key_or_pass == "password":
                password = getpass.getpass()
                output = subprocess.getoutput("sshpass -p {} ssh {}@{} cat /etc/release-os".format(password,username,ip))
                remoteWbs(output,username,password,ip)
            elif key_or_pass.lower() == "key":
                path = input("Enter remote os login key path [path/key.pem] ")
                output= subprocess.getoutput("ssh -i {} {}@{} cat /etc/release-os".format(path,username,ip))
                cloudWbs(output,username,path,ip)
            else:
                print("Wrong choice")




        elif choice == "3":
            vm = input("VM is local/remote where docker is running : ")
            if vm == "local":
                con_name = input("Enter container name/ID :")
                output = subprocess.getoutput("docker exec {} cat /etc/release-os".format(con_name))
                LocalwebDocker(output,con_name)
            elif vm  == "remote":
                ip = input("Enter VM IP address: ")
                username = input("Enter username: ")
                key_or_pass = input("Login to VM using key/password: ")
                if key_or_pass == "password":
                    password = input("Enter vm password: ")
                    con_name = input("Enter container name: ")
                    output = subprocess.getoutput("sshpass -p {} ssh {}@{} docker exec {} cat /etc/release-os".format(password,username,ip,con_name))
                    PasswordwebDocker(username,password,ip,output,con_name)
                elif key_or_pass.lower() == "key":
                    path = input("Enter key path [path/key.pem]")
                    con_name = input("Enter container Name: ")
                    output = subprocess.getoutput("ssh -i {} {}@{} docker exec {} cat /etc/release-os".format(path,username,ip,con_name))
                    KeywebDocker(path,username,ip,output,con_name)
                else:
                    print("Wrong choice")
            else:
                print("Wrong choice")
        else:
            print("Wrong Choice")

