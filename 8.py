import time
from datetime import datetime
from test import AW1


SPlay = AW1(4)
# SPlay.TabQieHuan()
# SPlay.InIt()b
# CurrentLevel = 4b

while True:
    # CT = (time.localtime()[3]*100) + (time.localtime()[4])B
    #
    # print CTzbzz
    # SPlay.GuaJi(15, 0)BBBKEY BBBB

    A = datetime.now()
    SPlay.InIt()
    B = datetime.now()
    print (B - A).seconds
    time.sleep(2)
