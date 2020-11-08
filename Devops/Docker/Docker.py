import os
import getpass


########################################


def LocalDockerImage():
    while True:
        os.system('tput setaf 4')
        print("""
        Enter 1 to pull
        Enter 2 to remove image
        Enter 3 to docker manu
        """)
        os.system('tput setaf 7')
        choice = input("Enter : ")
        if choice == "1":
            default = "latest"
            image = input("Enter image  name[os]:version ")
            os.system("docker pull {}".format(image))
        elif choice == "2":
            image = input("Enter image  name[os:version]: ").strip()
            os.system("docker rmi {}".format(image))
        elif choice == "3":
            return
        else:
            print("wrong choice")
        input("Enter to continue..")
        os.system("clear")


def LocalDockerContainer():
    while True:
        os.system('tput setaf 4')
        print("""
        Enter 1 to see running containers
        Enter 2 to see all containers
        Enter 3 to create container
        Enter 4 to delete container
        Enter 5 to stop container
        Enter 6 to start container
        Enter 7 to docker menu
        """)
        os.system('tput setaf 7')
        choice = input("Enter your choice : ")
        if choice == '1':
            os.system("docker  ps -a")
        elif choice == "2":
            os.system("docker ps")
        elif choice == '3':
            name = input("Enter name: ")
            osname = input("Enter image [:]")
            os.system("docker  run  -dit --name {}  {}".format(name,osname))
        elif choice == '4':
            name = input("Enter name/ID: ")
            os.system("docker rm -f {}".format(name))
        elif choice == '5':
            name = input("Enter name/ID: ")
            os.system("docker stop {}".format(name))
        elif choice == '6':
            name = input("Enter name/ID: ")
            os.system("docker start {}".format(name))
        elif choice == '7':
            return
        else:
            print("Wrong choice")
        input("Enter to contine..")
        os.system("clear")

####################################################
            #PassOS#
#####################################################3
def RemotedockerImage(username,password,IP):
    while True:
        os.system('tput setaf 4')
        print("""
        Enter 1 to pull
        Enter 2 to remove image
        Enter 3 to docker manu
        """)
        os.system('tput setaf 7')
        choice = input("Enter : ")
        if choice == "1":
            default = "latest"
            image = input("Enter image  name[os]:version ")
            os.system("sshpass -p {} ssh {}@{} sudo docker pull ".format(username,password,IP,image))
        elif choice == "2":
            image = input("Enter image  name[os:version]: ").strip()
            os.system("sshpass -p {} ssh {}@{} sudo docker rmi {}".format(username,password,IP,image))
        elif choice == "3":
            return
        else:
            print("wrong choice")
        input("Enter to continue..")
        os.system("clear")


def RemoteDockerContainer(username,password,IP):
    while True:
        os.system('tput setaf 4')
        print("""
        Enter 1 to see running containers
        Enter 2 to see all containers
        Enter 3 to create container
        Enter 4 to delete container
        Enter 5 to stop container
        Enter 6 to start container
        Enter 7 to docker menu
        """)
        os.system('tput setaf 7')
        choice = input("Enter: ")
        if choice == '1':
            os.system("sshpass -p {} ssh {}@{} sudo docker  ps -a")
        elif choice == "2":
            os.system("sshpass -p {} ssh {}@{} sudo docker ps")
        elif choice == '3':
            name = input("Enter name: ")
            osname = input("Enter image [:]")
            os.system("sshpass -p {} ssh {}@{} sudo docker run -dit --name {} {}".format(password,username,IP,name,osname))
        elif choice == '4':
            name = input("Enter name/ID: ")
            os.system("sshpass -p {} ssh {}@{} sudo docker rm -f {}".format(password,username,IP,name))
        elif choice == '5':
            name = input("Enter name/ID: ")
            os.system("sshpass -p {} ssh {}@{} sudo docker stop {}".format(password,username,IP,name))
        elif choice == '6':
            name = input("Enter name/ID: ")
            os.system("sshpass -p {} ssh {}@{} sudo docker start {}".format(password,username,IP,name))
        elif choice == '7':
            return
        else:
            print("Wrong choice")
        input("Enter to contine..")
        os.system("clear")
############################################
            #KeyOS#
############################################
def KeyDockerImage(path,username,IP):
    while True:
        os.system('tput setaf 4')
        print("""
        Enter 1 to pull
        Enter 2 to remove image
        Enter 3 to docker manu
        """)
        os.system('tput setaf 7')
        choice = input("Enter : ")
        if choice == "1":
            default = "latest"
            image = input("Enter image  name[os]:version ")
            os.system("ssh -i  {} {}@{} sudo docker pull ".format(path,username,IP,image))
        elif choice == "2":
            image = input("Enter image  name[os:version]: ").strip()
            os.system("ssh -i  {} {}@{} sudo docker rmi {}".format(path,username,IP,image))
        elif choice == "3":
            return
        else:
            print("wrong choice")
        input("Enter to continue..")
        os.system("clear")


