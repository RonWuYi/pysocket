import time

from NewAllWay import AW
from test import AW1

CT = (time.localtime()[3]*100) + (time.localtime()[4])
SPlay = AW()
SPlayN = AW1()

time.sleep(5)
SPlay.InIt()
# SPlay.GongXunRenWu(9, 120)
SPlay.JingYingRenWu(9, 160)