import os
import time
import subprocess
import platform
import shutil
from cmd import Cmd
import importlib
import logging

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    filename=os.path.join(script_dir, "app.log"),  # Use os.path.join to construct the log file path
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define a logger
logger = logging.getLogger('app')

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

class MyCmd(Cmd):
    def __init__(self):
        super().__init__()

        # Load user-defined commands from mods
        self.user_defined_commands = {}
        self.load_mods()

    def load_mods(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        mods_dir = os.path.join(script_dir, "mods")

        logger.debug(f"Mods directory: {mods_dir}")

        if not os.path.exists(mods_dir):
            os.makedirs(mods_dir)

        for mod_file in os.listdir(mods_dir):
            if mod_file.endswith(".py"):
                mod_name = mod_file[:-3]
                try:
                    user_commands = importlib.import_module(f"mods.{mod_name}")
                    commands_added = {
                        name: func for name, func in user_commands.__dict__.items()
                        if callable(func) and not name.startswith("__")
                    }
                    self.user_defined_commands.update(commands_added)
                    logger.debug(f"{mod_name} loaded successfully. Custom commands: {commands_added}")
                except ImportError:
                    logger.debug(f"Failed to load {mod_file}. Please check the syntax and content of the mod file.")


    def do_command(self, line):
        """Handles the processing of user commands."""
        print(f"Received command: '{line}'")
        print(f"User-defined commands: {self.user_defined_commands}")
        print(f"Registered commands: {self.get_names()}")

        # Check for custom commands from loaded mods
        for command_name, command_func in self.user_defined_commands.items():
            print(f"Checking custom command: {command_name}")
            if line.startswith(command_name):
                args = line[len(command_name):].strip()
                print(f"Custom command args: {args}")
                command_func(args)
                return

        # Handle commands from the base class (Cmd)
        try:
            super().onecmd(line)
        except Exception as e:
            print(f"Error: {e}")

    def default(self, line):
        # Handle mod management commands
        if line.startswith("mod "):
            self.handle_mod_command(line[4:])
        else:
            # Handle user-defined commands
            command, *args = line.split()
            if command in self.user_defined_commands:
                self.user_defined_commands[command](" ".join(args))
            else:
                print("Command not found.")

    def handle_mod_command(self, line):
        commands = line.split()

        if len(commands) < 1:
            print("Usage: mod <list/load/unload> [mod_name]")
            return

        cmd = commands[0].lower()

        if cmd == 'list':
            """list available mods"""
            self.list_mods()
        elif cmd == 'load':
            """load the mod you want"""
            if len(commands) < 2:
                print("Usage: mod load <mod_name>")
                return
            self.load_mod(commands[1])
        elif cmd == 'unload':
            """unload the mod you want"""
            if len(commands) < 2:
                print("Usage: mod unload <mod_name>")
                return
            self.unload_mod(commands[1])
        else:
            print("Invalid command. Usage: mod <list/load/unload> [mod_name]")

    def list_mods(self):
        """List currently loaded mods."""
        print("Loaded Mods:")
        for mod_name in self.user_defined_commands:
            print(f"- {mod_name}")

    def load_mod(self, mod_name):
        """Load a specific mod."""
        try:
            importlib.import_module(f"mods.{mod_name}")
            print(f"{mod_name} loaded successfully.")
        except ImportError:
            print(f"Failed to load {mod_name}. Please check the syntax and content of the mod file.")

    def unload_mod(self, mod_name):
        """Unload a specific mod."""
        if mod_name in self.user_defined_commands:
            del self.user_defined_commands[mod_name]
            print(f"{mod_name} unloaded successfully.")
        else:
            print(f"{mod_name} is not loaded.")
#
#
# Separating mods part from the main thing
#
#

    def do_end(self, args):
        """asks politely for the app to die. USAGE: end [APP]"""
        if not args:
            print("Usage: end <APP>")
            return

        if platform.system() == "Windows":
            os.system('taskkill /im ' + args)
        else:
            os.system('pkill ' + args)

        print(args + " has been ended")

    def do_kill(self, args):
        """Murders the app in the middle of whatever it is doing. USAGE: kill [app]"""
        if not args:
            print("Usage: kill <APP>")
            return

        if platform.system() == "Windows":
            os.system('taskkill /f /im ' + args)
        else:
            os.system('pkill -9 ' + args)

        print(args + " has been killed")


    def do_clear(self):
        """Clears the screen"""
        clear_screen()

    def do_ping(self, args):
        """Pings a website of your choosing. USAGE: ping [-c] <website>"""
        args = args.split()  # Split the arguments into a list

        if args[0] == "-c":
            if len(args) != 3:
                print("Usage: ping -c <count> <host>")
                return

            count = args[1]
            host = args[2]
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, str(count), host]
            subprocess.call(command)
        else:
            host = args[0]
            number = 4
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, str(number), host]
            subprocess.call(command)


    def do_echo(self, args):
        """Copies a phrase you give it"""
        copy = args
        print(copy)

    def do_copy(self, args):
        """Copies files and directories. Usage: copy [-d] <source> <destination>"""
        args = args.split()

        if len(args) < 2:
            print("Usage: copy [-d] <source> <destination>")
            return

        if args[0] == "-d":
            # Copy directory contents
            source_dir = args[1]
            destination_dir = args[2]

            if not os.path.exists(source_dir):
                print("Source directory does not exist.")
                return

            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            try:
                for item in os.listdir(source_dir):
                    source_item = os.path.join(source_dir, item)
                    if os.path.isfile(source_item):
                        shutil.copy(source_item, destination_dir)
                    elif os.path.isdir(source_item):
                        destination_item = os.path.join(destination_dir, item)
                        shutil.copytree(source_item, destination_item)
                print("Directory contents copied successfully.")
            except Exception as e:
                print("Error copying directory contents:", str(e))
        else:
            # Copy file
            source_file = args[0]
            destination_dir = args[1]

            if not os.path.exists(source_file):
                print("Source file does not exist.")
                return

            if not os.path.isdir(destination_dir):
                print("Destination directory is not valid.")
                return

            try:
                shutil.copy(source_file, destination_dir)
                print("File copied successfully.")
            except Exception as e:
                print("Error copying file:", str(e))


    def do_summon(self, args):
        """Launches a file of your choosing"""
        e = args
        os.system(e)

    def do_create(self, args):
        """Creates a file"""
        if len(args) != 2:
            print("Usage: create <filename.extension>")
        else:
            f = args
            with open(f, 'w') as f:
                f.write(' ')


    def do_date(self):
        """Prints the date"""
        print("The date in your area is:", time.strftime("%m/%d/%Y"))

    def do_filelist(self, args):
        """Lists files and directories in a given path"""
        if len(args) != 2:
            print("Usage: filelist <full/path/of/directory>")
        else:
            file_path = args
            dir_list = os.listdir(file_path)
            print("Files and directories in '", file_path, "':")
            print(dir_list)


    def do_exit(self):
        """Exit application"""
        print("logout")
        return True  # Returning True will exit the cmd loop

    def do_startapp(self, args):
        """Starts an app"""
        if len(args) != 2:
            print("Usage: startapp <appname>")
        else:
            app = args
            subprocess.Popen(app)  # unfortunatly, your getting the apps cmd outputs in the terminal
    
    def do_docs(self, args):
        """Basically help but more detailed"""
        if len(args) != 2:
            print("Usage: docs [COMMAND]")
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            docs_dir = os.path.join(script_dir, "help.ex")

            logger.debug(f"docs database directory: {docs_dir}")

            if not os.path.exists(docs_dir):
                os.makedirs(docs_dir)

            os.chdir(docs_dir)
            f = "docs.txt"
            with open(f, 'w') as f:
                # f.write(' ')
                pass

    def do_credits(self):
        """Credits to all the repos and apps used to make this product that deserve credits"""
        print("Icon designed in Pixelorama, go to https://github.com/Orama-Interactive/Pixelorama/ for info")
        print("Inspired by https://github.com/Cyber-Coding-Scripts/Terminal")
        print("This product is a product of EverestWorks, please do not use for malicious intent.")
        print("=====================TERMINAL INFO=====================")
        print("EverTerm v1.0.420 LabTest01 Interval 2\n")
        print("Build Date: 24/8/2023 19:42\n")

if __name__ == '__main__':
    prompt = MyCmd()
    clear_screen()
    print("EverTerm v1.0.420 LabTest02 Interval 1 ")
    print("This build is an experimental build and possibly unstable")
    print("If you find a bug please report to EverestWorks")
    print("Logs can be found in the directory the executable is located in, under the name app.log")
    prompt.prompt = "$: "
    prompt.cmdloop("Starting Up..")