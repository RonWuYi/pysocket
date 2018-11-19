from old.test import AW1
from old.util import *

shen_wei_time = 30


class running(object):

    def mainrun(self):
        time.sleep(2)
        tab_qie_huan()
        time.sleep(3)

        while True:
            SPlay = AW1(4, 81)
            print "start a new round at {}.".format(current_date_time())

            CT = ((time.localtime()[3] * 10000)
                  + (time.localtime()[4] * 100)
                  + (time.localtime()[5]))
            customize_init()
            # if 1 < CT < 100000:
            qi_fu()
            time.sleep(1)
            lan_yue_da_ren()
            time.sleep(1)
            SPlay.gong_xun_ren_wu(run_times=10,
                                  extra_time=15, ge_su=3)
            SPlay.jing_ying_ren_wu(run_times=10,
                                   extra_time=7, ge_su=7)
            SPlay.chuang_tian_guan(180)
            # SPlay.hui_shou_full()
            SPlay.cai_liao_fu_ben(which_one=3, fu_ben_time=2, extra_time=30)
            # SPlay.hui_shou_full()
            SPlay.ge_ren_boss(5)
            # SPlay.hui_shou_full()
            SPlay.ta_fang_feng_mo(3)
            sui_shi_ya_biao()
            SPlay.wei_wang_ren_wu()
            SPlay.chu_mo_ren_wu(25, False)
            lin_qu_huo_yue_jiang_li()
            lian_gong(45)
            SPlay.gua_ji(hh=10, mm=0, ss=0)
            time.sleep(1)
            fu_li_da_ting()
            AW1.jue_xing()

if __name__ == '__main__':
    myrun = running()
    myrun.mainrun()