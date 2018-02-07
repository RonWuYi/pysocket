import time
from datetime import datetime
from NewAllWay import AW
from test import AW1

CT = ((time.localtime()[3] * 10000) + (time.localtime()[4] * 100) + (time.localtime()[5]))
# print CT
SPlay = AW()
SPlayN = AW1(2)
# time.sleep(3)
#
# print datetime.now()
#

print SPlayN.seconds_change(SPlayN._TimeDiff(23, 59))
# print type(SPlayN.SecondsChange(SPlayN._TimeDiff(19, 5)))
# #
# SPlayN.GuaSuoYaoTa()