import time

from NewAllWay import AW
from test import AW1

CT = (time.localtime()[3]*100) + (time.localtime()[4])
SPlay = AW()
SPlayN = AW1(2)

time.sleep(2)
SPlayN.GoChuMoNPC()
# SPlayN.TaFangFengMo(3)