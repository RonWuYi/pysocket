import time

from test import AW1

SPlay = AW1(4)
SPlay.TabQieHuan()
SPlay.InIt()

while True:
    print "start a round at {}".format(SPlay.CurrentDateTime())
    CT = ((time.localtime()[3] * 10000) + (time.localtime()[4] * 100) + (time.localtime()[5]))
    # if CT > 1 and CT < 1000:
    #     SPlay.GongXunRenWu(9, 120)
    #     SPlay.JingYingRenWu(9, 150)
    #     SPlay.ChuangTianGuan()
    #     SPlay.HuiShou()
    #     SPlay.CaiLiaoFuBen()
    #     SPlay.HuiShou()
    #     SPlay.GeRenBoss()
    #     SPlay.HuiShou()
    #     SPlay.TaFangFengMo(3)
    #     SPlay.WeiWangRenWu()
    #     SPlay.ChuMoRenWu(120)
    #     SPlay.LianGong(120)
    #     SPlay.GuaJi(10, 0)
    if CT > 1 and CT < 100000:
        SPlay.CapturePic(CT)
        SPlay.GongXunRenWu(9, 110)
        SPlay.JingYingRenWu(9, 140)
        SPlay.ChuangTianGuan()
        SPlay.HuiShou()
        SPlay.CaiLiaoFuBen()
        SPlay.HuiShou()
        SPlay.GeRenBoss()
        SPlay.HuiShou()
        SPlay.TaFangFengMo(3)
        SPlay.WeiWangRenWu()
        SPlay.ChuMoRenWu(120)
        SPlay.LianGong(120)
        SPlay.GuaJi(10, 0)
    elif CT > 100000 and CT < 103000:
        SPlay.RiJinZhuSongLi()
        SPlay.GuaJi(10, 30)
    elif CT > 103000 and CT < 130000:
        SPlay.RiShenWei(60)
        SPlay.GuaJi(13, 0)
    elif CT > 130000 and CT < 140000:
        SPlay.CapturePic(CT)
        SPlay.RiSuoYaoTa()
        SPlay.GuaJi(14, 0)
    elif CT > 140000 and CT < 143500:
        SPlay.RiShiMuMiZhen()
        SPlay.GuaJi(14, 35)
    elif CT > 143500 and CT < 150000:
        SPlay.RiBiGuan()
        SPlay.GuaJi(15, 0)
    elif CT > 150000 and CT < 173000:
        SPlay.RiJiaLanShenDian()
        SPlay.GuaJi(17, 30)
    elif CT > 173000 and CT < 190500:
        SPlay.RiMoBaiChengZhu()
        SPlay.GuaJi(19, 5)
    elif CT > 190500 and CT < 193000:
        SPlay.RiWorldBoss()
        SPlay.GuaJi(19, 30)
    elif CT > 193000 and CT < 213500:
        SPlay.CapturePic(CT)
        SPlay.RiYeZhanBiQi()
        SPlay.GuaJi(21, 35)
    elif CT > 213500 and CT < 220000:
        SPlay.RiJinZhuSongLi()
        SPlay.GuaJi(22, 0)
    elif CT > 220000 and CT < 223000:
        SPlay.RiShenWei(70)
        SPlay.GuaJi(22, 30)
    elif CT > 223000 and CT < 230000:
        SPlay.RiDuoBeiYaSong()
        SPlay.HuoYueJiang()
        SPlay.GuaJi(23, 30)
    else:
        time.sleep(1)
        SPlay.HuiShou()
        SPlay.GuaJi(23, 59, 59)
        SPlay.D +=1
        SPlay.HuiShou()