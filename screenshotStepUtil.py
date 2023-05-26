from tkinter.constants import E
import pyautogui
def frameStep():
    pyautogui.keyDown("n")
    pyautogui.keyUp("n")
def screenshot():
    pyautogui.keyDown("f5")
    pyautogui.keyUp("f5")

pyautogui.PAUSE = 0.1
waitTime = 0.20
print("setup complete")
pyautogui.sleep(3)
print("starting")
for i in range(30):
    screenshot()
    pyautogui.sleep(waitTime)
    frameStep()
    pyautogui.sleep(waitTime)