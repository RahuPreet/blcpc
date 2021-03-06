#!/usr/bin/python3
import os
import crypt
import subprocess
import traceback
import sys
os.system("tput setaf 1")
print("\t\t\tWelcome Delhivery IT")
print("\t\t\t--------------------")
os.system("tput setaf 4")


print("""press 1: to install chrome
press 2: to install hplip
press 3: to install Hp printer Driver
press 4: to create user
Press 5: to install adobe reader 
Press 6: to install anydesk
press 7: to install Sapphire IMS
press 8: to install dependencies
press 9: to install update 
press 10: to remove unnecessary file 
press 11: to exit
""")
print("Plese select your option : " , end="")
ch=input()
print(ch)

if int(ch) ==1:
       os.system("sudo apt-get install -y gdebi")
       os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
       os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")
elif int(ch) ==2:
      os.system("sudo apt-get update")
      os.system("sudo apt install hplip-gui -y")
elif int(ch) ==3:
      os.system("sudo hp-setup")
elif int(ch) ==4:
    os.system("useradd -m -s /bin/bash -p $(openssl passwd -1 welcome@123) Delhivery")
    os.system("sudo cp /etc/skel/* /home/Delhivery")
elif int(ch) ==5:
     os.system("sudo apt install gdebi-core libxml2:i386 libcanberra-gtk-module:i386 gtk2-engines-murrine:i386 libatk-adaptor:i386")
     os.system("sudo apt-get update")
     os.system("wget ftp://ftp.adobe.com/pub/adobe/reader/unix/9.x/9.5.5/enu/AdbeRdr9.5.5-1_i386linux_enu.deb")
     os.system("sudo gdebi AdbeRdr9.5.5-1_i386linux_enu.deb")
     os.system("sudo apt update")
elif int(ch) ==6:
    os.system("sudo wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | apt-key add -")
    os.system("echo deb http://deb.anydesk.com/ all main >/etc/apt/sources.list.d/anydesk-stable.list")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install anydesk")
elif int(ch) ==7:
     os.system("sudo apt-get update")
     os.system("sudo apt-get install")
     os.system("sudo apt-get install fping")
     os.system("sudo apt-get install python")
     os.system("wget http://dv.bcan.in/SoftwareRepository/SapphireIMSAgent.zip")
     os.system("unzip SapphireIMSAgent.zip")
     os.system("sh sapphire_agent_install.sh -sudo -install -loc /opt -server dv.bcan.in -port 80 -ssl 0 -username sapphire -password ims") 
elif int(ch) ==8:
    os.system("sudo apt-get install -f")
elif int(ch) ==9:
    os.system("sudo apt-get update")
elif int(ch) ==10:
    os.system("sudo apt-get autoremove")
     

    

    
else: 
       print("does not support")
