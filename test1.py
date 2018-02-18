import time
from test import AW1
from test import current_date_time
from test import customize_init
from test import lin_qu_huo_yue_jiang_li
from test import lian_gong
# from test import capture_pic

SPlay = AW1(2, 81)
SPlay.tab_qie_huan()
customize_init()

while True:
    print "start a new round at " \
          "{}, with {} times events " \
          "complete.".format(current_date_time(), SPlay.EventTime)
    CT = ((time.localtime()[3] * 10000) + (time.localtime()[4] * 100) + (time.localtime()[5]))
    # if CT > 1 and CT < 100000:

    if 1 < CT < 100000:
        # capture_pic(CT)
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
        SPlay.gua_ji(10, 0)

    elif 100000 < CT < 103000:
        SPlay.ri_jin_zhu_song_li()
        SPlay.gua_ji(10, 30)
    # elif CT > 103000 and CT < 111000:

    elif 103000 < CT < 111000:

        SPlay.ri_shen_wei(30)
        SPlay.gua_ji(11, 10)
    # elif CT > 111000 and CT < 113500:

    elif 111000 < CT < 113500:
        SPlay.ri_duo_bei_ya_song()
        SPlay.gua_ji(11, 35)
    # elif CT > 113500 and CT < 130000:

    elif 113500 < CT < 130000:
        lian_gong(30)
        SPlay.gua_ji(13)
    # elif CT > 130000 and CT < 140000:

    elif 130000 < CT < 140000:
        # capture_pic(CT)
        SPlay.ri_suo_yao_ta()
        SPlay.gua_ji(14)
    # elif CT > 140000 and CT < 143500:

    elif 140000 < CT < 143500:
        SPlay.ri_shi_mu()
        SPlay.gua_ji(14, 35)
    # elif CT > 143500 and CT < 150000:

    elif 143500 < CT < 150000:
        SPlay.ri_bi_guan()
        SPlay.gua_ji(15, 0)
    # elif CT > 150000 and CT < 173000:

    elif 150000 < CT < 173000:
        SPlay.ri_guai_wu_gong_cheng()
        SPlay.gua_ji(17)
    # elif CT > 150000 and CT < 173000:
    #     SPlay.RiJiaLanShenDian()
    #     SPlay.GuaJi(17, 30)
    # elif CT > 173000 and CT < 190000:

    elif 173000 < CT < 190000:
        SPlay.ri_mo_bai_cheng_zhu()
        SPlay.gua_ji(19)
    # elif CT > 190000 and CT < 192000:

    elif 190000 < CT < 192000:

        SPlay.ri_world_boss()
        SPlay.gua_ji(19, 20)
    # elif CT > 192000 and CT < 194000:

    elif 192000 < CT < 194000:
        # SPlay.CapturePic(CT)
        SPlay.ri_da_ti()
        SPlay.gua_ji(19, 40)
    # elif CT > 194000 and CT < 200000:
    elif 194000 < CT < 200000:
        # SPlay.CapturePic(CT)
        SPlay.ri_ye_zhan_bi_qi()
        SPlay.gua_ji(20)
    # elif CT > 200000 and CT < 213500:
    elif 200000 < CT < 213500:
        # SPlay.CapturePic(CT)
        SPlay.bang_hui_huo_dong()
        SPlay.gua_ji(21, 35)
    # elif CT > 213500 and CT < 220000:
    elif 213500 < CT < 220000:
        SPlay.ri_jin_zhu_song_li()
        SPlay.gua_ji(22)
    # elif CT > 220000 and CT < 223000:
    elif 220000 < CT < 223000:
        SPlay.ri_shen_wei(70)
        SPlay.gua_ji(22, 30)
    # elif CT > 223000 and CT < 230000:
    elif 223000 < CT < 230000:
        SPlay.ri_duo_bei_ya_song()
        lin_qu_huo_yue_jiang_li()
        SPlay.gua_ji(23, 30)
    else:
        time.sleep(1)
        SPlay.hui_shou_full()
        SPlay.gua_ji(23, 59, 59)
        SPlay.D += 1
        SPlay.hui_shou_full()
