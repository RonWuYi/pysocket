import time
from NewAllWay import AW

SPlay = AW()

time.sleep(2)
SPlay.TabQieHuan()

while True:
    CT = (time.localtime()[3] * 100) + (time.localtime()[4])
    if CT > 100 and CT < 150:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 151 and CT < 240:
        if SPlay.JingYingRenWuComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.JingYingRenWu()
        elif SPlay.JingYingRenWuComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "JingYingRenWu Complete, keep the same status"
    elif CT > 241 and CT < 330:
        if SPlay.GongXunRenWuComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.GongXunRenWu()
        elif SPlay.GongXunRenWuComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "GongXunRenWu Complete, keep the same status"
    elif CT > 331 and CT < 420:
        if SPlay.CaiLiaoFuBenComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.CaiLiaoFuBen()
        elif SPlay.CaiLiaoFuBenComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "CaiLiaoFuBen Complete, keep the same status"
    elif CT > 421 and CT < 510:
        if SPlay.ChuMoRenWuComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.ChuMoRenWu()
        elif SPlay.ChuMoRenWuComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "ChuMoRenWu Complete, keep the same status"
    elif CT > 511 and CT < 600:
        if SPlay.WeiWangRenWuComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.WeiWangRenWu()
        elif SPlay.WeiWangRenWuComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "WeiWangRenWu Complete, keep the same status"
    elif CT > 601 and CT < 650:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 651 and CT < 740:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 741 and CT < 830:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 831 and CT < 920:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 921 and CT < 1010:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 1011 and CT < 1100:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 1101 and CT < 1150:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 1151 and CT < 1240:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 1241 and CT < 1330:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 1331 and CT < 1420:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            if SPlay.TaFangFengMoComplete == False:
                time.sleep(1)
                SPlay.InIt()
                SPlay.HuiShou()
                SPlay.InIt()
                SPlay.TaFangFengMo()
            elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
                SPlay.InIt()
                SPlay.GuaJi()
            else:
                print "TaFangFengMo Complete, keep the same status"
    elif CT > 1421 and CT < 1510:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            if SPlay.TaFangFengMoComplete == False:
                time.sleep(1)
                SPlay.InIt()
                SPlay.HuiShou()
                SPlay.InIt()
                SPlay.TaFangFengMo()
            elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
                SPlay.InIt()
                SPlay.GuaJi()
            else:
                print "TaFangFengMo Complete, keep the same status"
    elif CT > 1511 and CT < 1600:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            if SPlay.TaFangFengMoComplete == False:
                time.sleep(1)
                SPlay.InIt()
                SPlay.HuiShou()
                SPlay.InIt()
                SPlay.TaFangFengMo()
            elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
                SPlay.InIt()
                SPlay.GuaJi()
            else:
                print "TaFangFengMo Complete, keep the same status"
    elif CT > 1601 and CT < 1650:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            if SPlay.TaFangFengMoComplete == False:
                time.sleep(1)
                SPlay.InIt()
                SPlay.HuiShou()
                SPlay.InIt()
                SPlay.TaFangFengMo()
            elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
                SPlay.InIt()
                SPlay.GuaJi()
            else:
                print "TaFangFengMo Complete, keep the same status"
    elif CT > 1651 and CT < 1740:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            if SPlay.TaFangFengMoComplete == False:
                time.sleep(1)
                SPlay.InIt()
                SPlay.HuiShou()
                SPlay.InIt()
                SPlay.TaFangFengMo()
            elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
                SPlay.InIt()
                SPlay.GuaJi()
            else:
                print "TaFangFengMo Complete, keep the same status"
    elif CT > 1741 and CT < 1830:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            if SPlay.TaFangFengMoComplete == False:
                time.sleep(1)
                SPlay.InIt()
                SPlay.HuiShou()
                SPlay.InIt()
                SPlay.TaFangFengMo()
            elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
                SPlay.InIt()
                SPlay.GuaJi()
            else:
                print "TaFangFengMo Complete, keep the same status"
    elif CT > 1831 and CT < 1920:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            if SPlay.TaFangFengMoComplete == False:
                time.sleep(1)
                SPlay.InIt()
                SPlay.HuiShou()
                SPlay.InIt()
                SPlay.TaFangFengMo()
            elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
                SPlay.InIt()
                SPlay.GuaJi()
            else:
                print "TaFangFengMo Complete, keep the same status"
    elif CT > 1921 and CT < 2010:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            if SPlay.TaFangFengMoComplete == False:
                time.sleep(1)
                SPlay.InIt()
                SPlay.HuiShou()
                SPlay.InIt()
                SPlay.TaFangFengMo()
            elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
                SPlay.InIt()
                SPlay.GuaJi()
            else:
                print "TaFangFengMo Complete, keep the same status"
    elif CT > 2011 and CT < 2100:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.TaFangFengMo()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            if SPlay.TaFangFengMoComplete == False:
                time.sleep(1)
                SPlay.InIt()
                SPlay.HuiShou()
                SPlay.InIt()
                SPlay.TaFangFengMo()
            elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
                SPlay.InIt()
                SPlay.GuaJi()
            else:
                print "TaFangFengMo Complete, keep the same status"
    else:
        SPlay.InIt()
        SPlay.GuaJi()
        time.sleep(3600)
        SPlay.HuiShou()