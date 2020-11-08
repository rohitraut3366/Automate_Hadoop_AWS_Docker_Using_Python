import os
import getpass


def Local_LVM():
    while True:
        os.system('tput setaf 4')
        print("""
        ====================================
                WELCOME TO MY LVM MENU
        ====================================
        PRESS 1:DISPLAY HARDISK INFORMATION
        PRESS 2:DISPLAY MOUNT POINTS
        PRESS 3:CREATE PV,CREATE VG,CREATE LV,CREATE FOLDER,MOUNT LV
        PRESS 4:DISPLAY LV/VG/PV
        PRESS 5:EXTEND VG/LV
        PRESS 6:REDUCE LV
        PRESS 7:TO Return
        """)
        os.system('tput setaf 7')
        choice = input("ENTER YOUR CHOICE:")
        if choice == '1':
            os.system("fdisk -l")
        elif choice == '2':
            os.system("df -hT")
        elif choice == '3':
                os.system('tput setaf 4')
                print("""
                            PRESS 1:CREATE PV
                            PRESS 2:CREATE VG
                            PRESS 3:CREATE LV
                            PRESS 4:MOUNT LV
                            PRESS 5: RETURN
                    """)
                os.system('tput setaf 7')
                choice = input("Enter your choice: ")
                if choice == '1':
                    hd1 = input("ENTER DISK NAME: ")
                    os.system("pvcreate /dev/" + hd1)
                elif choice == '2':
                    vg_name = input("ENTER VG NAME: ")
                    space_separated_pv_name = input("space separated pv name : ").split()
                    x = " /dev/".join(space_separated_pv_name)
                    os.system("vgcreate {} /dev/{}".format(vg_name,x))
                elif choice == '3':
                    lv_name = input("ENTER NAME OF LV:")
                    vg_name = input("ENTER VG NAME: ")
                    size_of_lv = input("ENTER SIZE OF LV:")
                    os.system("lvcreate --size +{}G --name {} {}".format(size_of_lv,lv_name,vg_name))
                elif choice == "4":
                    lv_name = input("ENTER NAME OF LV:")
                    vg_name = input("ENTER VG NAME: ")
                    os.system("mkfs.ext4 /dev/{}/{}".format(vg_name,lv_name))
                    folder = input("ENTER FOLDER NAME TO MOUNT:")
                    os.system("mkdir /{}".format(folder))
                    os.system("mount /dev/{}/{} /{}".format(vg_name,lv_name,folder))
                elif choice == "5":
                    pass
                else:
                    print("wrong choice")
        elif choice == '4':
            c = input("ENTER PV/LV/VG: ")
            if c.lower() == "pv":
                os.system("pvdisplay")
            elif c.lower() == "vg":
                os.system("vgdisplay")
            elif c.lower() == "lv":
                os.system("lvdisplay")
            else:
                print("wrong choice")
        elif choice == '5':
            c = input("ENTER LV/VG: ")
            if c == 'LV':
                size_change = input("ENTER SIZE TO BE INCREASED:")
                vg_name = input("ENTER VG NAME: ")
                lv_name = input("ENTER NAME OF LV:")
                os.system("lvextend --size +{}G  /dev/{}/{}".format(size_change,vg_name,lv_name))
                os.system("resize2fs /dev/{}/{}".format(vg_name,lv_name))
            elif c =="VG":
                pv = input("Enter new PV name: ")
                vg = input("Enter VG-Name: ")
                os.system("vgextend {} /dev/{}".format(vg,pv))
        elif choice == '6':
            vg_name = input("ENTER VG NAME: ")
            lv_name = input("ENTER NAME OF LV:")
            new_size = input("ENTER SIZE UPTO WHICH LV SHOULD BE REDUCED:")
            if 'n'==input("lv is mounted y/n: "):
                os.system("e2fsck - ff /dev/{}/{}".format(vg_name, lv_name))
                os.system("lvreduce -r -L {}G /dev/{}/{}".format(new_size,vg_name,lv_name))
            else:
                print("please umount lv else you might loose online work")
        elif choice == '7':
            return
        else:
            print("wrong choice")

        input("Enter to continue..")
        os.system("clear")

########################################################


