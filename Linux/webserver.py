import os,subprocess


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

def webDocker(output,name):
    if "CentOS" in output:
        os.system("docker exec {} yum install httpd -y".format(name))
        os.system("docker exec {} /usr/sbin/httpd".format(name))
    else:
        print("This code only support CENTOS")


#############################################