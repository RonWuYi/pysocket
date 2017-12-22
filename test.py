import time

# CT = (time.localtime()[3]*100) + (time.localtime()[4])
# print CT
from NewAllWay import AW
SPlay = AW()

# time.sleep(2)z
SPlay.TabQieHuan()
SPlay.InIt()
SPlay.GeRenBoss()
while True:
    SPlay.InIt()
    SPlay.GuaJi()
    time.sleep(3600)
    SPlay.HuiShou()