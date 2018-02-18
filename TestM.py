import time
from datetime import datetime
from NewAllWay import AW
from test import AW1
from test import _re_start
from test import customize_init
from test import lian_gong

# CT = ((time.localtime()[3] * 10000) + (time.localtime()[4] * 100) + (time.localtime()[5]))
# # print CT
# SPlay = AW()
SPlay = AW1(0,81)
time.sleep(2)
#
# print datetime.now()
#

# print seconds_change(SPlayN._time_diff(23, 59))
# print type(SPlayN.SecondsChange(SPlayN._TimeDiff(19, 5)))
# #
# customize_init()
# _go_gua_ji_npc()
# _re_start()
SPlay.gong_xun_ren_wu(run_times=10, extra_time=110, ge_su=3)
SPlay.jing_ying_ren_wu(run_times=10, extra_time=125, ge_su=5)
SPlay.chuang_tian_guan(120)
SPlay.hui_shou_full()
SPlay.cai_liao_fu_ben(which_one=4, extra_time=50)
SPlay.hui_shou_full()
SPlay.ge_ren_boss(120)
SPlay.hui_shou_full()
SPlay.ta_fang_feng_mo(3)
SPlay.wei_wang_ren_wu()
SPlay.chu_mo_ren_wu(45, False)
lian_gong(45)