def RemoteLvm(username,password,Ip):
    while True:
        os.system('tput setaf 4')
        print("""
        ======================================
                WELCOME TO MY LVM MENU
        ======================================
        PRESS 1:DISPLAY HARDISK INFORMATION
        PRESS 2:DISPLAY MOUNT POINTS
        PRESS 3:CREATE PV,CREATE VG,CREATE LV,CREATE FOLDER,MOUNT LV
        PRESS 4:DISPLAY LV/VG/PV
        PRESS 5:EXTEND VG/LV
        PRESS 6:REDUCE LV
        PRESS 7:TO Return
        """)
        os.system('tput setaf 7')
        choice = input("ENTER YOUR CHOICE:")
        if choice == '1':
            os.system("sshpass -p {} ssh {}@{} sudo fdisk -l".format(password,username,Ip))
        if choice == '2':
            os.system("sshpass -p {} ssh {}@{} sudo df -hT".format(password,username,Ip))
        elif choice == '3':
                os.system('tput setaf 4')
                print("""
                            PRESS 1:CREATE PV
                            PRESS 2:CREATE VG
                            PRESS 3:CREATE LV
                            PRESS 4:MOUNT LV
                            PRESS 5: RETURN
                    """)
                os.system('tput setaf 7')
                choice = input("Enter your choice: ")
                if choice == '1':
                    hd1 = input("ENTER DISK NAME: ")
                    os.system("sshpass -p {} ssh {}@{} sudo pvcreate /dev/".format(password, username, Ip) + hd1)
                elif choice == '2':
                    vg_name = input("ENTER VG NAME: ")
                    space_separated_pv_name = input("space separated pv name : ").split()
                    x = " /dev/".join(space_separated_pv_name)
                    os.system("sshpass -p {} ssh {}@{} sudo vgcreate {} /dev/{}".format(password, username, Ip, vg_name,x))
                elif choice == '3':
                    lv_name = input("ENTER NAME OF LV:")
                    vg_name = input("ENTER VG NAME: ")
                    size_of_lv = input("ENTER SIZE OF LV:")
                    os.system("sshpass -p {} ssh {}@{} sudo lvcreate --size +{}G --name {} {}".format(password, username, Ip, size_of_lv, lv_name, vg_name))
                elif choice == "4":
                    lv_name = input("ENTER NAME OF LV:")
                    vg_name = input("ENTER VG NAME: ")
                    os.system("sshpass -p {} ssh {}@{} sudo mkfs.ext4 /dev/{}/{}".format(password, username, Ip, vg_name, lv_name))
                    folder = input("ENTER FOLDER NAME TO MOUNT:")
                    os.system("sshpass -p {} ssh {}@{} sudo mkdir /{}".format(password, username, Ip, folder))
                    os.system("sshpass -p {} ssh {}@{} sudo mount /dev/{}/{} /{}".format(password, username, Ip, vg_name, lv_name, folder))
                elif choice == "5":
                    pass
                else:
                    print("wrong choice")
        elif choice == '4':
            c = input("ENTER PV/LV/VG: ")
            if c.lower() == "pv":
                os.system("sshpass -p {} ssh {}@{} sudo pvdisplay".format(password,username,Ip))
            elif c.lower() == "vg":
                os.system("sshpass -p {} ssh {}@{} sudo vgdisplay".format(password,username,Ip))
            elif c.lower() == "lv":
                os.system("sshpass -p {} ssh {}@{} sudo lvdisplay".format(password,username,Ip))
        elif choice == '5':
            c = input("ENTER LV/VG: ")
            if c == 'LV':
                size_change = input("ENTER SIZE TO BE INCREASED:")
                vg_name = input("ENTER VG NAME: ")
                lv_name = input("ENTER NAME OF LV:")
                os.system("sshpass -p {} ssh {}@{} sudo lvextend --size +{}G  /dev/{}/{}".format(password,username,Ip,size_change,vg_name,lv_name))
                os.system("sshpass -p {} ssh {}@{} sudo resize2fs /dev/{}/{}".format(password,username,Ip,vg_name,lv_name))
            elif c =="VG":
                pv = input("Enter new PV name: ")
                vg = input("Enter VG-Name: ")
                os.system("sshpass -p {} ssh {}@{} sudo vgextend {} /dev/{}".format(password,username,Ip, vg,pv))
        elif choice == '6':
            vg_name = input("ENTER VG NAME: ")
            lv_name = input("ENTER NAME OF LV:")
            new_size = input("ENTER SIZE UPTO WHICH LV SHOULD BE REDUCED:")
            if 'n'==input("lv is mounted y/n: "):
                os.system("sshpass -p {} ssh {}@{} sudo e2fsck - ff /dev/{}/{}".format(password,username,Ip,vg_name, lv_name))
                os.system("sshpass -p {} ssh {}@{} sudo lvreduce -r -L {}G /dev/{}/{}".format(password,username,Ip,new_size,vg_name,lv_name))
            else:
                print("please umount lv else you might loose online work")
        elif choice == '7':
            return
        else:
            print("wrong choice")


        input("Enter to continue..")
        os.system("clear")

########################################################


