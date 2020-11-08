import os
import getpass

from AWS.aws import Aws
from BIGDATA.hadoop import HadoopMainMenu
from Devops.Docker.Docker import dockerMain
from Linux.LVM import LVM
from Linux.webserver import webserverMain

menuPass = "1"
x = getpass.getpass()
if x != menuPass:
    print("Wrong password")
    exit()


def mainMenu():
    while True:
        os.system('tput setaf 4')
        print("""
        ===================================================
                   Welcome to Menu Program
        ===================================================
                    Press 1: For AWS
                    Press 2: For Hadoop	
                    Press 3: For Lvm
                    Press 4: For Docker
                    Press 5: For Webserver 
                    Press 6: For Exit
             """)
        os.system('tput setaf 7')
        choice = input("\n Enter Your Choice:")
        if choice == '1':
            Aws()
        elif choice == '2':
            HadoopMainMenu()
        elif choice == '3':
            LVM()
        elif choice == '4':
            dockerMain()
        elif choice == "5":
            webserverMain()
        else:
            exit()

mainMenu()