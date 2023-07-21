from copy import copy # the imports
import os
import time
import subprocess
import platform
import shutil
from cmd import Cmd

def winClear(): #this might seem useless but this is just  for upcoming mod support, this is going to be transferred as a module soon
    os.system('cls')

def linxuClear():
    print("\033c", end="")


class cmd(Cmd):

    def do_end(self, args): #new command!
        """ENDS the app"""
        os.system('taskkill /im ' + args)
        print("Done")
    
    def do_kill(self, args): #new command!
        """KILLS the app"""
        os.system('taskkill /f /im ' + args)
        print("Done")

    def do_clear(self, args):
        """it clears the screen, the name says so"""
        if platform.system()=="Windows":
            winClear()
        else: #Linux and Mac clear variant
            linxuClear

    def do_ping(self, args): #pings a website of your choosing
        """Pings a website of your choosing"""
        host = str(args)
        number = 5
        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))

    def do_phasecopy(self, args): # it copies phrases, what do you expect? (works)
        """copies a phase you give it"""
        copy = str(args)
        print(copy)

    def do_filecopy(self, args, args2): # copies file (works)
        """copies files"""
        first = args
        second = args2 #you can make this a file, most preferably a directory
        shutil.copy(first, second)

    def do_summon(self, args): #new command!
        """Launches a file of your choosing"""
        e = str(args)
        os.system(e)
    
    def do_create(self, args): #new command!
        """creates a file"""
        f = str(args)
        with open(f, 'w') as f:
            f.write(' ')

    def do_date(self, args): #lists the date (works)
        """prints the date"""
        print("The date in your area is: " + time.strftime("%m/%d/%Y"))

    def do_filelist(self, args): # lists files, it is in the name. (works)
        """lists file, basically like ls in linux"""
        file = input("Enter The Direct File Path To Read: ")
        dir_list2 = os.listdir(file)
        print("Files and directories in '", file, "':")
        print(dir_list2)

    def do_exit(self, args):# exits terminal (conviently works)
        """exit application"""
        print("logout")
        exit()

    def do_startapp(self, args): # starts an app (works)
        """starts an app, its in the name"""
        app = args
        subprocess.Popen(app) # the aftermath of the app start might be a bit buggy

    def do_credits(self, args): # shows the stuff used and things (works)
        """Credits to all of the github repos and apps i used"""
        print("Icon designed in Pixelorama, go to https://github.com/Orama-Interactive/Pixelorama/ for info")
        print("Inspired by https://github.com/Cyber-Coding-Scripts/Terminal")
        print("This product is a product of EverestWorks, please do not use for malicious intent.")


        print("=====================TERMINAL INFO=====================") #added this section
        print("EverTerm Version 1.1.110 Phase 2\n") 
        print("Build Date: 23/12/2022 19:14\n")



if __name__ == '__main__':
    prompt = cmd()
    if platform.system()=="Windows": # OS Checking
        winClear()
    else: 
        linxuClear()

    
    print("Everterm Build 23948 LabTest02 Interval 5 ")
    print("Public Beta 1")
    print("This build is an experimental build and possibly unstable\nIf you find a bug please report to EverestWorks")
    prompt.prompt = "$: "
    prompt.cmdloop("Booting Up..")