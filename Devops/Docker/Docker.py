import os

from Linux.webserver import webDocker



def dockerImage():
    while True:
        print("""
        Enter 1 to pull
        Enter 2 to remove image
        Enter 3 to docker manu
        """)
        choice = input("Enter : ")
        if choice == "1":
            default = "latest"
            image = input("Enter image  name[os]:version ")
            os.system("docker pull ".format(image))
        elif choice == "2":
            image = input("Enter image  name[os:version]: ").strip()
            os.system("docker rmi {}".format(image))
        elif choice == "3":
            return
        else:
            print("wrong choice")
        input("Enter to continue..")
        os.system("clear")

def dockerContainer():
    while True:
        print("""
        Enter 1 to see running containers
        Enter 2 to see all containers
        Enter 3 to create container
        Enter 4 to delete container
        Enter 5 to stop container
        Enter 6 to start container
        Enter 7 to docker menu
        """)
        choice = input("Enter: ")
        if choice == '1':
            os.system("docker  ps -a")
        elif choice == "2":
            os.system("docker ps")
        elif choice == '3':
            name = input("Enter name: ")
            osname = input("Enter image [:]")
            os.system("docker -dit run --name {} {}".format(name,osname))
        elif choice == '4':
            name = input("Enter name/ID: ")
            os.system("docker rm {}".format(name))
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
        os.system("clear")


def dockerMenu():
    while True:
        print("""
        Enter 1 to check docker info
        Enter 2 to work with Container Images
        Enter 3 to container operations
        Enter 4 to configure webserver in container
        Enter 5 to exit
        Enter 6 to main menu
        """)
        choice = input("Enter your choice: ")
        if choice == '1':
            os.system("docker info")
        elif choice == '2':
            dockerImage()
        elif choice == '3':
            dockerContainer()
        elif choice == '4':
            name = input("container name/Id : ").strip()
            t = os.system("docker exec {} cat /etc/os-release".format(name))
            webDocker(t, name=name)
        elif choice == '5':
            exit()
        elif choice == '6':
            return
        else:
            print("Wrong choice")

