import time
from AllWay import AW

SPlay = AW()

time.sleep(2)
SPlay.TabQieHuan()

while True:
    CT = (time.localtime()[3] * 100) + (time.localtime()[4])
    if CT > 100 and CT < 130:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        # elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == True:
        #     print "keep the same status"
        else:
            print "keep the same status"
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
        if SPlay.Complete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        continue
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    else:
        time.sleep(5)
        SPlay.GuaJi()
        time.sleep(3600)