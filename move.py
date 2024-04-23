import pyautogui
import time
import random
import tkinter as tk
import os

root = tk.Tk()
os.environ["TK_SILENCE_DEPRECATION"] = "1"
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

while True:
    x = random.randint(0,screen_width)
    y = random.randint(0,screen_height)
    pyautogui.moveTo(x,y)

    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    # print('moved to '+str(result) + '('+ str(x) + ','+ str(y) + ')')
    
    #Mouse will move every 5 seconds
    time.sleep(5) 