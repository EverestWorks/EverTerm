# Everest-Tools
A toolset for Windows written in Python! 

Current Stats:

=====================================================

Release Version: Version 1.0

OS Platform: Windows 10

Python Minimum Version: Python 3

=====================================================

The source is for **PYTHON 3+ ONLY** PYTHON 2 is not supported!

======================================

To compile to executable(s):
Requirements:
Windows 10 with Python in the system PATH, 
Brain, 
Hands, 
CMD.exe

======================================

If you do not have the pyinstaller module, install with the command: 
`pip install pyinstaller`

Once pyinstaller is ready, download the source with either
<<<<<<< HEAD
`gh repo clone EverestWorks/Everest` (Alert me if it doesn't work)!
=======
`gh repo clone EverestWorks/Everest-Tools` or `git clone https://github.com/EverestWorks/Everest-Tools.git` (Alert me if it doesn't work)!
>>>>>>> 37e7ac5597a283323aaaabe89e31cc1c172e1d31
Then change your directory to the source
Use the pyinstaller command as: 
`pyinstaller -F -i [icon.ico] [file.py]`
Use py2exe as:
'python setup.py py2exe' in the src directory

For pyinstaller:
Replace [icon.ico] with the icon that matches the file name of [file.py]
Replace [file.py] with the python file you wish to compile

To compile all, run the compileall.bat located in the compile directory, or run the batch file of the python file you want to compile
PYINSTALLER MUST BE INSTALLED

