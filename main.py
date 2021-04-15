"""
Title: Spam Bot
Author: Jackson Reid
Date Created: 2021-04-15
"""

import pyautogui
import time

time.sleep(3)  # This gives you time to swap to the messaging application
f = open("script.txt", 'r')  # Opens the script file
for word in f:
    pyautogui.typewrite(word)  # Prints one line of the file
    pyautogui.press("enter")  # Sends the message
    time.sleep(0.5)
