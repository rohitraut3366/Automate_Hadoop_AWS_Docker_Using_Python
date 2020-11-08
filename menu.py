import os
import getpass

from AWS.aws import Aws
from BIGDATA.hadoop import HadoopMainMenu
from Devops.Docker.Docker import dockerMain
from Linux.LVM import Lvm

menuPass = "1"
x = getpass.getpass()
if x != menuPass:
    print("Wrong password")
    exit()


def mainMenu():
    while True:
        os.system('tput setaf 4')
        print("""
                    Press 1: For Hadoop
                    Press 2: For AWS	
                    Press 3: For Lvm
                    Press 4: For Docker 
                    Press 5: For Exit
             """)
        os.system('tput setaf 7')
        choice = int(input("\n Enter Your Choice:"))
        if choice == 1:
            HadoopMainMenu()
        elif choice == 2:
            Aws()
        elif choice == 3:
            Lvm()
        elif choice == 4:
            dockerMain()
        else:
            exit()

