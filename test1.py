import time

from test import AW1

CT = (time.localtime()[3]*100) + (time.localtime()[4])
SPlay = AW1()

SPlay.TabQieHuan()
SPlay.InIt()
CurrentLevel = 4
while True:
    if CT > 1 and CT < 1000:
        SPlay.GongXunRenWu(9, 120)
        SPlay.JingYingRenWu(9, 150)
        SPlay.ChuangTianGuan(CurrentLevel)
        SPlay.HuiShou()
        SPlay.CaiLiaoFuBen()
        SPlay.HuiShou()
        SPlay.GeRenBoss(5)
        SPlay.HuiShou()
        SPlay.ChuMoRenWu()
        SPlay.TaFangFengMo(3)
        SPlay.WeiWangRenWu()
        SPlay.LianGong()
        SPlay.GuaJi(10, 0, CurrentLevel)
    elif CT > 1000 and CT < 1030:
        SPlay.RiJinZhuSongLi()
        SPlay.GuaJi(10, 30, CurrentLevel)
    elif CT > 1030 and CT < 1300:
        SPlay.RiShenWei()
        SPlay.GuaJi(13, 0, CurrentLevel)
    elif CT > 1300 and CT < 1400:
        SPlay.RiSuoYaoTa()
        SPlay.GuaJi(14, 0, CurrentLevel)
    elif CT > 1400 and CT < 1435:
        SPlay.RiShiMuMiZhen()
        SPlay.GuaJi(14, 35, CurrentLevel)
    elif CT > 1435 and CT < 1500:
        SPlay.RiBiGuan()
        SPlay.GuaJi(15, 0, CurrentLevel)
    elif CT > 1500 and CT < 1730:
        SPlay.RiJiaLanShenDian()
        SPlay.GuaJi(17, 30, CurrentLevel)
    elif CT > 1730 and CT < 1905:
        SPlay.RiMoBaiChengZhu()
        SPlay.GuaJi(19, 5, CurrentLevel)
    elif CT > 1905 and CT < 1930:
        SPlay.RiWorldBoss()
        SPlay.GuaJi(19, 30, CurrentLevel)
    elif CT > 1930 and CT < 2135:
        SPlay.RiYeZhanBiQi()
        SPlay.GuaJi(21, 35, CurrentLevel)
    elif CT > 2135 and CT < 2200:
        SPlay.RiJinZhuSongLi()
        SPlay.GuaJi(22, 0, CurrentLevel)
    elif CT > 2200 and CT < 2230:
        SPlay.RiShenWei()
        SPlay.GuaJi(22, 30, CurrentLevel)
    elif CT > 2230 and CT < 2300:
        SPlay.RiDuoBeiYaSong()
    else:
        time.sleep(1)
        SPlay.HuiShou()
        SPlay.GuaJi(23, 59, CurrentLevel)
        SPlay.D +=1
        SPlay.HuiShou()