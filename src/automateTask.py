#! python3
# automateTask.py - the file that will automate tasks
# you want it to do
import pyautogui
import os
import time
# Declaring the pause and failsafe
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
# Alerting the user that there is a failsafe
print("IMPORTANT! TO EXIT, MOVE YOUR MOUSE TO THE UPPER LEFT-HAND CORNER DURING AUTOMATION WILL CANCEL THE PROGRAM!")
print("\n When automation starts, you will see: Automation is starting!")
# Making the data folder if it isn't present
print("\n\nLoading data...")
os.chdir('C:\\')
os.mkdir('C:\\DATA')
os.chdir('C:\\DATA')
time.sleep(3)
print("\nComplete!")
# Temporary resolution declaration
print("\nYour resolution is:  " + str(pyautogui.size))
# The actual part of the program, where it reads text files
# and converts it into a python file
xData = input("Please enter the path of the x data in C:\\Users\\your_user\\text.txt format:")
yData = input("Please enter the path of the y data in C:\\Users\\your_user\\text.txt format:")
xFile = open(xData)
yFile = open(yData)
