from cmath import phase
from copy import copy
import sys
import os
import time
import subprocess
import platform
import socket

print("EverTerm Version 1.0.0\n")
print("Build Date: 8/7/2022 13:42\n")
while True:
    cmd = input("$: ")
    if cmd == "help":
        print("EverTerm is still in early stages of development.\nSee dev.md for the phases of development")
        print("help: runs this command\nping: pings a website on the internet\nphasecopy:prints a phrase you type to it\nfilecopy: self explanatory\ndate: lists a date\n filelist:lists files, what did you expect?\nexit: exits terminal")
    if cmd == 'ping':
        host = input("Enter Website To Ping: ")
        number = input("Enter How Many Times To Ping: ")
        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if cmd == "phrasecopy":
        copy = input("Enter phase to copy:")
        print(copy)
    if cmd == "filecopy":
        pass
    if cmd == "date":
        print("The Local Date Is: " + time.strftime("%m/%d/%Y"))
    if cmd == 'filelist':
        file = input("Enter The Direct File Path To Read: ")
        dir_list2 = os.listdir(file)
        print("Files and directories in '", file, "':")
        print(dir_list2)
    if cmd == "exit":
        print("off")
        exit()
    if cmd == "credits":
        print("Icon designed in Pixelorama, go to https://github.com/Orama-Interactive/Pixelorama/ for info")
        print("Inspired by https://github.com/Cyber-Coding-Scripts/Terminal")
        print("WARNING! THIS PROJECT IS STILL IN PHASE 1 DEVELOPMENT")
