from copy import copy
import os
import time
import subprocess
import platform
import socket
import shutil
from datetime import datetime
import keyboard
from cmd import Cmd

class cmd(Cmd):

 while True: # the main thing

        def do_clear(self, args):
            """it clears the screen, the name says so"""
            if platform.system()=="Windows":
                subprocess.Popen("cls", shell=True).communicate()
            else: #Linux and Mac clear variant
                print("\033c", end="") 

        def do_ping(self, args, args2): #pings a website of your choosing (works)
            """Pings a website of your choosing"""
            host = args
            number = args2
            def ping(host):
                param = '-n' if platform.system().lower() == 'windows' else '-c'
                command = ['ping', param, number, host]
                return subprocess.call(command)
            print(ping(host))

        def do_phasecopy(self, args): # it copies phrases, what do you expect? (works)
            """copies a command you give it"""
            copy = str(args)
            print(copy)

        def do_filecopy(self, args, args2): # copies file (works)
            """copies files"""
            first = args
            second = args2 #you can make this a file, most preferably a directory
            shutil.copy(first, second)

        def do_date(self, args): #lists the date (works)
            """prints the date"""
            print("The date in your area is: " + time.strftime("%m/%d/%Y"))

        def do_filelist(self, args): # lists files, it is in the name. (works)
            """lists file, basically like ls in linux"""
            file = input("Enter The Direct File Path To Read: ")
            dir_list2 = os.listdir(file)
            print("Files and directories in '", file, "':")
            print(dir_list2)

        def do_exit(self, args):# exits terminal (works)
            """exit"""
            print("logout")
            exit()

        def do_startapp(self, args): # starts an app (works)
            """starts an app, its in the name"""
            app = args
            subprocess.Popen(app) #the aftermath of the app start is a bit buggy

        def do_credits(self, args): # shows the stuff used and things (works)
            print("Icon designed in Pixelorama, go to https://github.com/Orama-Interactive/Pixelorama/ for info")
            print("Inspired by https://github.com/Cyber-Coding-Scripts/Terminal")
            print("This product is a product of EverestWorks, please do not use for malicious intent.")
            

            print("==============TERMINAL INFO=====================") #added this section
            print("EverTerm Version 1.1.110 Phase 2\n") 
            print("Build Date: 23/12/2022 19:14\n")



if __name__ == '__main__':
    prompt = cmd()
    prompt.cmdloop('Booting up...')
    if platform.system()=="Windows": # OS Checking
        print("OS check sucsessful, running EverTerm") 
        os.system('cls')
        time.sleep(0.5)
    else: 
        print("WARN: Linux support is in beta")
        print("Please use at your own risk")
        time.sleep(2)
        print("\033c", end="")
    
    print("Everterm Build 21994")
    print("This build is an experimental build and possibly unstable\n if you find a bug please report to EverestWorks")
    prompt.prompt = '$: '