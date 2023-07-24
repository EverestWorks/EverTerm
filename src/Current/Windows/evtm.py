import os
import time
import subprocess
import platform
import shutil
from cmd import Cmd

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

class MyCmd(Cmd):
    def __init__(self):
        super().__init__()
        self.user_defined_commands = self.load_user_commands()

    def load_user_commands(self):
        try:
            import user_commands
            return {
                name: func for name, func in user_commands.__dict__.items()
                if callable(func) and not name.startswith("__")
            }
        except ImportError:
            return {}

    def default(self, line):
        # Handle user-defined commands
        command, *args = line.split()
        if command in self.user_defined_commands:
            self.user_defined_commands[command](" ".join(args))
        else:
            print("Command not found.")

    def do_end(self, args):
        """ENDS the app"""
        if platform.system() == "Windows":
            os.system('taskkill /im ' + args)
        else:
            os.system('pkill ' + args)
        print("Done")

    def do_kill(self, args):
        """KILLS the app"""
        if platform.system() == "Windows":
            os.system('taskkill /f /im ' + args)
        else:
            os.system('pkill -9 ' + args)
        print("Done")

    def do_clear(self, args):
        """Clears the screen"""
        clear_screen()

    def do_ping(self, args):
        """Pings a website of your choosing"""
        host = args
        number = 4
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, str(number), host]
        subprocess.call(command)

    def do_phasecopy(self, args):
        """Copies a phrase you give it"""
        copy = args
        print(copy)

    def do_filecopy(self, args):
        """Copies files"""
        args = args.split()
        if len(args) != 2:
            print("Usage: filecopy <source_file> <destination_directory>")
        else:
            first, second = args
            shutil.copy(first, second)

    def do_summon(self, args):
        """Launches a file of your choosing"""
        e = args
        os.system(e)

    def do_create(self, args):
        """Creates a file"""
        f = args
        with open(f, 'w') as f:
            f.write(' ')

    def do_date(self, args):
        """Prints the date"""
        print("The date in your area is:", time.strftime("%m/%d/%Y"))

    def do_filelist(self, args):
        """Lists files and directories in a given path"""
        file_path = input("Enter The Direct File Path To Read: ")
        dir_list = os.listdir(file_path)
        print("Files and directories in '", file_path, "':")
        print(dir_list)

    def do_exit(self, args):
        """Exit application"""
        print("logout")
        return True  # Returning True will exit the cmd loop

    def do_startapp(self, args):
        """Starts an app"""
        app = args
        subprocess.Popen(app)  # The aftermath of the app start might be a bit buggy

    def do_credits(self, args):
        """Credits to all the GitHub repos and apps used"""
        print("Icon designed in Pixelorama, go to https://github.com/Orama-Interactive/Pixelorama/ for info")
        print("Inspired by https://github.com/Cyber-Coding-Scripts/Terminal")
        print("This product is a product of EverestWorks, please do not use for malicious intent.")
        print("=====================TERMINAL INFO=====================")
        print("EverTerm Build 23948 LabTest02 Interval 5\n")
        print("Build Date: 21/7/2023 12:59\n")

if __name__ == '__main__':
    prompt = MyCmd()
    clear_screen()
    print("Everterm Build 23948 LabTest02 Interval 5 ")
    print("Public Beta 1")
    print("This build is an experimental build and possibly unstable")
    print("If you find a bug please report to EverestWorks")
    prompt.prompt = "$: "
    prompt.cmdloop("Booting Up..")