def CloudRemoteLvm(key_path,username,Ip):
    while True:
        os.system('tput setaf 4')
        print("""
        =====================================
                WELCOME TO MY LVM MENU
        =====================================
        PRESS 1:DISPLAY HARDISK INFORMATION
        PRESS 2:DISPLAY MOUNT POINTS
        PRESS 3:CREATE PV,CREATE VG,CREATE LV,CREATE FOLDER,MOUNT LV
        PRESS 4:DISPLAY LV/VG/PV
        PRESS 5:EXTEND VG/LV
        PRESS 6:REDUCE LV
        PRESS 7:TO Return
        """)
        os.system('tput setaf 7')
        choice = input("ENTER YOUR CHOICE:")
        if choice == '1':
            os.system("ls")
            os.system("ssh -i {}  {}@{} sudo fdisk -l".format(key_path,username,Ip))
        if choice == '2':
            os.system("ssh -i {}  {}@{} sudo df -hT".format(key_path,username,Ip))
        elif choice == '3':
                os.system('tput setaf 4')
                print("""
                            PRESS 1:CREATE PV
                            PRESS 2:CREATE VG
                            PRESS 3:CREATE LV
                            PRESS 4:MOUNT LV
                            PRESS 5: RETURN
                    """)
                os.system('tput setaf 7')
                choice = input("Enter your choice: ")
                if choice == '1':
                    hd1 = input("ENTER DISK NAME: ")
                    os.system("ssh -i {} {}@{} sudo pvcreate /dev/".format(key_path,username,Ip) + hd1)
                elif choice == '2':
                    vg_name = input("ENTER VG NAME: ")
                    space_separated_pv_name = input("space separated pv name : ").split()
                    x = " /dev/".join(space_separated_pv_name)
                    os.system("ssh -i {} {}@{} sudo vgcreate {} /dev/{}".format(key_path,username,Ip,vg_name,x))
                elif choice == '3':
                    lv_name = input("ENTER NAME OF LV:")
                    vg_name = input("ENTER VG NAME: ")
                    size_of_lv = input("ENTER SIZE OF LV:")
                    os.system("ssh -i {} {}@{} sudo lvcreate --size +{}G --name {} {}".format(key_path,username,Ip, size_of_lv,lv_name,vg_name))
                elif choice == "4":
                    lv_name = input("ENTER NAME OF LV:")
                    vg_name = input("ENTER VG NAME: ")
                    os.system("ssh -i {} {}@{} sudo mkfs.ext4 /dev/{}/{}".format(key_path,username,Ip, vg_name,lv_name))
                    folder = input("ENTER FOLDER NAME TO MOUNT:")
                    os.system("ssh -i {}  {}@{} sudo mkdir /{}".format(key_path,username,Ip,folder))
                    os.system("ssh -i {}  {}@{} sudo mount /dev/{}/{} /{}".format(key_path,username,Ip, vg_name,lv_name,folder))
                elif choice == "5":
                    pass
                else:
                    print("wrong choice")
        elif choice == '4':
            c = input("ENTER PV/LV/VG: ")
            if c.lower() == "pv":
                os.system("ssh -i {}  {}@{} sudo pvdisplay".format(key_path,username,Ip))
            elif c.lower() == "vg":
                os.system("ssh -i {}  {}@{} sudo vgdisplay".format(key_path,username,Ip))
            elif c.lower() == "lv":
                os.system("ssh -i {}  {}@{} sudo lvdisplay".format(key_path,username,Ip))
        elif choice == '5':
            c = input("ENTER LV/VG: ")
            if c == 'LV':
                size_change = input("ENTER SIZE TO BE INCREASED:")
                vg_name = input("ENTER VG NAME: ")
                lv_name = input("ENTER NAME OF LV:")
                os.system("ssh -i {}  {}@{} sudo lvextend --size +{}G  /dev/{}/{}".format(key_path,username,Ip,size_change,vg_name,lv_name))
                os.system("ssh -i {}  {}@{} sudo resize2fs /dev/{}/{}".format(key_path,username,Ip,vg_name,lv_name))
            elif c =="VG":
                pv = input("Enter new PV name: ")
                vg = input("Enter VG-Name: ")
                os.system("ssh -i {} {}@{} sudo vgextend {} /dev/{}".format(key_path,username,Ip,vg,pv))
        elif choice == '6':
            vg_name = input("ENTER VG NAME: ")
            lv_name = input("ENTER NAME OF LV:")
            new_size = input("ENTER SIZE UPTO WHICH LV SHOULD BE REDUCED:")
            if 'n' == input("lv is mounted y/n: "):
                os.system("ssh -i {} {}@{} sudo e2fsck - ff /dev/{}/{}".format(key_path,username,Ip,vg_name, lv_name))
                os.system("ssh -i {} {}@{} sudo lvreduce -r -L {}G /dev/{}/{}".format(key_path,username,Ip,new_size,vg_name,lv_name))
            else:
                print("please umount lv else you might loose online work")
        elif choice == '7':
            return
        else:
            print("Bottom")
            print("wrong choice")


        input("Enter to continue..")
        os.system("clear")
#######################################################


########################################################
########################################################
def LVM():
    ostype = input("""
                       	Enter local to work on local operating system
                       	Enter remote to work on remote operating system
                        """)

    if ostype == "local":
        Local_LVM()
    elif ostype == "remote":
        Ip = input("Enter IP address: ")
        username = input("Enter username: ")
        login_type = input("Login using passsword  or key: ")
        if login_type == "password":
            password = getpass.getpass()
            print("Enter password: ")
            RemoteLvm(username,password,Ip)
        elif login_type.lower() == "key":
            key_path = input("Enter key path in this format[path/key]: ")
            CloudRemoteLvm(key_path,username,Ip)
        else:
            print("wrong choice Enter password/key : ")
    else:
        print("wrong choice ")
        return