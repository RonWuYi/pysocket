import time
from test import AW1

SPlay = AW1(5)
SPlay.tab_qie_huan()
SPlay.InIt()

while True:
    print "start a new round at {}, with {} times events complete.".format(SPlay.CurrentDateTime(), SPlay.EventTime)
    CT = ((time.localtime()[3] * 10000) + (time.localtime()[4] * 100) + (time.localtime()[5]))
    # if CT > 1 and CT < 100000:

    if 1 < CT < 100000:
        SPlay.CapturePic(CT)
        SPlay.gong_xun_ren_wu(9, 105)
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
    # elif CT > 100000 and CT < 103000:

    elif 100000 < CT < 103000:
        SPlay.RiJinZhuSongLi()
        SPlay.GuaJi(10, 30)
    # elif CT > 103000 and CT < 111000:

    elif 103000 < CT < 111000:

        SPlay.RiShenWei(30)
        SPlay.GuaJi(11, 10)
    # elif CT > 111000 and CT < 113500:

    elif 111000 < CT < 113500:
        SPlay.RiDuoBeiYaSong()
        SPlay.GuaJi(11, 35)
    # elif CT > 113500 and CT < 130000:

    elif 113500 < CT < 130000:
        SPlay.LianGong(30)
        SPlay.GuaJi(13)
    # elif CT > 130000 and CT < 140000:

    elif 130000 < CT < 140000:
        SPlay.CapturePic(CT)
        SPlay.RiSuoYaoTa()
        SPlay.GuaJi(14)
    # elif CT > 140000 and CT < 143500:

    elif 140000 < CT < 143500:
        SPlay.RiShiMuMiZhen()
        SPlay.GuaJi(14, 35)
    # elif CT > 143500 and CT < 150000:

    elif 143500 < CT < 150000:
        SPlay.RiBiGuan()
        SPlay.GuaJi(15, 0)
    # elif CT > 150000 and CT < 173000:

    elif 150000 < CT < 173000:
        SPlay.RiGuaiWuGongCheng()
        SPlay.GuaJi(17)
    # elif CT > 150000 and CT < 173000:
    #     SPlay.RiJiaLanShenDian()
    #     SPlay.GuaJi(17, 30)
    # elif CT > 173000 and CT < 190000:

    elif 173000 < CT < 190000:
        SPlay.RiMoBaiChengZhu()
        SPlay.GuaJi(19)
    # elif CT > 190000 and CT < 192000:

    elif 190000 < CT < 192000:

        SPlay.RiWorldBoss()
        SPlay.GuaJi(19, 20)
    # elif CT > 192000 and CT < 194000:

    elif 192000 < CT < 194000:
        # SPlay.CapturePic(CT)
        SPlay.RiDaTi()
        SPlay.GuaJi(19, 40)
    # elif CT > 194000 and CT < 200000:
    elif 194000 < CT < 200000:
        # SPlay.CapturePic(CT)
        SPlay.RiYeZhanBiQi()
        SPlay.GuaJi(20)
    # elif CT > 200000 and CT < 213500:
    elif 200000 < CT < 213500:
        # SPlay.CapturePic(CT)
        SPlay.BangHui()
        SPlay.GuaJi(21, 35)
    # elif CT > 213500 and CT < 220000:
    elif 213500 < CT < 220000:
        SPlay.RiJinZhuSongLi()
        SPlay.GuaJi(22)
    # elif CT > 220000 and CT < 223000:
    elif 220000 < CT < 223000:
        SPlay.RiShenWei(70)
        SPlay.GuaJi(22, 30)
    # elif CT > 223000 and CT < 230000:
    elif 223000 < CT < 230000:
        SPlay.RiDuoBeiYaSong()
        SPlay.LinQuHuoYueJiangLi()
        SPlay.GuaJi(23, 30)
    else:
        time.sleep(1)
        SPlay.HuiShou()
        SPlay.GuaJi(23, 59, 59)
        SPlay.D += 1
        SPlay.HuiShou()
