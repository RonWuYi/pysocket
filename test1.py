import time

from test import AW1


SPlay = AW1(3)
SPlay.TabQieHuan()
SPlay.InIt()

while True:
    print "start a round at {}".format(SPlay.CurrentDateTime())
    CT = (time.localtime()[3] * 100) + (time.localtime()[4])
    if CT > 1 and CT < 1000:
        # SPlay.GongXunRenWu(9, 120)
        # SPlay.JingYingRenWu(3, 150)
        # SPlay.ChuangTianGuan()
        # SPlay.HuiShou()
        # SPlay.CaiLiaoFuBen()
        # SPlay.HuiShou()
        # SPlay.GeRenBoss()
        # SPlay.HuiShou()
        SPlay.TaFangFengMo(1)
        SPlay.WeiWangRenWu()
        SPlay.ChuMoRenWu(60)
        SPlay.LianGong(120)
        SPlay.GuaJi(10, 0)
    elif CT > 1000 and CT < 1030:
        SPlay.RiJinZhuSongLi()
        SPlay.GuaJi(10, 30)
    elif CT > 1030 and CT < 1300:
        SPlay.RiShenWei()
        SPlay.GuaJi(13, 0)
    elif CT > 1300 and CT < 1400:
        SPlay.RiSuoYaoTa()
        SPlay.GuaJi(14, 0)
    elif CT > 1400 and CT < 1435:
        SPlay.RiShiMuMiZhen()
        SPlay.GuaJi(14, 35)
    elif CT > 1435 and CT < 1500:
        SPlay.RiBiGuan()
        SPlay.GuaJi(15, 0)
    elif CT > 1500 and CT < 1730:
        SPlay.RiJiaLanShenDian()
        SPlay.GuaJi(17, 30)
    elif CT > 1730 and CT < 1905:
        SPlay.RiMoBaiChengZhu()
        SPlay.GuaJi(19, 5)
    elif CT > 1905 and CT < 1930:
        SPlay.RiWorldBoss()
        SPlay.GuaJi(19, 30)
    elif CT > 1930 and CT < 2135:
        SPlay.RiYeZhanBiQi()
        SPlay.GuaJi(21, 35)
    elif CT > 2135 and CT < 2200:
        SPlay.RiJinZhuSongLi()
        SPlay.GuaJi(22, 0)
    elif CT > 2200 and CT < 2230:
        SPlay.RiShenWei()
        SPlay.GuaJi(22, 30)
    elif CT > 2230 and CT < 2300:
        SPlay.RiDuoBeiYaSong()
    else:
        time.sleep(1)
        SPlay.HuiShou()
        SPlay.GuaJi(23, 59, 59)
        SPlay.D +=1
        SPlay.HuiShou()