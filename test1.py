import time

from test import AW1

CT = (time.localtime()[3]*100) + (time.localtime()[4])
SPlay = AW1()

SPlay.TabQieHuan()
SPlay.InIt()

while True:
    if CT > 1 and CT < 400:
        SPlay.GuaJi()
        time.sleep(14350)
    elif CT > 400 and CT < 710:
        SPlay.GongXunRenWu(9, 120)
        SPlay.JingYingRenWu(9, 160)
        SPlay.ChuangTianGuan(850)
        SPlay.CaiLiaoFuBen()
        SPlay.HuiShou()
        SPlay.GeRenBoss(5)
        SPlay.HuiShou()
        SPlay.ChuMoRenWu()
        SPlay.TaFangFengMo(3)
    elif CT > 710 and CT < 1000:
        SPlay.GuaJi()
        time.sleep(13800)
    elif CT > 1000 and CT < 1015:
        SPlay.RiJinZhuSongLi()
    elif CT > 1015 and CT < 1030:
        SPlay.GuaJi()
        time.sleep(900)
    elif CT > 1030 and CT < 1100:
        SPlay.RiShenWei()
    elif CT > 1100 and CT < 1300:
        SPlay.GuaJi()
        time.sleep(7200)
    elif CT > 1300 and CT < 1330:
        SPlay.RiSuoYaoTa()
    elif CT > 1330 and CT < 1400:
        SPlay.GuaJi()
        time.sleep(1800)
    elif CT > 1400 and CT < 1405:
        SPlay.RiShiMuMiZhen()
    elif CT > 1405 and CT < 1435:
        SPlay.GuaJi()
        time.sleep(1800)
    elif CT > 1435 and CT < 1455:
        SPlay.RiBiGuan()
    elif CT > 1500 and CT < 1600:
        SPlay.RiJiaLanShenDian()
    elif CT > 1600 and CT < 1730:
        SPlay.GuaJi()
        time.sleep(2400)
    elif CT > 1730 and CT < 1800:
        SPlay.RiMoBaiChengZhu()
    elif CT > 1905 and CT < 1930:
        SPlay.RiWorldBoss()
    elif CT > 1930 and CT < 1950:
        SPlay.RiYeZhanBiQi()
    elif CT > 2100 and CT < 2135:
        SPlay.GuaJi()
        time.sleep(2100)
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

