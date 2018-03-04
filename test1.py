import time
from test import AW1
from test import current_date_time
from test import customize_init
from test import lin_qu_huo_yue_jiang_li
from test import lian_gong
# from test import re_start

SPlay = AW1(2, 81)
SPlay.tab_qie_huan()
customize_init()

while True:
    SPlay = AW1(2, 81)
    print "start a new round at " \
          "{}, with {} events " \
          "complete.".format(current_date_time(), SPlay.EventTime)
    CT = ((time.localtime()[3] * 10000) + (time.localtime()[4] * 100) + (time.localtime()[5]))

    if 1 < CT < 100000:
        SPlay.gong_xun_ren_wu(run_times=10, extra_time=15, ge_su=3)
        SPlay.jing_ying_ren_wu(run_times=10, extra_time=35, ge_su=5)
        SPlay.chuang_tian_guan(140)
        SPlay.hui_shou_full()
        SPlay.cai_liao_fu_ben(which_one=7, extra_time=30)
        SPlay.hui_shou_full()
        SPlay.ge_ren_boss(160)
        SPlay.hui_shou_full()
        SPlay.ta_fang_feng_mo(3)
        SPlay.wei_wang_ren_wu()
        SPlay.chu_mo_ren_wu(45, False)
        lian_gong(45)
        SPlay.gua_ji(hh=10, mm=0, ss=0)

    elif 100000 < CT < 103000:
        SPlay.ri_jin_zhu_song_li()
        SPlay.gua_ji(hh=10, mm=30)

    elif 103000 < CT < 111000:
        SPlay.ri_shen_wei(30)
        SPlay.gua_ji(hh=11, mm=10)

    elif 111000 < CT < 113500:
        SPlay.ri_duo_bei_ya_song()
        SPlay.gua_ji(hh=11, mm=35)
        # re_start(40)

    elif 113500 < CT < 130000:
        # lian_gong(30)
        SPlay.gua_ji(hh=13)

    elif 130000 < CT < 140000:
        SPlay.ri_suo_yao_ta()
        SPlay.gua_ji(hh=14)

    elif 140000 < CT < 143500:
        SPlay.ri_shi_mu()
        SPlay.gua_ji(hh=14, mm=35)

    elif 143500 < CT < 150000:
        SPlay.ri_bi_guan()
        SPlay.gua_ji(hh=15)

    elif 150000 < CT < 161500:
        SPlay.ri_guai_wu_gong_cheng()
        SPlay.gua_ji(hh=17)
        # re_start(40)

    elif 161500 < CT < 173000:
        SPlay.ri_jin_zhu_song_li()
        SPlay.gua_ji(hh=17, mm=30)

    elif 173000 < CT < 190000:
        SPlay.ri_mo_bai_cheng_zhu()
        SPlay.gua_ji(hh=19)

    elif 190000 < CT < 192000:
        SPlay.ri_world_boss()
        SPlay.gua_ji(hh=19, mm=20)

    elif 192000 < CT < 194000:
        SPlay.ri_da_ti()
        SPlay.gua_ji(hh=19, mm=40)

    elif 194000 < CT < 200000:
        SPlay.ri_ye_zhan_bi_qi()
        SPlay.gua_ji(hh=20)

    elif 200000 < CT < 213500:
        SPlay.bang_hui_huo_dong()
        SPlay.gua_ji(hh=21, mm=35)

    elif 213500 < CT < 220000:
        SPlay.ri_jin_zhu_song_li()
        SPlay.gua_ji(hh=22)

    elif 220000 < CT < 223000:
        SPlay.ri_shen_wei(90)
        lin_qu_huo_yue_jiang_li()
        SPlay.gua_ji(hh=22, mm=30)

    else:
        time.sleep(1)
        SPlay.hui_shou_full()
        SPlay.gua_ji(hh=23, mm=58)
        SPlay.hui_shou_full()
