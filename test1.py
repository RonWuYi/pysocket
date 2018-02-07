import time
from test import AW1

SPlay = AW1(5)
SPlay.TabQieHuan()
SPlay.InIt()

while True:
    print "start a new round at {}, with {} times events complete.".format(SPlay.CurrentDateTime(), SPlay.EventTime)
    CT = ((time.localtime()[3] * 10000) + (time.localtime()[4] * 100) + (time.localtime()[5]))
    if CT > 1 and CT < 100000:
        SPlay.CapturePic(CT)
        SPlay.GongXunRenWu(9, 105)
        SPlay.JingYingRenWu(9, 130)
        SPlay.ChuangTianGuan()
        SPlay.HuiShou()
        SPlay.CaiLiaoFuBen()
        SPlay.HuiShou()
        SPlay.GeRenBoss()
        SPlay.HuiShou()
        SPlay.TaFangFengMo(3)
        SPlay.WeiWangRenWu()
        SPlay.ChuMoRenWu(10)
        SPlay.LianGong(45)
        SPlay.GuaJi(10, 0)
        # pass
    elif CT > 100000 and CT < 103000:
        SPlay.RiJinZhuSongLi()
        SPlay.GuaJi(10, 30)
    elif CT > 103000 and CT < 111000:
        SPlay.RiShenWei(30)
        SPlay.GuaJi(11, 10)
    elif CT > 111000 and CT < 113500:
        SPlay.RiDuoBeiYaSong()
        SPlay.GuaJi(11, 35)
    elif CT > 113500 and CT < 130000:
        SPlay.LianGong(30)
        SPlay.GuaJi(13)
    elif CT > 130000 and CT < 140000:
        SPlay.CapturePic(CT)
        SPlay.RiSuoYaoTa()
        SPlay.GuaJi(14)
    elif CT > 140000 and CT < 143500:
        SPlay.RiShiMuMiZhen()
        SPlay.GuaJi(14, 35)
    elif CT > 143500 and CT < 150000:
        SPlay.RiBiGuan()
        SPlay.GuaJi(15, 0)
    elif CT > 150000 and CT < 173000:
        SPlay.RiGuaiWuGongCheng()
        SPlay.GuaJi(17)
    # elif CT > 150000 and CT < 173000:
    #     SPlay.RiJiaLanShenDian()
    #     SPlay.GuaJi(17, 30)
    elif CT > 173000 and CT < 190000:
        SPlay.RiMoBaiChengZhu()
        SPlay.GuaJi(19)
    elif CT > 190000 and CT < 192000:
        SPlay.RiWorldBoss()
        SPlay.GuaJi(19, 20)
    elif CT > 192000 and CT < 194000:
        # SPlay.CapturePic(CT)
        SPlay.RiDaTi()
        SPlay.GuaJi(19, 40)
    elif CT > 194000 and CT < 200000:
        # SPlay.CapturePic(CT)
        SPlay.RiYeZhanBiQi()
        SPlay.GuaJi(20)
    elif CT > 200000 and CT < 213500:
        # SPlay.CapturePic(CT)
        SPlay.BangHui()
        SPlay.GuaJi(21, 35)
    elif CT > 213500 and CT < 220000:
        SPlay.RiJinZhuSongLi()
        SPlay.GuaJi(22)
    elif CT > 220000 and CT < 223000:
        SPlay.RiShenWei(70)
        SPlay.GuaJi(22, 30)
    elif CT > 223000 and CT < 230000:
        SPlay.RiDuoBeiYaSong()
        SPlay.LinQuHuoYueJiangLi()
        SPlay.GuaJi(23, 30)
    else:
        time.sleep(1)
        SPlay.HuiShou()
        SPlay.GuaJi(23, 59, 59)
        SPlay.D +=1
        SPlay.HuiShou()