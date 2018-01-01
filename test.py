import time
import pyautogui

CT = (time.localtime()[3] * 100) + (time.localtime()[4])

import time
from NewAllWay import AW

SPlay = AW()

time.sleep(2)
SPlay.TabQieHuan()
SPlay.GeRenBoss()
SPlay.HuiShou()
SPlay.TaFangFengMo()
SPlay.HuiShou()
SPlay.JingYingRenWu()
SPlay.HuiShou()
SPlay.GongXunRenWu()
SPlay.HuiShou()
SPlay.CaiLiaoFuBen()
SPlay.HuiShou()
SPlay.ChuangTianGuan()
SPlay.HuiShou()
while True:
    SPlay.InIt()
    SPlay.GuaJi()
    time.sleep(3600)
    SPlay.HuiShou()
