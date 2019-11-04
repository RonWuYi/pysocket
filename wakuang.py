import pyautogui
import time

while True:
    try:
        time.sleep(0.3)
        # pyautogui.doubleClick(802, 909)
        # time.sleep(0.5)
        pyautogui.moveTo(x=1373, y=461)
        time.sleep(0.1)
        pyautogui.click(x=1373, y=461, interval=1)
        time.sleep(0.5)
        pyautogui.typewrite('Hello world!')   
        time.sleep(0.9)
        pyautogui.keyDown('down')
        time.sleep(0.5)
        pyautogui.keyUp('down')
        time.sleep(0.5)
        x,y = pyautogui.position()
        pos="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
        print(pos)
        # time.sleep(2)
    except KeyboardInterrupt:
        print("Done")
        break