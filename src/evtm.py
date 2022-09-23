from cmath import phase
from copy import copy
import sys
import os
import time
import subprocess
import platform
import socket
import shutil

if platform.system()=="Windows": # OS Checking
    print("OS check sucsessful, running EverTerm")
    subprocess.Popen("cls", shell=True).communicate() 
    time.sleep(0.5)

print("EverTerm Version 1.0.0122 Phase 1\n")
print("Build Date: 22/9/2022 20:13\n")

while True: # Basically the main thing
    cmd = input("$: ")
    if cmd == "clear": #clease screen
        if platform.system()=="Windows":
            subprocess.Popen("cls", shell=True).communicate() 
            
        print("EverTerm Version 1.0.0122 Phase 1\n")
        print("Build Date: 22/9/2022 20:13\n")

    if cmd == "help":
        print("EverTerm is still in early stages of development.\nSee dev.md for the phases of development")
        print("help: runs this command\nping: pings a website on the internet\nphasecopy:prints a phrase you type to it\nfilecopy: self explanatory\ndate: lists a date\n filelist:lists files, what did you expect?\nclear:clears the screen\nexit: exits terminal\n") #sorry about this, im just a little lazy, i will handle this later
        print("be sure to use // in the filecopy command for directories, thanks")

    if cmd == 'ping': #pings a website of your choosing
        host = input("Enter Website To Ping: ")
        number = input("Enter How Many Times To Ping: ")
        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))

    if cmd == "phrasecopy": # it copies phrases, what do you expect?
        copy = input("Enter phase to copy:")
        print(copy)

    if cmd == "filecopy":
        first = input("Please enter your original folder with the file in single quotes:\n")
        second = input("Enter your destination folder:\n") #you can make this a file, most preferably a directory
        shutil.copy(first, second)

    if cmd == "date": #lists the date
        print("The date in your area is: " + time.strftime("%m/%d/%Y"))

    if cmd == 'filelist': # lists files, it is in the name.
        file = input("Enter The Direct File Path To Read: ")
        dir_list2 = os.listdir(file)
        print("Files and directories in '", file, "':")
        print(dir_list2)

    if cmd == "exit":#exits
        print("logout at " + time.strftime("%m/%d/%Y"))
        text = "logout at " + time.strftime("%m/%d/%Y")
        e = open('log.txt', 'w')
        e.write(text)
        e.write('\n')
        exit()

    if cmd == "credits": #credits, what did you expect?
        print("Icon designed in Pixelorama, go to https://github.com/Orama-Interactive/Pixelorama/ for info")
        print("Inspired by https://github.com/Cyber-Coding-Scripts/Terminal")
        print("This product is a product of EverestWorks, please do not use for malicious intent.")
