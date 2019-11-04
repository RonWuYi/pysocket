import pyautogui, sys
import time

while True:
    try:
        time.sleep(0.5)
        pyautogui.moveTo(x=936, y=-142)
        time.sleep(0.5)
        pyautogui.press('down')
        time.sleep(0.5)
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')
    except KeyboardInterrupt:
        print("Done")
        break
# pyautogui.click()
# time.sleep(0.5)