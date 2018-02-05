import time
from datetime import datetime
from NewAllWay import AW
from test import AW1

CT = (time.localtime()[3]*100) + (time.localtime()[4])
SPlay = AW()
SPlayN = AW1(2)
# time.sleep(3)

print datetime.now()
print SPlayN.SecondsChange(SPlayN._TimeDiff(23, 59, 59))

print SPlayN.CurrentDateTime()