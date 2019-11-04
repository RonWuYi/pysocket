import os,time
import pyautogui

# flag = True
while True:
    try:
        x,y = pyautogui.position()
        pos="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
        print pos
        time.sleep(2)
        pyautogui.moveTo(x,y)
        pyautogui.click(x, y)

        time.sleep(0.5)
        pyautogui.doubleClick(x, y)
    except KeyboardInterrupt:
        print("Done")
        break
    # x,y = pyautogui.position()
    # pos="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
    # print(pos)
    # time.sleep(2)
    # os.system('cls')
# print 'ending   ....'