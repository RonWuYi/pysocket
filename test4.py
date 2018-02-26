import time
import pyautogui
from NewAllWay import AW
from test import AW1
from test import _boss_hui_shou

CT = ((time.localtime()[3] * 10000) + (time.localtime()[4] * 100) + (time.localtime()[5]))

SPlay = AW()
SPlayN = AW1(2)
time.sleep(5)


def gua_suo_yao_ta():
    time.sleep(4)
    pyautogui.click(852, 685)

    time.sleep(2)
    pyautogui.click(309, 204)

    for i in range(7):
        time.sleep(2)
        pyautogui.doubleClick(194, 269)

    _boss_hui_shou()

while True:
    gua_suo_yao_ta()
    time.sleep(1100)