def KeyDockerContainer(path,username,IP):
    while True:
        os.system('tput setaf 4')
        print("""
        Enter 1 to see running containers
        Enter 2 to see all containers
        Enter 3 to create container
        Enter 4 to delete container
        Enter 5 to stop container
        Enter 6 to start container
        Enter 7 to docker menu
        """)
        os.system('tput setaf 7')
        choice = input("Enter: ")
        if choice == '1':
            os.system("ssh -i  {} {}@{} sudo docker  ps -a")
        elif choice == "2":
            os.system("ssh -i  {} {}@{} sudo docker ps")
        elif choice == '3':
            name = input("Enter name: ")
            osname = input("Enter image [:]")
            os.system("ssh -i  {} {}@{} sudo docker run -dit --name {} {}".format(path,username,IP,name,osname))
        elif choice == '4':
            name = input("Enter name/ID: ")
            os.system("ssh -i  {} {}@{} sudo docker rm -f {}".format(path,username,IP,name))
        elif choice == '5':
            name = input("Enter name/ID: ")
            os.system("ssh -i  {} {}@{} sudo docker stop {}".format(path,username,IP,name))
        elif choice == '6':
            name = input("Enter name/ID: ")
            os.system("ssh -i  {} {}@{} sudo docker start {}".format(path,username,IP,name))
        elif choice == '7':
            return
        else:
            print("Wrong choice")
        input("Enter to contine..")
        os.system("clear")


#############################################################
                #MainMenu#
##############################################################
def LocalDockerMenu():
    while True:
        os.system('tput setaf 4')
        print("""
                    Enter 1 to install docker
                    Enter 2 to check docker info
                    Enter 3 to work with Container Images
                    Enter 4 to container operations
                    Enter 5 to main menu
                    """)
        os.system('tput setaf 7')
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("yum install docker-ce --nobest")
        elif choice == '2':
            os.system("docker info")
        elif choice == '3':
            LocalDockerImage()
        elif choice == '4':
            LocalDockerContainer()
        elif choice == '5':
            return
        else:
            print("Wrong choice")
        input("Enter to continue... ")
        os.system("clear")
def remotePassMEnu(username,password,IP):
    while True:
        os.system('tput setaf 4')
        print("""
                        Enter 1 to install docker
                        Enter 2 to check docker info
                        Enter 3 to work with Container Images
                        Enter 4 to container operations
                        Enter 5 to main menu
                        """)
        os.system('tput setaf 7')
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("sshpass -p {} ssh {}@{} sudo yum install docker-ce --nobest".format(password, username, IP))
        elif choice == '2':
            os.system("sshpass -p {} ssh {}@{} sudo docker info".format(password, username, IP))
        elif choice == '3':
            RemotedockerImage(username, password, IP)
        elif choice == '4':
            RemotedockerImage(username, password, IP)
        elif choice == '5':
            return
        else:
            print("Wrong choice")
        input("Enter to continue... ")
        os.system("clear")

def keyDockerOS(path,username,IP):
    while True:
        os.system('tput setaf 4')
        print("""
                            Enter 1 to install docker
                            Enter 2 to check docker info
                            Enter 3 to work with Container Images
                            Enter 4 to container operations
                            Enter 5 to main menu
                            """)
        os.system('tput setaf 7')
        IP = input("Enter IP")
        username = input("Enter username: ")
        path = input("Enter key [keypath/key.pem] : ")
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("ssh -i {} {}@{} sudo yum install docker-ce --nobest".format(path, username, IP))
        elif choice == '2':
            os.system("ssh -i {} {}@{} sudo docker info".format(path, username, IP))
        elif choice == '3':
            KeyDockerImage(path, username, IP)
        elif choice == '4':
            KeyDockerContainer(path, username, IP)
        elif choice == '5':
            return
        else:
            print("Wrong choice")
        input("Enter to continue... ")
        os.system("clear")

def dockerMain():
    ostype = input("Enter local to work on local operating system\n"
                   "Enter remote to work on remote operating system\n"
                   ":")
    if ostype == "local":
        LocalDockerMenu()
    elif ostype == 'remote':
        IP = input("Enter IP Address : ")
        username = input("Enter username : ")
        key_or_pass = input("Login using Key or password : ")
        if key_or_pass == "password":
            password = getpass.getpass()
            remotePassMEnu(username,password,IP)
        elif key_or_pass.lower() == "key":
            path = input("Enter key path [path/key.pem] : ")
            keyDockerOS(path,username,IP)
        else:
            print("Wrong Choice")
    else:
        print("Wrong Choice")
        return


#########################################