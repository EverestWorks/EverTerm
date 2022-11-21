from copy import copy
import sys
import os
import time
import subprocess
import platform
import socket
import shutil
from datetime import datetime
import keyboard
from art import *


if __name__ == "__main__":     #  Added this little thing just for the modding, this wont work if this python file is imported into your mod, see modding documentation
    if platform.system()=="Windows": # OS Checking
        print("OS check sucsessful, running EverTerm")
        subprocess.Popen("cls", shell=True).communicate() 
        time.sleep(0.5)
    else: 
        print("WARN: Linux and Mac support is in beta")
        print("Please use at your own risk")
        time.sleep(2)
        print("\033c", end="")

    tprint("EverTerm") # shorten this thing and remove the build date from here



    while True: # the main thing
        cmd = input("$: ")
        if cmd == "clear": #clears screen (works)
            if platform.system()=="Windows":
                subprocess.Popen("cls", shell=True).communicate()
            else: #Linux and Mac clear variant
                print("\033c", end="") 
        if cmd == "help": # (works)
            print("EverTerm is still in early stages of development. See dev.md for the phases of development\n")
            print("help: runs this command\nping: pings a website on the internet\nphasecopy:prints a phrase you type to it\nfilecopy: self explanatory\ndate: lists a date\nfilelist:lists files, what did you expect?\nclear:clears the screen\nexit: exits terminal\n") #sorry about this, im just a little lazy, i will handle this later
            print("be sure to use / in the filecopy command for directories, WINDOWS ONLY")
            print("\nLinux users! please use your normal path! thanks!")

        if cmd == 'ping': #pings a website of your choosing (works)
            host = input("Enter Website To Ping: ")
            number = input("Enter How Many Times To Ping: ")
            def ping(host):
                param = '-n' if platform.system().lower() == 'windows' else '-c'
                command = ['ping', param, number, host]
                return subprocess.call(command)
            print(ping(host))

        if cmd == "phrasecopy": # it copies phrases, what do you expect? (works)
            copy = input("Enter phase to copy:")
            print(copy)

        if cmd == "filecopy": # copies file (works)
            first = input("Please enter your original folder with the file in single quotes:\n")
            second = input("Enter your destination folder:\n") #you can make this a file, most preferably a directory
            shutil.copy(first, second)

        if cmd == "date": #lists the date (works)
            print("The date in your area is: " + time.strftime("%m/%d/%Y"))

        if cmd == 'filelist': # lists files, it is in the name. (works)
            file = input("Enter The Direct File Path To Read: ")
            dir_list2 = os.listdir(file)
            print("Files and directories in '", file, "':")
            print(dir_list2)

        if cmd == "exit":# exits terminal (works)
            var = "This is just a placeholder, just wait"
            text = str(var)
            print("logout at " + text)
            e = open('log.txt', 'w')
            e.write(text)
            e.write('\n')
            exit()
        if cmd == "startapp": # starts an app (works)
            print("WARN: windows users use a / instead of regular slash!\n ")
            app = input("Enter the FULL path of the app:\n")
            subprocess.Popen(app)

        if cmd == "credits": # shows the stuff used and things (works)
            print("Icon designed in Pixelorama, go to https://github.com/Orama-Interactive/Pixelorama/ for info")
            print("Inspired by https://github.com/Cyber-Coding-Scripts/Terminal")
            print("This product is a product of EverestWorks, please do not use for malicious intent.")
            

            print("==============TERMINAL INFO=====================")
            print("EverTerm Version 1.1.233 Phase 1\n")
            print("Build Date: 24/11/2022 20:13\n")

    
    



else:
    print("ERROR-99-11-19a: This is stated by the compiler as module, this is main file.\n Report this error to the github page at https://github.com/EverestWorks/EverTerm!")