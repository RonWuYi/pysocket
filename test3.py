import time

from test import AW1


SPlay = AW1(3)
# SPlay.TabQieHuan()
# SPlay.InIt()

while True:
    print "####################################################"
    print "start a round at {}".format(SPlay.CurrentDateTime())
    CT = ((time.localtime()[3] * 10000) + (time.localtime()[4]*100) + (time.localtime()[5]))
    print "another round CT is ", CT
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
        print "CT is ", CT
        SPlay.TestPlay("CT > 1 and CT < 1000")
        SPlay.TestGuaJi(10, 0, 0)
    elif CT > 100000 and CT < 103000:
        print "CT is ", CT
        SPlay.TestPlay("CT > 1000 and CT < 1030:")
        SPlay.TestGuaJi(10, 30, 0)
    elif CT > 103000 and CT < 130000:
        print "CT is ", CT
        SPlay.TestPlay("CT > 1030 and CT < 1300:")
        SPlay.TestGuaJi(13, 0, 0)
    elif CT > 130000 and CT < 140000:
        print "CT is ", CT
        SPlay.TestPlay("CT > 1300 and CT < 1400:")
        SPlay.TestGuaJi(14, 0, 0)
    elif CT > 140000 and CT < 143500:
        print "CT is ", CT
        SPlay.TestPlay("CT > 1400 and CT < 1435:")
        SPlay.TestGuaJi(14, 35, 0)
    elif CT > 143500 and CT < 150000:
        print "CT is ", CT
        SPlay.TestPlay("CT > 1435 and CT < 1500:")
        SPlay.TestGuaJi(15, 0, 0)
    elif CT > 150000 and CT < 173000:
        print "CT is ", CT
        SPlay.TestPlay("CT > 1500 and CT < 1730:")
        SPlay.TestGuaJi(17, 30, 0)
    elif CT > 173000 and CT < 190500:
        print "CT is ", CT
        SPlay.TestPlay("CT > 1730 and CT < 1905:")
        SPlay.TestGuaJi(19, 5, 0)
    elif CT > 190500 and CT < 193000:
        print "CT is ", CT
        SPlay.TestPlay("CT > 1905 and CT < 1930:")
        SPlay.TestGuaJi(19, 3, 0)
    elif CT > 193000 and CT < 213500:
        print "CT is ", CT
        SPlay.TestPlay("CT > 1930 and CT < 2135:")
        SPlay.TestGuaJi(21, 35, 0)
    elif CT > 213500 and CT < 220000:
        print "CT is ", CT
        SPlay.TestPlay(" CT > 2135 and CT < 2200:")
        SPlay.TestGuaJi(22, 0, 0)
    elif CT > 220000 and CT < 223000:
        print "CT is ", CT
        SPlay.TestPlay("CT > 2200 and CT < 2230:")
        SPlay.TestGuaJi(22, 30, 0)
    elif CT > 223000 and CT < 230000:
        print "CT is ", CT
        SPlay.TestPlay("CT > 2230 and CT < 2300:")
        SPlay.TestGuaJi(23, 0, 0)
    else:
        print "CT is ", CT
        SPlay.TestPlay("The finial:")
        time.sleep(1)
        SPlay.HuiShou()
        SPlay.GuaJi(23, 59, 59)
        SPlay.D +=1
        SPlay.HuiShou()