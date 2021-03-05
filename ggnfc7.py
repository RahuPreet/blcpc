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
print("\t\t\tCreated By Rahul Gupta")
os.system("tput setaf 12")


print("""press 1: to install anydesk
Press 2: to exit
""")

print("Plese select your option : " , end="")
ch=input()
print(ch)

if int(ch) ==1:
    os.system("!{sys.executable} -m pip install anydesk")
    os.system("sudo wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | apt-key add -")
    os.system("echo deb http://deb.anydesk.com/ all main >/etc/apt/sources.list.d/anydesk-stable.list")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install anydesk")
    
else: 
      print("does not support")
