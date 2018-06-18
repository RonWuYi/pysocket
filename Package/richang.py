import time

from Package.basic import BASIC
from Package.util import go_gua_ji_npc, xiao_chu_jie_mian, customize_init

class BASICFUNCTIONRC(BASIC):

    def __init__(self):
        super(BASICFUNCTIONRC, self).__init__()
        self.open()
        self.function()
        self.clean()
        self.close()

    def function(self):
        pass

    def open(self):
        pass

    def close(self):
        pass

    def clean(self):
        pass


class YAOTA(BASIC):
    def __init__(self, da_time):
        self.da_time = da_time
        super(YAOTA, self).__init__()
    # To Do
    def gua_suo_yao_ta(self):
        go_gua_ji_npc()
        xiao_chu_jie_mian()

        time.sleep(1)
        pyautogui.click(654, 390)

        if self.zhuan_shen_level == 0:
            time.sleep(1)
            pyautogui.click(515, 397)
        elif 0 < self.zhuan_shen_level <= 2:
            time.sleep(1)
            pyautogui.click(515, 426)
        elif 2 < self.zhuan_shen_level <= 4:
            time.sleep(1)
            pyautogui.click(515, 453)
        elif 4 < self.zhuan_shen_level <= 6:
            time.sleep(1)
            pyautogui.click(515, 483)
        elif 6 < self.zhuan_shen_level <= 8:
            time.sleep(1)
            pyautogui.click(515, 511)
        else:
            time.sleep(1)
            pyautogui.click(515, 539)
        while True:
            xiao_chu_jie_mian()
            time.sleep(0.5)
            pyautogui.press('z')
            time.sleep(600)
            pyautogui.click(854, 684)
            time.sleep(1)
            pyautogui.click(310, 204)
            time.sleep(1)
            for i in range(8):
                time.sleep(2)
                pyautogui.doubleClick(197, 271)
                time.sleep(0.5)
            pyautogui.press('esc')
            xiao_chu_jie_mian()
            time.sleep(360000)

    def da_suo_yao_ta(self):
        go_gua_ji_npc()
        xiao_chu_jie_mian()

        time.sleep(1)
        pyautogui.click(654, 390)

        if self.zhuan_shen_level == 0:
            time.sleep(1)
            pyautogui.click(515, 397)
        elif 0 < self.zhuan_shen_level <= 2:
            time.sleep(1)
            pyautogui.click(515, 426)
        elif 2 < self.zhuan_shen_level <= 4:
            time.sleep(1)
            pyautogui.click(515, 453)
        elif 4 < self.zhuan_shen_level <= 6:
            time.sleep(1)
            pyautogui.click(515, 483)
        elif 6 < self.zhuan_shen_level <= 8:
            time.sleep(1)
            pyautogui.click(515, 511)
        else:
            time.sleep(1)
            pyautogui.click(515, 539)

        xiao_chu_jie_mian()
        pyautogui.press('z')
        time.sleep(self.Seconds*self.da_time)
        customize_init()