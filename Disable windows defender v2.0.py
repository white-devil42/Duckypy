import pyautogui
import time
def enter(x, y):
    while y>0:
        pyautogui.hotkey("enter")
        time.sleep(x)
        y=y-1
def tab(x, y):
    while y>0:
        pyautogui.hotkey("tab")
        time.sleep(x)
        y=y-1
def down(x, y):
    while y>0:
        pyautogui.hotkey("down")
        time.sleep(x)
        y=y-1
#enter (time delay after keypress, how many times)
#2 s delay needed to prevent lag
time.sleep(2)
pyautogui.hotkey("ctrl","esc")
time.sleep(0.3)
pyautogui.typewrite("virus & threat protection", interval=0.01)
time.sleep(1)
enter(1, 1)
tab(0.05, 4)
enter(0.05, 1)
tab(0.05, 7)
enter(0.05, 1)
#at exclution page; copy paste and change "exe" to your choice you need
enter(0.05, 1)
down(0.05, 2)
enter(0.05, 1)
pyautogui.typewrite("exe", interval=0.01)
time.sleep(0.3)
tab(0.05, 2)
enter(0.05, 1)
#i needed "vbs" too
enter(0.05, 1)
down(0.05, 2)
enter(0.05, 1)
pyautogui.typewrite("vbs", interval=0.01)
time.sleep(0.3)
tab(0.05, 2)
enter(0.05, 1)
#exiting
pyautogui.hotkey("alt","f4")
