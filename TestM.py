import time
from datetime import datetime
from NewAllWay import AW
from test import AW1
from test import _re_start
from test import customize_init

CT = ((time.localtime()[3] * 10000) + (time.localtime()[4] * 100) + (time.localtime()[5]))
# print CT
SPlay = AW()
SPlayN = AW1(2)
time.sleep(2)
#
# print datetime.now()
#

# print seconds_change(SPlayN._time_diff(23, 59))
# print type(SPlayN.SecondsChange(SPlayN._TimeDiff(19, 5)))
# #
customize_init()
# _go_gua_ji_npc()
# _re_start()
SPlayN.wei_wang_ren_wu()