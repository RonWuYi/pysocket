import time
from AllWay import AW


CT = (time.localtime()[3]*100) + (time.localtime()[4])

SPlay = AW()

time.sleep(2)
SPlay.TabQieHuan()

while True:
    if CT > 100 and CT < 130:
        time.sleep(1)
        SPlay.InIt()
        SPlay.TaFangFengMo()
        SPlay.HuiShou()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.InIt()
        SPlay.GongXunRenWu()
        SPlay.HuiShou()
    elif CT > 221 and CT < 300:
        time.sleep(1)
        SPlay.InIt()
        SPlay.JingYingRenWu()
        SPlay.HuiShou()
    elif CT > 301 and CT < 330:
        time.sleep(1)
        SPlay.InIt()
        SPlay.CaiLiaoFuBen()
        SPlay.HuiShou()
    elif CT > 331 and CT < 410:
        time.sleep(1)
        SPlay.ChuMoRenWu()
        SPlay.HuiShou()
    elif CT > 411 and CT < 440:
        time.sleep(1)
        SPlay.ChuangTianGuan()
        SPlay.HuiShou()
    # elif CT > 131 and CT < 220:
    #     time.sleep(1)
    #     SPlay.GongXunRenWu()
    # elif CT > 131 and CT < 220:
    #     time.sleep(1)
    #     SPlay.GongXunRenWu()
    # elif CT > 131 and CT < 220:
    #     time.sleep(1)
    #     SPlay.GongXunRenWu()
    # elif CT > 131 and CT < 220:
    #     time.sleep(1)
    #     SPlay.GongXunRenWu()
    # elif CT > 131 and CT < 220:
    #     time.sleep(1)
    #     SPlay.GongXunRenWu()
    # elif CT > 131 and CT < 220:
    #     time.sleep(1)
    #     SPlay.GongXunRenWu()
    # elif CT > 131 and CT < 220:
    #     time.sleep(1)
    #     SPlay.GongXunRenWu()
    # elif CT > 131 and CT < 220:
    #     time.sleep(1)
    #     SPlay.GongXunRenWu()
    # elif CT > 131 and CT < 220:
    #     time.sleep(1)
    #     SPlay.GongXunRenWu()
    # elif CT > 131 and CT < 220:
    #     time.sleep(1)
    #     SPlay.GongXunRenWu()
    else:
        time.sleep(5)
        SPlay.GuaJi()
        time.sleep(3600)
        SPlay.HuiShou()