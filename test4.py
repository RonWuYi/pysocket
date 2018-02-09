import time
import pyautogui
from datetime import datetime
from NewAllWay import AW
from test import AW1
from test import seconds_change
from test import _boss_hui_shou

CT = ((time.localtime()[3] * 10000) + (time.localtime()[4] * 100) + (time.localtime()[5]))
# print CT
SPlay = AW()
SPlayN = AW1(2)
time.sleep(3)
#
# print datetime.now()
#

print seconds_change(SPlayN._time_diff(23, 59))
# print type(SPlayN.SecondsChange(SPlayN._TimeDiff(19, 5)))
# #

def GuaSuoYaoTa():
    time.sleep(4)
    pyautogui.click(852, 685)

    time.sleep(2)
    pyautogui.click(309, 204)

    # time.sleep(1)
    # pyautogui.doubleClick(852, 685)
    for i in range(7):
        time.sleep(2)
        pyautogui.doubleClick(194, 269)

    _boss_hui_shou()
    # time.sleep(3)
    # pyautogui.doubleClick(854, 164)
    #
    # # time.sleep(2)
    # # pyautogui.doubleClick(636, 731)
    #
    # time.sleep(2)
    # pyautogui.doubleClick(571, 673)
    #
    # time.sleep(2)
    # pyautogui.doubleClick(199, 271)
    #
    # time.sleep(2)
    # pyautogui.doubleClick(792, 596)
    # # 597, 200
    #
    # time.sleep(2)
    # pyautogui.doubleClick(597, 200)

    # time.sleep(2)
    # pyautogui.press('esc')

while True:
    GuaSuoYaoTa()
    time.sleep(1100)




