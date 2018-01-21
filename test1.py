import time

from test import AW1

CT = (time.localtime()[3]*100) + (time.localtime()[4])
SPlay = AW1()

SPlay.TabQieHuan()
SPlay.InIt()

while True:
    if CT > 1 and CT < 930:
        SPlay.GongXunRenWu(9, 120)
        SPlay.JingYingRenWu(9, 160)
        SPlay.ChuangTianGuan(850)
        SPlay.CaiLiaoFuBen()
        SPlay.HuiShou()
        SPlay.GeRenBoss(5)
        SPlay.HuiShou()
        SPlay.ChuMoRenWu()
        SPlay.TaFangFengMo(3)
    elif CT > 1630 and CT < 1730:
        SPlay.GuaJi()
        time.sleep(2400)
    elif CT > 1730 and CT < 1800:
        SPlay.RiMoBaiChengZhu()
    elif CT > 1905 and CT < 1930:
        SPlay.RiWorldBoss()
    elif CT > 1930 and CT < 1950:
        SPlay.RiYeZhanBiQi()
    elif CT > 2100 and CT < 2135:
        SPlay.TaFangFengMo(1)
    elif CT > 2135 and CT < 2150:
        SPlay.RiJinZhuSongLi()
    elif CT > 2200 and CT < 2230:
        SPlay.RiShenWei()
    elif CT > 2230 and CT < 2300:
        SPlay.RiDuoBeiYaSong()
    else:
        time.sleep(1)
        SPlay.GuaJi()
        time.sleep(1200)
        SPlay.HuiShouLess()

