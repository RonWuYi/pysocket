import time
from test import AW1
from test import lian_gong

while True:
    SPlay = AW1(2, 81)
    time.sleep(5)
    SPlay.gong_xun_ren_wu(run_times=10, extra_time=40, ge_su=3)
    SPlay.jing_ying_ren_wu(run_times=10, extra_time=60, ge_su=7)
    SPlay.chuang_tian_guan(160)
    SPlay.cai_liao_fu_ben(fu_ben_time=2, which_one=7, extra_time=50)
    SPlay.ge_ren_boss(160)
    SPlay.ta_fang_feng_mo(3)
    SPlay.wei_wang_ren_wu()
    SPlay.chu_mo_ren_wu(45, False)
    lian_gong(45)
    time.sleep(1)
    SPlay.gua_ji(hh=23, mm=58)
