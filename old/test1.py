import time
from test import AW1
from test import current_date_time
from test import customize_init
from test import lin_qu_huo_yue_jiang_li
from test import lian_gong
# from test import re_start
shen_wei_time = 30
# SPlay = AW1(5, 81)
# SPlay.tab_qie_huan()
# customize_init()
time.sleep(5)

while True:
    SPlay = AW1(4, 81)
    print "start a new round at {}.".format(current_date_time())

    CT = ((time.localtime()[3] * 10000)
          + (time.localtime()[4] * 100)
          + (time.localtime()[5]))
    customize_init()
    if 1 < CT < 100000:
        SPlay.gong_xun_ren_wu(run_times=10,
                              extra_time=15, ge_su=3)
        SPlay.jing_ying_ren_wu(run_times=10,
                               extra_time=30, ge_su=6)
        SPlay.chuang_tian_guan(180)
        # SPlay.hui_shou_full()
        SPlay.cai_liao_fu_ben(which_one=3, fu_ben_time=2, extra_time=30)
        # SPlay.hui_shou_full()
        SPlay.ge_ren_boss(5)
        # SPlay.hui_shou_full()
        SPlay.ta_fang_feng_mo(1)
        SPlay.wei_wang_ren_wu()
        SPlay.chu_mo_ren_wu(45, False)
        lian_gong(45)
        SPlay.gua_ji(hh=10, mm=0, ss=0)

    # elif 100000 < CT < 103000:
    #     SPlay.ri_jin_zhu_song_li()
    #     SPlay.gua_ji(hh=10, mm=30)
    #
    # elif 103000 < CT < 111000:
    #     SPlay.ri_shen_wei(30)
    #     SPlay.gua_ji(hh=11, mm=10)

    elif 100000 < CT < 104000:
        SPlay.ri_jin_zhu_song_li()
        SPlay.gua_ji(hh=10, mm=40)

    elif 104000 < CT < 111000:
        SPlay.ri_shen_wei(shen_wei_time)
        SPlay.gua_ji(hh=11, mm=10)

    elif 111000 < CT < 113500:
        SPlay.ri_duo_bei_ya_song()
        SPlay.gua_ji(hh=11, mm=35)
        # re_start(40)

    elif 113000 < CT < 123000:
        SPlay.ri_hai_tian_sheng_yan()
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
        SPlay.gua_ji(hh=16, mm=15)
        # re_start(40)

    elif 161500 < CT < 173000:
        SPlay.ri_jin_zhu_song_li()
        SPlay.gua_ji(hh=17, mm=30)

    elif 173000 < CT < 185925:
        SPlay.ri_mo_bai_cheng_zhu()
        SPlay.gua_ji(hh=18, mm=59, ss=25)

    elif 185925 < CT < 192000:
        SPlay.ri_world_boss()
        SPlay.gua_ji(hh=19, mm=20)

    elif 192000 < CT < 193925:
        SPlay.ri_da_ti()
        SPlay.gua_ji(hh=19, mm=39, ss=25)

    elif 193925 < CT < 200000:
        SPlay.ri_ye_zhan_bi_qi()
        SPlay.gua_ji(hh=20)

    elif 200000 < CT < 213500:
        SPlay.bang_hui_huo_dong()
        SPlay.gua_ji(hh=21, mm=35)

    # elif 213500 < CT < 220000:
    #     SPlay.ri_jin_zhu_song_li()
    #     SPlay.gua_ji(hh=22)
    #
    # elif 220000 < CT < 223000:
    #     SPlay.ri_shen_wei(90)
    #     lin_qu_huo_yue_jiang_li()
    #     SPlay.gua_ji(hh=22, mm=30)

    elif 213500 < CT < 221000:
        SPlay.ri_jin_zhu_song_li()
        SPlay.gua_ji(hh=22, mm=10)

    elif 221000 < CT < 223000:
        SPlay.ri_shen_wei(shen_wei_time)
        lin_qu_huo_yue_jiang_li()
        SPlay.gua_ji(hh=22, mm=30)

    else:
        time.sleep(1)
        # SPlay.hui_shou_full()
        SPlay.gua_ji(hh=23, mm=58)
        # SPlay.hui_shou_full()
