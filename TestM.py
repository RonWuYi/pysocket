import time

from NewAllWay import AW
from test import AW1

CT = (time.localtime()[3]*100) + (time.localtime()[4])
SPlay = AW()
SPlayN = AW1()

time.sleep(5)
# SPlay.InIt()b
# SPlay.GongXunRenWu(9, 120)
SPlayN.ChuMoRenWu()