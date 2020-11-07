import os

def Local_OS_LVM():
    while True:
        print("WELCOME TO MY LVM MENU")
        print("PRESS 1:DISPLAY HARDISK INFORMATION")
        print("PRESS 2:DISPLAY MOUNT POINTS")
        print("PRESS 3:CREATE PV,CREATE VG,CREATE LV,CREATE FOLDER,MOUNT LV")
        print("PRESS 4:DISPLAY LV/VG/PV")
        print("PRESS 5:EXTEND VG/LV")
        print("PRESS 6:REDUCE LV")
        print("PRESS 7:TO Return ")
        choice = input("ENTER YOUR CHOICE:")
        if choice == '1':
            os.system("fdisk -l")
        if choice == '2':
            os.system("dh -hT")
        elif choice == '3':
                    print("""
                            PRESS 1:CREATE PV
                            PRESS 2:CREATE VG
                            PRESS 3:CREATE LV
                            PRESS 4:MOUNT LV
                            PRESS 5: RETURN
                    """)
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        hd1 = input("ENTER DISK NAME: ")
                        os.system("pvcreate /dev/" + hd1)
                    elif choice == '2':
                        vg_name = input("ENTER VG NAME: ")
                        space_separated_pv_name = input("space separated pv name : ").split()
                        x = " /dev/".join(space_separated_pv_name)
                        os.system("vgcreate " + vg_name + " "+"/dev/{}".format(x))
                    elif choice == '3':
                        lv_name = input("ENTER NAME OF LV:")
                        vg_name = input("ENTER VG NAME: ")
                        size_of_lv = input("ENTER SIZE OF LV:")
                        os.system("lvcreate --size +" + size_of_lv + "G --name " + lv_name + " " + vg_name)

                    elif choice == "5":
                        os.system("mkfs.ext4 /dev/" + vg_name + "/" + lv_name)
                        folder = input("ENTER FOLDER NAME:")
                        os.system("mkdir /" + folder)
                        os.system("mount /dev/" + vg_name + "/" + lv_name + " " + "/" + folder)
                    elif choice == "5":
                        return

        elif choice == '4':
            c = input("ENTER PV/LV/VG: ")
            if c.lower() == "pv":
                os.system("pvdisplay")
            elif c.lower() == "vg":
                os.system("vgdisplay")
            elif c.lower() == "lv":
                os.system("lvdisplay")
        elif choice == '5':
            c = input("ENTER LV/VG: ")
            if c == 'LV':
                size_change = input("ENTER SIZE TO BE INCREASED:")
                vg_name = input("ENTER VG NAME: ")
                lv_name = input("ENTER NAME OF LV:")
                os.system("lvextend --size +" + size_change + "G  /dev/" + vg_name + "/" + lv_name)
                os.system("resize2fs /dev/" + vg_name + "/" + lv_name)
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
                os.system("lvreduce -r -L" + new_size + "G /dev/" + vg_name + "/" + lv_name)
            else:
                print("please umount lv else you might loose online work")
        elif choice == '7':
            return
        else:
            print("wrong choice")
            exit()

        input("Enter to continue..")
        os.system("clear")



