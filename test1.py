import time

from test import AW

CT = (time.localtime()[3]*100) + (time.localtime()[4])
SPlay = AW()

SPlay.TabQieHuan()
SPlay.InIt()

while True:
    if CT > 1 and CT < 930:
        SPlay.GongXunRenWu(9, 120)
        SPlay.JingYingRenWu(9, 160)
        SPlay.ChuangTianGuan(850)
        SPlay.CaiLiaoFuBen()
        SPlay.HuiShou()
        SPlay.GeRenBoss(5)
        SPlay.HuiShou()
        SPlay.ChuMoRenWu()
        SPlay.TaFangFengMo(3)
    elif CT > 2100 and CT < 2135:
        SPlay.TaFangFengMo(1)
    elif CT > 2135 and CT < 2150:
        SPlay.RiJinZhuSongLi()
    elif CT > 2200 and CT < 2230:
        # SPlay.RiShenWei()
        SPlay.GuaJi()
        time.sleep(3600)
    elif CT > 2230 and CT < 2300:
        # SPlay.RiShenWei()
        SPlay.RiDuoBeiYaSong()
        # time.sleep(3600)
    else:
        time.sleep(1)
        SPlay.GeRenBoss(2)
        SPlay.GuaJi()
        time.sleep(1200)
        SPlay.HuiShouLess()
        # SPlay.TaFangFengMo()
        # SPlay.HuiShou()
        #
#     if CT > 100 and CT < 130:
#         time.sleep(1)
#         SPlay.InIt()
#         SPlay.TaFangFengMo()
#         SPlay.HuiShou()
#     elif CT > 1731 and CT < 1830:
#         time.sleep(1)
#         SPlay.InIt()
#         SPlay.RiMoBaiChengZhu()
#     else:
#         SPlay.InIt()
#         SPlay.GuaJi()
#         time.sleep(3600)
#         SPlay.HuiShou()
#     # elif CT > 221 and CT < 300:
#     #     time.sleep(1)
#     #     SPlay.InIt()
#     #     SPlay.JingYingRenWu()
#     #     SPlay.HuiShou()
#     # elif CT > 301 and CT < 330:
#     #     time.sleep(1)
#     #     SPlay.InIt()
#     #     SPlay.CaiLiaoFuBen()
#     #     SPlay.HuiShou()
#     # elif CT > 331 and CT < 410:
#     #     time.sleep(1)
#     #     SPlay.ChuMoRenWu()
#     #     SPlay.HuiShou()
#     # elif CT > 411 and CT < 440:
#     #     time.sleep(1)
#     #     SPlay.ChuangTianGuan()
#     #     SPlay.HuiShou()
#     # elif CT > 131 and CT < 220:
#     #     time.sleep(1)
#     #     SPlay.GongXunRenWu()
#     # elif CT > 131 and CT < 220:
#     #     time.sleep(1)
#     #     SPlay.GongXunRenWu()
#     # elif CT > 131 and CT < 220:
#     #     time.sleep(1)
#     #     SPlay.GongXunRenWu()
#     # elif CT > 131 and CT < 220:
#     #     time.sleep(1)
#     #     SPlay.GongXunRenWu()
#     # elif CT > 131 and CT < 220:
#     #     time.sleep(1)
#     #     SPlay.GongXunRenWu()
#     # elif CT > 131 and CT < 220:
#     #     time.sleep(1)
#     #     SPlay.GongXunRenWu()
#     # elif CT > 131 and CT < 220:
#     #     time.sleep(1)
#     #     SPlay.GongXunRenWu()
#     # elif CT > 131 and CT < 220:
#     #     time.sleep(1)
#     #     SPlay.GongXunRenWu()
#     # elif CT > 131 and CT < 220:
#     #     time.sleep(1)
#     #     SPlay.GongXunRenWu()
#     # elif CT > 131 and CT < 220:
#     #     time.sleep(1)
#     #     SPlay.GongXunRenWu()

