import time

from NewAllWay import AW

CT = (time.localtime()[3]*100) + (time.localtime()[4])
SPlay = AW()

time.sleep(5)
SPlay.InIt()