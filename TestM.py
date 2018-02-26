import time
from test import AW1
from test import customize_init
from test import lin_qu_huo_yue_jiang_li
from test import lian_gong

SPlay = AW1(2, 81)
SPlay.tab_qie_huan()
customize_init()

while True:
    SPlay = AW1(2, 81)
    time.sleep(5)
    SPlay.gong_xun_ren_wu(run_times=10, extra_time=40, ge_su=3)
    SPlay.jing_ying_ren_wu(run_times=10, extra_time=60, ge_su=5)
    SPlay.chuang_tian_guan(160)
    SPlay.hui_shou_full()
    SPlay.cai_liao_fu_ben(which_one=7, extra_time=50)
    SPlay.hui_shou_full()
    SPlay.ge_ren_boss(160)
    SPlay.hui_shou_full()
    SPlay.ta_fang_feng_mo(3)
    SPlay.wei_wang_ren_wu()
    SPlay.chu_mo_ren_wu(45, False)
    lian_gong(45)
    SPlay.gua_ji(hh=10, mm=0, ss=0)
    time.sleep(1)
    SPlay.hui_shou_full()
    SPlay.gua_ji(hh=23, mm=58)
    lin_qu_huo_yue_jiang_li()
    SPlay.hui_shou_full()
