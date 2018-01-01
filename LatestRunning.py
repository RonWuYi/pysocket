import time
from NewAllWay import AW

SPlay = AW()
time.sleep(2)
SPlay.TabQieHuan()

while True:
    CT = (time.localtime()[3] * 100) + (time.localtime()[4])
    if CT > 1 and CT < 530:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.TaFangFengMo()
            SPlay.HuiShouLess()
            SPlay.JingYingRenWu()
            SPlay.HuiShouLess()
            SPlay.GongXunRenWu()
            SPlay.HuiShouLess()
            # SPlay.CaiLiaoFuBen()
            # SPlay.HuiShou()
            SPlay.ChuangTianGuan()
            SPlay.HuiShouLess()
            SPlay.ChuMoRenWu()
            SPlay.WeiWangRenWu()
            SPlay.GeRenBoss()
            SPlay.HuiShouLess()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "CaiLiaoFuBen Complete, keep the same status"
    # if CT > 100 and CT < 150:
    #     if SPlay.GeRenBossiComplete == False:
    #         time.sleep(1)
    #         SPlay.InIt()
    #         SPlay.HuiShou()
    #         SPlay.InIt()
    #         SPlay.GeRenBoss()
    #     elif SPlay.GeRenBossiComplete == True and SPlay.GuaJiFlag == False:
    #         SPlay.InIt()
    #         SPlay.GuaJi()
    #     else:
    #         print "TaFangFengMo Complete, keep the same status"
    # elif CT > 151 and CT < 240:
    #     if SPlay.JingYingRenWuComplete == False:
    #         time.sleep(1)
    #         SPlay.InIt()
    #         SPlay.HuiShou()
    #         SPlay.InIt()
    #         SPlay.JingYingRenWu()
    #     elif SPlay.JingYingRenWuComplete == True and SPlay.GuaJiFlag == False:
    #         SPlay.InIt()
    #         SPlay.GuaJi()
    #     else:
    #         print "JingYingRenWu Complete, keep the same status"
    # elif CT > 241 and CT < 330:
    #     if SPlay.GongXunRenWuComplete == False:
    #         time.sleep(1)
    #         SPlay.InIt()
    #         SPlay.HuiShou()
    #         SPlay.InIt()
    #         SPlay.GongXunRenWu()
    #     elif SPlay.GongXunRenWuComplete == True and SPlay.GuaJiFlag == False:
    #         SPlay.InIt()
    #         SPlay.GuaJi()
    #     else:
    #         print "GongXunRenWu Complete, keep the same status"
    elif CT > 531 and CT < 1010:
        SPlay.InIt()
        SPlay.GuaJi()
        # if SPlay.CaiLiaoFuBenComplete == False:
        #     time.sleep(1)
        #     SPlay.InIt()
        #     SPlay.HuiShou()
        #     SPlay.InIt()
        #     SPlay.CaiLiaoFuBen()
        # elif SPlay.CaiLiaoFuBenComplete == True and SPlay.GuaJiFlag == False:
        #     SPlay.InIt()
        #     SPlay.GuaJi()
        # else:
        #     print "CaiLiaoFuBen Complete, keep the same status"
    # elif CT > 421 and CT < 510:
    #     if SPlay.ChuMoRenWuComplete == False:
    #         time.sleep(1)
    #         SPlay.InIt()
    #         SPlay.HuiShou()
    #         SPlay.InIt()
    #         SPlay.ChuMoRenWu()
    #     elif SPlay.ChuMoRenWuComplete == True and SPlay.GuaJiFlag == False:
    #         SPlay.InIt()
    #         SPlay.GuaJi()
    #     else:
    #         print "ChuMoRenWu Complete, keep the same status"
    # elif CT > 511 and CT < 600:
    #     if SPlay.WeiWangRenWuComplete == False:
    #         time.sleep(1)
    #         SPlay.InIt()
    #         SPlay.HuiShou()
    #         SPlay.InIt()
    #         SPlay.WeiWangRenWu()
    #     elif SPlay.WeiWangRenWuComplete == True and SPlay.GuaJiFlag == False:
    #         SPlay.InIt()
    #         SPlay.GuaJi()
    #     else:
    #         print "WeiWangRenWu Complete, keep the same status"
    # elif CT > 601 and CT < 650:
    #     if SPlay.TaFangFengMoComplete == False:
    #         time.sleep(1)
    #         SPlay.InIt()
    #         SPlay.HuiShou()
    #         SPlay.InIt()
    #         SPlay.TaFangFengMo()
    #     elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
    #         SPlay.InIt()
    #         SPlay.GuaJi()
    #     else:
    #         print "TaFangFengMo Complete, keep the same status"
    # elif CT > 651 and CT < 740:
    #     if SPlay.TaFangFengMoComplete == False:
    #         time.sleep(1)
    #         SPlay.InIt()
    #         SPlay.HuiShou()
    #         SPlay.InIt()
    #         SPlay.TaFangFengMo()
    #     elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
    #         SPlay.InIt()
    #         SPlay.GuaJi()
    #     else:
    #         print "TaFangFengMo Complete, keep the same status"
    # elif CT > 741 and CT < 830:
    #     if SPlay.TaFangFengMoComplete == False:
    #         time.sleep(1)
    #         SPlay.InIt()
    #         SPlay.HuiShou()
    #         SPlay.InIt()
    #         SPlay.TaFangFengMo()
    #     elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
    #         SPlay.InIt()
    #         SPlay.GuaJi()
    #     else:
    #         print "TaFangFengMo Complete, keep the same status"
    # elif CT > 831 and CT < 920:
    #     if SPlay.TaFangFengMoComplete == False:
    #         time.sleep(1)
    #         SPlay.InIt()
    #         SPlay.HuiShou()
    #         SPlay.InIt()
    #         SPlay.TaFangFengMo()
    #     elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
    #         SPlay.InIt()
    #         SPlay.GuaJi()
    #     else:
    #         print "TaFangFengMo Complete, keep the same status"
    # elif CT > 921 and CT < 1010:
    #     if SPlay.TaFangFengMoComplete == False:
    #         time.sleep(1)
    #         SPlay.InIt()
    #         SPlay.HuiShou()
    #         SPlay.InIt()
    #         SPlay.TaFangFengMo()
    #     elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
    #         SPlay.InIt()
    #         SPlay.GuaJi()
    #     else:
    #         print "TaFangFengMo Complete, keep the same status"
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
    elif CT > 1331 and CT < 1400:
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
    elif CT > 1405 and CT < 1435:
        if SPlay.TaFangFengMoComplete == False:
            time.sleep(1)
            SPlay.InIt()
            # SPlay.HuiShou()
            # SPlay.InIt()
            SPlay.RiShiMuMiZhen()
        elif SPlay.TaFangFengMoComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 1435 and CT < 1500:
        if SPlay.BiGuanComplete == False:
            time.sleep(1)
            SPlay.InIt()
            # SPlay.HuiShou()
            # SPlay.InIt()
            SPlay.RiBiGuan()
        elif SPlay.BiGuanComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    elif CT > 1501 and CT < 1614:
        if SPlay.JiaLanShenDianComplete == False:
            time.sleep(1)
            SPlay.InIt()
            # SPlay.HuiShou()
            # SPlay.InIt()
            SPlay.RiJiaLanShenDian()
        elif SPlay.JiaLanShenDianComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "JiaLanShenDian Complete, keep the same status"
    elif CT > 1615 and CT < 1630:
        SPlay.JinZhuSongLiComplete =False
        if SPlay.MoBaiChengZhuComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            # SPlay.InIt()
            SPlay.RiJinZhuSongLi()
        elif SPlay.MoBaiChengZhuComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "MoBaiChengZhu Complete, keep the same status"
    elif CT > 1631 and CT < 1830:
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
    elif CT > 1905 and CT < 1920:
        if SPlay.WorldBossComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.WorldBoss()
        elif SPlay.WorldBossComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "WorldBoss Complete, keep the same status"
    elif CT > 1930 and CT < 1950:
        if SPlay.YeZhanBiQiComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.YeZhanBiQi()
        elif SPlay.YeZhanBiQiComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "YeZhanBiQi Complete, keep the same status"
    elif CT > 2011 and CT < 2130:
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
    elif CT > 2135 and CT < 2151:
        if SPlay.JinZhuSongLiComplete == False:
            time.sleep(1)
            SPlay.InIt()
            SPlay.HuiShou()
            SPlay.InIt()
            SPlay.JinZhuSongLi()
        # elif SPlay.JinZhuSongLiComplete == True and SPlay.GuaJiFlag == False:
        #     if SPlay.TaFangFengMoComplete == False:
        #         time.sleep(1)
        #         SPlay.InIt()
        #         SPlay.HuiShou()
        #         SPlay.InIt()
        #         SPlay.TaFangFengMo()
        elif SPlay.JinZhuSongLiComplete == True and SPlay.GuaJiFlag == False:
            SPlay.InIt()
            SPlay.GuaJi()
        else:
            print "TaFangFengMo Complete, keep the same status"
    else:
        SPlay.InIt()
        SPlay.GuaJi()
        time.sleep(3600)
        SPlay.HuiShou()