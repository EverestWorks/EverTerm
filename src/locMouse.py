#! python3
# locMouse - a tool that runs on the windows cmd and finds where your mouse is
# for the automateTask.py and writeTask.py
import pyautogui
print("Press CTRL-C to exit")
# Fetch the mouse coordinates
try:
    while True:
        # Find and print the coordinates
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + '    Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print("\nMade for Everest Tools toolkit")
    print("\nExiting...")
