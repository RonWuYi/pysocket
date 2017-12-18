import time
from AllWay import AW


CT = (time.localtime()[3]*100) + (time.localtime()[4])

SPlay = AW()

time.sleep(2)
SPlay.TabQieHuan()

while True:
    if CT > 100 and CT < 130:
        time.sleep(1)
        SPlay.TaFangFengMo()
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
    elif CT > 131 and CT < 220:
        time.sleep(1)
        SPlay.GongXunRenWu()
    else:
        time.sleep(5)
        SPlay.GuaJi()
        time.sleep(3600)