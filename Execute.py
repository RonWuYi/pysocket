import logging.config
import time
import pyautogui

from Package.renwu import BASICFUNCTIONRW
from Package.richang import BASICFUNCTIONRC
from datetime import datetime as sm
from Package.util import go_feng_mo_npc, huo_dong_jie_mian, xiao_chu_jie_mian, customize_init, go_wei_wang_npc, \
    go_gua_ji_npc, current_date_time, bao_wu_shen_dun_jie_mian, bao_wu_jie_mian, go_to, lian_gong, go_chu_mo_npc, \
    seconds_change, boss_hui_shou, yin_xiong_jie_mian

logging.config.fileConfig('C:\\Work\\pysocket\\log\\logging.conf')
logging.basicConfig(filename='/home/hdc/Downloads/github/pysocket/log/{}.log'.format(str(sm.today())[:16]),level=logging.DEBUG)
logger = logging.getLogger('simple_example')

pyautogui.PAUSE = 1.5
GongXunTime = 120
JinYinTime = 160
cai_liao_move_value = 30
ge_ren_boss_time = 19


class GONGXUN(BASICFUNCTIONRW):
    def function(self, run_times=10, wait_time=100, extra_time=0, ge_su=3):
        logger.info("Start GongXunRenWu at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'JinYanGongXun'

        bao_wu_jie_mian(ge_su)
        time.sleep(1)
        pyautogui.click(793, 583)

        for i in range(run_times):

            time.sleep(1)
            pyautogui.click(622, 527)
            time.sleep(8)

            # jie shou ren wu
            pyautogui.click(509, 567)
            time.sleep(1)

            # qian wang wan cheng ren wu
            pyautogui.click(509, 567)

            # deng dai wan cheng
            time.sleep(wait_time+extra_time)

            # dian ji di mian (fang zi wa kuang cuo wo)
            # click chuan
            time.sleep(1)
            pyautogui.click(793, 583)

            # wan cheng ren wu - san bei jiang li
            time.sleep(2)
            pyautogui.click(610, 511)
            time.sleep(1)

            logger.info("GongXunRenWu complete at {}".format(current_date_time()))
        customize_init()
        self.GongXunRenWuComplete = True


class JINGYING(BASICFUNCTIONRW):
    def function(self, run_times=10,
                         wait_time=100, extra_time=0, ge_su=4):
        logger.info("Start JingYingRenWu at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'TianFu'

        yin_xiong_jie_mian(ge_su)

        for j in range(run_times):
            time.sleep(1)
            pyautogui.click(509, 567)
            time.sleep(1)
            pyautogui.click(509, 567)
            time.sleep(wait_time+extra_time)

            time.sleep(1)
            pyautogui.click(628, 206)
            time.sleep(1)

            time.sleep(1)
            pyautogui.click(613, 510)
            time.sleep(1)

        logger.info("JingYingRenWu complete at {}".format(current_date_time()))
        customize_init()
        self.JingYingRenWuComplete = True


class TAFANG(BASICFUNCTIONRW):
    def __init__(self, feng_mo_time):
        self.feng_mo_time = feng_mo_time
        super(TAFANG, self).__init__()

    def function(self):
        logger.info("Start TaFangFengMo at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'TaFangFengMo'

        # self._BaoWuShenDunJieMian()
        for jj in range(self.feng_mo_time):
            go_feng_mo_npc()
            time.sleep(6)
            # jin ru feng mo gu
            time.sleep(1)
            pyautogui.click(506, 592)

            # xiao chu jie mian
            time.sleep(1)
            pyautogui.press('esc')

            time.sleep(1)
            pyautogui.press('esc')

            # kai shi shua guai
            time.sleep(1)
            pyautogui.click(701, 458)

            for ii in range(2):
                # dian
                pyautogui.click(322, 456)

                # dao lu dian ji dian, ren wu qian jin
                pyautogui.click(765, 359, button='right', clicks=1)

                # du
                pyautogui.click(414, 456)

                # dao lu dian ji dian, ren wu qian jin
                pyautogui.click(765, 359, button='right', clicks=1)

                # bin
                pyautogui.click(509, 456)

                # dao lu dian ji dian, ren wu qian jin
                pyautogui.click(765, 359, button='right', clicks=1)

                # bao
                pyautogui.click(605, 456)

                # dao lu dian ji dian, ren wu qian jin
                pyautogui.click(765, 359, button='right', clicks=1)

            # deng dai jie shu
            time.sleep(420)

            # lin qu jiang li
            time.sleep(5)
            pyautogui.click(606, 382)

        logger.info("TaFangFengMo Complete at {}".format(current_date_time()))
        customize_init()
        self.TaFangFengMoComplete = True


class TIANGUAN(BASICFUNCTIONRW):
    def function(self, extra_time=0):
        logger.info("Start ChuangTianGuan at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'ChuangTianGuan'

        time.sleep(1)

        go_gua_ji_npc()

        time.sleep(1)
        pyautogui.click(1013, 632)
        time.sleep(5)

        time.sleep(1)
        pyautogui.click(507, 600)
        if self.zhuan_shen_level == 0:
            time.sleep(190 + extra_time)
        elif self.zhuan_shen_level == 1:
            time.sleep(230 + extra_time)
        elif self.zhuan_shen_level == 2:
            time.sleep(430 + extra_time)
        elif self.zhuan_shen_level == 3:
            time.sleep(600 + extra_time)
        elif self.zhuan_shen_level == 4:
            time.sleep(790 + extra_time)
        elif self.zhuan_shen_level == 5:
            time.sleep(860 + extra_time)
        elif self.zhuan_shen_level == 6:
            time.sleep(960 + extra_time)
        else:
            time.sleep(1500 + extra_time)
        pyautogui.click(511, 514)
        logger.info("ChuangTianGuan Complete at {}".format(current_date_time()))
        customize_init()
        self.ChuangTianGuanComplete = True


class CAILIAO(BASICFUNCTIONRW):
    def function(self, fu_ben_time=2,
                        which_one=7, basic_time=75, extra_time=0):
        logger.info("Start CaiLiaoFuBen at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'CaiLiaoFuBen'
        time.sleep(1)
        bao_wu_shen_dun_jie_mian()
        for i in range(fu_ben_time):
            if which_one == 1:
                for j in [1]:
                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (j * cai_liao_move_value)))
                    time.sleep(1)
                    pyautogui.click(499, 583)

                    # zi dong zhan dou
                    time.sleep(1)
                    pyautogui.press('z')
                    if j < 3:
                        time.sleep(10+basic_time+extra_time)
                    elif j == 3:
                        time.sleep(35+basic_time+extra_time)
                    elif j == 4:
                        time.sleep(195+basic_time+extra_time)
                    elif j == 5:
                        time.sleep(basic_time+extra_time)
                    elif j == 6:
                        time.sleep(55+basic_time+extra_time)
                    else:
                        time.sleep(50+basic_time+extra_time)
                    boss_hui_shou()
                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            elif which_one == 2:
                for j in [1, 4]:
                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (j * cai_liao_move_value)))

                    time.sleep(1)
                    pyautogui.click(499, 583)

                    # zi dong zhan dou
                    time.sleep(1)
                    pyautogui.press('z')
                    if j < 3:
                        time.sleep(10+basic_time+extra_time)
                    elif j == 3:
                        time.sleep(35+basic_time+extra_time)
                    elif j == 4:
                        time.sleep(195+basic_time+extra_time)
                    elif j == 5:
                        time.sleep(basic_time+extra_time)
                    elif j == 6:
                        time.sleep(55+basic_time+extra_time)
                    else:
                        time.sleep(50+basic_time+extra_time)
                    boss_hui_shou()
                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            elif which_one == 3:
                for j in [1, 4, 6]:
                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (j * cai_liao_move_value)))

                    time.sleep(1)
                    pyautogui.click(499, 583)

                    # zi dong zhan dou
                    time.sleep(1)
                    pyautogui.press('z')
                    if j < 3:
                        time.sleep(10+basic_time+extra_time)
                    elif j == 3:
                        time.sleep(35+basic_time+extra_time)
                    elif j == 4:
                        time.sleep(195+basic_time+extra_time)
                    elif j == 5:
                        time.sleep(basic_time+extra_time)
                    elif j == 6:
                        time.sleep(55+basic_time+extra_time)
                    else:
                        time.sleep(50+basic_time+extra_time)
                    boss_hui_shou()
                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            elif which_one == 4:
                for j in [1, 4, 5, 6]:
                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (j * cai_liao_move_value)))

                    time.sleep(1)
                    pyautogui.click(499, 583)

                    # zi dong zhan dou
                    time.sleep(1)
                    pyautogui.press('z')
                    if j < 3:
                        time.sleep(10+basic_time+extra_time)
                    elif j == 3:
                        time.sleep(35+basic_time+extra_time)
                    elif j == 4:
                        time.sleep(195+basic_time+extra_time)
                    elif j == 5:
                        time.sleep(basic_time+extra_time)
                    elif j == 6:
                        time.sleep(55+basic_time+extra_time)
                    else:
                        time.sleep(50+basic_time+extra_time)
                    boss_hui_shou()
                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            else:
                for j in range(0, 7):
                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (j * cai_liao_move_value)))

                    time.sleep(1)
                    pyautogui.click(499, 583)

                    # zi dong zhan dou
                    time.sleep(1)
                    pyautogui.press('z')
                    if j < 3:
                        time.sleep(10+basic_time+extra_time)
                    elif j == 3:
                        time.sleep(35+basic_time+extra_time)
                    elif j == 4:
                        time.sleep(195+basic_time+extra_time)
                    elif j == 5:
                        time.sleep(basic_time+extra_time)
                    elif j == 6:
                        time.sleep(55+basic_time+extra_time)
                    else:
                        time.sleep(50+basic_time+extra_time)
                    boss_hui_shou()
                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)

            # self.hui_shou_full()
        logger.info("CaiLiaoFuBen Complete at {}".format(current_date_time()))
        customize_init()
        self.CaiLiaoFuBenComplete = True


class WEIWANG(BASICFUNCTIONRW):
    def function(self):
        logger.info("Start WeiWangRenWu at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'WeiWangRenWu'

        go_wei_wang_npc()

        # ############ task 1 #########################################
        # click ren wu ming cheng
        time.sleep(1)
        pyautogui.click(322, 258)
        time.sleep(1)

        # jie shou xuan shang
        pyautogui.click(645, 525)
        time.sleep(1)

        # chuan
        pyautogui.click(684, 488)
        time.sleep(1)

        pyautogui.press('esc')
        time.sleep(1)
        # shou ji 1
        pyautogui.click(533, 399)
        time.sleep(22)

        # shou ji 2
        pyautogui.click(547, 307)
        time.sleep(22)

        # shou ji 3
        pyautogui.click(451, 403)
        time.sleep(22)

        # shou ji 4
        pyautogui.click(450, 317)
        time.sleep(22)

        # wan cheng ren wu dian chuan
        go_wei_wang_npc()

        # wan cheng ren wu
        pyautogui.click(645, 526)
        time.sleep(1)

        # task 2
        # jie qu ren wu
        pyautogui.click(327, 307)
        time.sleep(1)
        pyautogui.click(645, 525)
        time.sleep(1)

        pyautogui.click(709, 490)
        time.sleep(1)

        pyautogui.press('esc')
        time.sleep(1)
        # deng dai wan cheng
        time.sleep(50)

        # chuan
        go_wei_wang_npc()
        # wan cheng ren wu
        pyautogui.click(645, 526)
        time.sleep(1)

        # task 3
        # ri chang ren wu
        time.sleep(1)
        pyautogui.click(335, 402)
        time.sleep(1)
        # jie shou xuan shang
        pyautogui.click(645, 525)
        time.sleep(1)
        pyautogui.click(696, 489)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        # deng dai wan cheng
        time.sleep(50)

        # chuan
        go_wei_wang_npc()

        # wan cheng ren wu
        pyautogui.click(645, 526)
        time.sleep(2)

        # task 4
        pyautogui.click(334, 452)

        # jie qu ren wu
        time.sleep(1)
        pyautogui.click(645, 525)
        time.sleep(1)
        pyautogui.click(684, 487)
        pyautogui.press('esc')
        time.sleep(1)
        time.sleep(35)

        # chuan
        go_wei_wang_npc()

        # wan cheng ren wu
        pyautogui.click(645, 526)
        time.sleep(2)

        # lin qu jiang li
        pyautogui.click(336, 600)
        time.sleep(2)
        pyautogui.click(450, 600)
        time.sleep(2)
        pyautogui.click(566, 600)
        time.sleep(2)

        pyautogui.press('esc')
        logger.info("WeiWangRenWu complete at {}".format(current_date_time()))
        customize_init()
        self.WeiWangRenWuComplete = True


class CHUMO(BASICFUNCTIONRW):
    def __init__(self, chu_mo_time, go_to_true):
        self.chu_mo_time = chu_mo_time
        self.go_to_true = go_to_true
        super(CHUMO, self).__init__()

    def function(self):
        logger.info("Start ChuMoRenWu at {}".format(current_date_time()))

        # chuan dao Zhang TianShi
        go_chu_mo_npc()

        # jin ru jiang jun mu
        time.sleep(2)
        pyautogui.click(544, 497)
        time.sleep(1)

        pyautogui.press('esc')
        time.sleep(2)
        if self.go_to_true:
            go_to(63, 25)
            # da pai zi
            time.sleep(10)
            xiao_chu_jie_mian()
            pyautogui.press('z')
            time.sleep(self.chu_mo_time*60)
        else:
            xiao_chu_jie_mian()
            pyautogui.press('z')
            time.sleep(self.chu_mo_time*60)
        customize_init()
        go_chu_mo_npc()
        for i in range(5):
            time.sleep(1)
            pyautogui.click(551, 571)
        time.sleep(1)
        pyautogui.press('esc')
        logger.info("ChuMoRenWu complete at {}".format(current_date_time()))
        customize_init()
        self.ChuMoRenWuComplete = True


class PRIVATEBOSS(BASICFUNCTIONRW):
    def __init__(self, extra_time=0):
        self.extra_time = extra_time
        super(PRIVATEBOSS, self).__init__()

    def function(self):
        logger.info("Start GeRenBoss at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'GeRenBoss'

        if self.zhuan_shen_level == 0:
            for i in range(3):
                # ge ren boss
                bao_wu_jie_mian(2)
                time.sleep(1)
                pyautogui.click(792, 595)

                time.sleep(1)
                pyautogui.click(348, 198)

                # boss ming zi
                time.sleep(1)
                pyautogui.click(261, (255 + (i * 40)))
                time.sleep(1)
                pyautogui.click(785, 617)
                time.sleep(0.5)
                pyautogui.press('z')
                time.sleep(1)
                if i == 0:
                    time.sleep(35 + (i * 15) + self.extra_time)
                elif i == 1:
                    time.sleep(50 + (i * 15) + self.extra_time)
                else:
                    time.sleep(70 + (i * 15) + self.extra_time)
                time.sleep(1)
                boss_hui_shou()
                time.sleep(1)
                pyautogui.click(859, 533)
        elif 0 < self.zhuan_shen_level <= 2:
            for i in range(4):
                # ge ren boss
                bao_wu_jie_mian(2)
                time.sleep(1)
                pyautogui.click(792, 595)

                time.sleep(1)
                pyautogui.click(348, 198)

                # boss ming zi
                time.sleep(1)
                pyautogui.click(261, (255 + (i * 40)))
                time.sleep(1)
                pyautogui.click(785, 617)
                time.sleep(0.5)
                pyautogui.press('z')
                time.sleep(1)
                if i == 0:
                    time.sleep(35 + (i * ge_ren_boss_time) + self.extra_time)
                elif i == 1:
                    time.sleep(50 + (i * ge_ren_boss_time) + self.extra_time)
                elif i == 2:
                    time.sleep(70 + (i * ge_ren_boss_time) + self.extra_time)
                else:
                    time.sleep(90 + (i * ge_ren_boss_time) + self.extra_time)
                time.sleep(1)
                boss_hui_shou()
                time.sleep(1)
                pyautogui.click(859, 533)
        elif 2 < self.zhuan_shen_level <= 4:
            for i in range(5):
                # ge ren boss
                bao_wu_jie_mian(2)
                time.sleep(1)
                pyautogui.click(792, 595)

                time.sleep(1)
                pyautogui.click(348, 198)

                # boss ming zi
                time.sleep(1)
                pyautogui.click(261, (255 + (i * 40)))
                time.sleep(1)
                pyautogui.click(785, 617)
                time.sleep(0.5)
                pyautogui.press('z')
                time.sleep(1)
                if i == 0:
                    time.sleep(35 + (i * ge_ren_boss_time) + self.extra_time)
                elif i == 1:
                    time.sleep(45 + (i * ge_ren_boss_time) + self.extra_time)
                elif i == 2:
                    time.sleep(55 + (i * ge_ren_boss_time) + self.extra_time)
                elif i == 3:
                    time.sleep(70 + (i * ge_ren_boss_time) + self.extra_time)
                else:
                    time.sleep(80 + (i * ge_ren_boss_time) + self.extra_time)
                time.sleep(1)
                boss_hui_shou()
                time.sleep(1)
                pyautogui.click(859, 533)
        else:
            for i in range(6):
                # ge ren boss
                bao_wu_jie_mian(2)
                time.sleep(1)
                pyautogui.click(792, 595)

                time.sleep(1)
                pyautogui.click(348, 198)

                # boss ming zi
                time.sleep(1)
                pyautogui.click(261, (255 + (i * 40)))
                time.sleep(1)
                pyautogui.click(785, 617)
                time.sleep(0.5)
                pyautogui.press('z')
                time.sleep(1)
                if i == 0:
                    time.sleep(35 + (i * ge_ren_boss_time) + self.extra_time)
                elif i == 1:
                    time.sleep(45 + (i * ge_ren_boss_time) + self.extra_time)
                elif i == 2:
                    time.sleep(60 + (i * ge_ren_boss_time) + self.extra_time)
                elif i == 3:
                    time.sleep(70 + (i * ge_ren_boss_time) + self.extra_time)
                elif i == 4:
                    time.sleep(90 + (i * ge_ren_boss_time) + self.extra_time)
                else:
                    time.sleep(100 + (i * ge_ren_boss_time) + self.extra_time)
                time.sleep(1)
                boss_hui_shou()
                time.sleep(1)
                pyautogui.click(859, 533)
        logger.info("GeRenBoss complete at {}".format(current_date_time()))
        customize_init()
        self.GeRenBossiComplete = True


class RIMOBAI(BASICFUNCTIONRC):
    def function(self):
        logger.info("Start MoBaiChengZhu at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'MoBaiChengZhu'

        time.sleep(1)
        huo_dong_jie_mian()
        pyautogui.click(701, 458)

        for i in range(10):
            time.sleep(1)
            for j in range(4):
                time.sleep(0.5)
                pyautogui.click(582, 598)
                time.sleep(0.1)
                pyautogui.click(582, 598)
                time.sleep(0.1)
                pyautogui.click(582, 598)
                time.sleep(0.1)
            time.sleep(0.5)
            pyautogui.click(797, 520)
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(0.5)
        pyautogui.press('r')
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(0.5)
        pyautogui.press('r')
        logger.info("MoBaiChengZhu complete at {}".format(current_date_time()))
        customize_init()
        self.MoBaiChengZhuComplete = True


class RIYEZHAN(BASICFUNCTIONRC):
    def function(self):
        logger.info("Start YeZhanBiQi at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'YeZhanBiQi'

        huo_dong_jie_mian()

        pyautogui.click(508, 609)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1200)
        logger.info("YeZhanBiQi complete at {}".format(current_date_time()))
        customize_init()
        self.YeZhanBiQiComplete = True


class RIWORLDBOSS(BASICFUNCTIONRC):
    def function(self):
        logger.info("Start WorldBoss at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'WorldBoss'

        time.sleep(1)
        huo_dong_jie_mian()
        pyautogui.click(510, 598)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(2000)

        # jia bei
        for i in range(10):
            pyautogui.click(454, 548)
            time.sleep(1)
        # pyautogui.press('e')
        logger.info("WorldBoss complete at {}".format(current_date_time()))
        customize_init()
        self.WorldBossComplete = True


class RIJINZHU(BASICFUNCTIONRC):
    def function(self):
        logger.info("Start JinZhuSongLi at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'JinZhuSongLi'

        huo_dong_jie_mian()

        # can yu huo dong
        time.sleep(2)
        pyautogui.click(508, 596)

        time.sleep(1)
        pyautogui.rightClick(949, 699)

        time.sleep(1)
        pyautogui.press('z')

        time.sleep(300)
        logger.info("JinZhuSongLi complete at {}".format(current_date_time()))
        customize_init()


class RISHENWEI(BASICFUNCTIONRC):
    def __init__(self, shen_wei_time):
        self.shen_wei_time =shen_wei_time
        super(RISHENWEI, self).__init__()

    def function(self):
        logger.info("Start ShenWei at {}".format(current_date_time()))

        huo_dong_jie_mian()
        time.sleep(0.5)
        # jin ru shen wei
        pyautogui.click(510, 607)
        time.sleep(1)

        xiao_chu_jie_mian()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(self.Seconds*self.shen_wei_time)
        for i in range(10):
            if i == 6:
                pyautogui.click(889, 578)
                time.sleep(5)
                pyautogui.click(889, 578)
                time.sleep(68)
                pyautogui.click(511, 600)
            else:
                pyautogui.click(889, 578)
                time.sleep(5)
                pyautogui.click(889, 578)
                time.sleep(52)
                pyautogui.click(511, 600)
        # li kai
        time.sleep(1)
        pyautogui.click(911, 566)
        # que ding
        time.sleep(1)
        pyautogui.click(448, 455)
        logger.info("ShenWei complete at {}".format(current_date_time()))
        customize_init()
        self.ShenWeiComplete = True


class RIBIGUAN(BASICFUNCTIONRC):
    def function(self):
        logger.info("Start BiGuan at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'BiGuan'

        time.sleep(1)
        huo_dong_jie_mian()
        pyautogui.click(509, 609)

        # xiao chu jie mian
        xiao_chu_jie_mian()

        # To do, improve it
        # di tu
        time.sleep(1)
        pyautogui.press('m')

        if self.zhuan_shen_level == 0:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(612, 192)
            time.sleep(1)
            pyautogui.typewrite('26')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(710, 192)
            time.sleep(1)
            pyautogui.typewrite('34')
        elif 0 < self.zhuan_shen_level <= 2:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(613, 192)
            time.sleep(1)
            pyautogui.typewrite('26')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(713, 192)
            time.sleep(1)
            pyautogui.typewrite('34')

        elif 2 < self.zhuan_shen_level <= 4:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(613, 192)
            time.sleep(1)
            pyautogui.typewrite('26')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(713, 192)
            time.sleep(1)
            pyautogui.typewrite('34')

        elif 4 < self.zhuan_shen_level <= 6:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(613, 192)
            time.sleep(1)
            pyautogui.typewrite('26')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(713, 192)
            time.sleep(1)
            pyautogui.typewrite('34')

        else:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(613, 192)
            time.sleep(1)
            pyautogui.typewrite('22')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(713, 192)
            time.sleep(1)
            pyautogui.typewrite('30')

        # qian wang di dian
        time.sleep(1)
        pyautogui.click(770, 192)

        # zai ci dian ji
        time.sleep(1)
        pyautogui.click(770, 192)
        time.sleep(1200)

        time.sleep(1)
        pyautogui.press('esc')
        logger.info("BiGuan complete at {}".format(current_date_time()))
        customize_init()
        # flag
        self.BiGuanComplete = True


class RIGUAIWUGONGCHENG(BASICFUNCTIONRC):
    def function(self):
        logger.info("Start GuaiWuGongCheng at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'GuaiWuGongCheng'

        time.sleep(1)

        # self._HuoDongJieMian()
        bao_wu_jie_mian(5)

        # Qian Wang
        pyautogui.click(793, 581)
        time.sleep(1)

        # can yu huo dong
        pyautogui.click(509, 596)
        time.sleep(1)

        # _huo_dong_jie_mian()
        # time.sleep(1)
        #
        # pyautogui.click(508, 609)
        # time.sleep(1)

        # su ji
        pyautogui.click(679, 728)
        time.sleep(1)

        xiao_chu_jie_mian()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1750)
        logger.info("GuaiWuGongCheng complete at {}".format(current_date_time()))
        customize_init()
        self.GuaiWuGongChengComplete = True


class RISUOYAOTA(BASICFUNCTIONRC):
    def function(self):
        logger.info("Start RiSuoYaoTa at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'RiSuoYaoTa'

        time.sleep(1)

        huo_dong_jie_mian()
        pyautogui.click(510, 396)
        # gua ji ban ge xiao shi
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1750)
        logger.info("RiSuoYaoTa complete at {}".format(current_date_time()))
        customize_init()
        self.SuoYaoTaComplete = True


class RIYASONG(BASICFUNCTIONRC):
    def function(self):
        logger.info("Start RiDuoBeiYaSong at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'RiDuoBeiYaSong'

        time.sleep(1)

        for ii in range(3):
            bao_wu_jie_mian(3)

            # qian wang
            time.sleep(1)
            pyautogui.click(793, 551)

            # jie qu ren wu
            time.sleep(1)
            pyautogui.click(509, 582)

            # shua xin
            for i in range(10):
                time.sleep(1)
                pyautogui.click(649, 551)
            # hu song
            time.sleep(1)
            pyautogui.click(936, 550)

            if ii == 0:
                time.sleep(45)
            else:
                time.sleep(165)

            # que ding
            time.sleep(1)
            pyautogui.click(581, 502)

        logger.info("RiDuoBeiYaSong complete at {}".format(current_date_time()))
        customize_init()
        self.DuoBeiYaSongComplete = True


class RILIANGONG(BASICFUNCTIONRC):
    def __init__(self, lian_gong_time):
        self.lian_gong_time = lian_gong_time
        super(RILIANGONG, self).__init__()

    def function(self):
        logger.info("Start SanBeiLianGong at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'SanBeiLianGong'

        lian_gong(self.lian_gong_time)
        logger.info("SanBeiLianGong complete at {}".format(current_date_time()))
        customize_init()
        self.SanBeiLianGongComplete = True


class RIJIALANSHENDIAN(BASICFUNCTIONRC):
    def __init__(self, jia_lan_time):
        self.jia_lan_time = jia_lan_time
        super(RIJIALANSHENDIAN, self).__init__()

    def function(self):
        logger.info("Start JiaLanShenDian at {}".format(current_date_time()))

        time.sleep(1)

        huo_dong_jie_mian()
        pyautogui.click(510, 599)
        time.sleep(1)

        xiao_chu_jie_mian()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(self.jia_lan_time)
        logger.info("JiaLanShenDian complete at {}".format(current_date_time()))
        customize_init()
        self.JiaLanShenDianComplete = True


class RIHAITIAN(BASICFUNCTIONRC):
    # To Do
    def ri_hai_tian_sheng_yan(self):
        logger.info("Start HaiTianShengYan at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'HaiTianShengYan'

        time.sleep(1)

        huo_dong_jie_mian()
        pyautogui.click(508, 607)
        time.sleep(1)
        xiao_chu_jie_mian()
        pyautogui.press('z')
        time.sleep(900)

        # NPC part and delay part
        logger.info("HaiTianShengYan complete at {}".format(current_date_time()))
        customize_init()
        self.HaiTianShengYanComplete = True


class RISHIMU(BASICFUNCTIONRC):
    def ri_shi_mu(self):
        logger.info("Start ShiMuMiZhen at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'RiShiMuMiZhen'

        time.sleep(1)

        huo_dong_jie_mian()

        # Jin ru huo dong
        time.sleep(0.5)
        pyautogui.click(510, 599)
        time.sleep(10)
        # ToDo
        # NPC part and delay part
        logger.info("ShiMuMiZhen complete at {}".format(current_date_time()))
        customize_init()
        self.ShiMuMiZhenComplete = True


class RIDATI(BASICFUNCTIONRC):
    def function(self):
        logger.info("Start DaTi at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'RiDaTi'

        time.sleep(1)

        huo_dong_jie_mian()

        # Jin ru huo dong
        time.sleep(0.5)
        pyautogui.click(509, 581)
        time.sleep(900)
        # ToDo
        # NPC part and delay part
        logger.info("DaTi complete at {}".format(current_date_time()))
        customize_init()
        self.DaTi = True


class BANGHUI(BASICFUNCTIONRC):
    def function(self):
        logger.info("Start BangHui at {}".format(current_date_time()))
        self.GuaJiFlag = False
        self.CurStatus = 'BangHui'
        # self.EventTime += 1
        time.sleep(1)

        # Jin ru huo dong
        time.sleep(1)
        pyautogui.click(854, 685)

        time.sleep(1)
        pyautogui.click(373, 202)

        time.sleep(1)
        pyautogui.click(503, 561)

        time.sleep(1)
        pyautogui.click(507, 581)
        time.sleep(1)
        pyautogui.click(508, 621)
        time.sleep(600)

        logger.info("DaTi complete at {}".format(current_date_time()))
        customize_init()
        self.DaTi = True


class WAKUANG(BASICFUNCTIONRC):
    # ToDo imporve it
    def wa_kuang(self, wa_kuang_time):
        logger.info("Start WaKuang at {}".format(current_date_time()))
        self.GuaJiFlag = True
        self.CurStatus = 'WaKuang'

        time.sleep(wa_kuang_time*self.Seconds)
        pyautogui.click(1220, 611)
        time.sleep(1)
        logger.info("WaKuang Complete at {}".format(current_date_time()))
        customize_init()


class GUAJI(BASICFUNCTIONRC):
    def gua_ji(self, hh, mm=0, ss=0):
        logger.info("Start Guaji at {}".format(current_date_time()))
        self.GuaJiFlag = True
        self.CurStatus = 'GuaJi'

        go_gua_ji_npc()
        time.sleep(1)
        if self.CurrentLevel > 80:
            if self.zhuan_shen_level == 0:
                pyautogui.click(394, 418)
            elif self.zhuan_shen_level == 1:
                pyautogui.click(493, 419)
            elif self.zhuan_shen_level == 2:
                pyautogui.click(595, 418)
            elif self.zhuan_shen_level == 3:
                pyautogui.click(595, 418)
            elif self.zhuan_shen_level == 4:
                pyautogui.click(393, 449)
            else:
                pyautogui.click(494, 446)
        else:
            pyautogui.click(593, 390)

        # sui ji
        time.sleep(1)
        pyautogui.click(678, 728)
        time.sleep(1)
        xiao_chu_jie_mian()
        pyautogui.press('z')

        logger.info("GuaJi shijian is ", seconds_change(self._time_diff(hh, mm, ss)))
        time.sleep(self._time_diff(hh, mm, ss))
        logger.info("GuaJi complete at {}".format(current_date_time()))
        customize_init()

# class AW1(object):

    # def __init__(self, current_zhuan_shen, current_level=81):
    #     self.CurrentLevel = current_level
    #     self.zhuan_shen_level = current_zhuan_shen
    #     self.GuaJiFlag = True
    #     self.CurStatus = 'null'
    #     self.Complete = False
    #     # self.EventTime = 0
    #     self.Seconds = 60
    #     self.GongXunRenWuComplete = False
    #     self.JingYingRenWuComplete = False
    #     self.WeiWangRenWuComplete = False
    #     self.TaFangFengMoComplete = False
    #     self.CaiLiaoFuBenComplete = False
    #     self.ChuMoRenWuComplete = False
    #     self.ChuangTianGuanComplete = False
    #     self.MoBaiChengZhuComplete = False
    #     self.YeZhanBiQiComplete = False
    #     self.ShenWeiComplete = False
    #     self.WorldBossComplete = False
    #     self.JinZhuSongLiComplete = False
    #     self.YeZhanBiQiComplete = False
    #     self.GeRenBossiComplete = False
    #     self.GuaiWuGongChengComplete = False
    #     self.BiGuanComplete = False
    #     self.SuoYaoTaComplete = False
    #     self.DuoBeiYaSongComplete = False
    #     self.HaiTianShengYanComplete = False
    #     self.JiaLanShenDianComplete = False
    #     self.SanBeiLianGongComplete = False
    #     self.ShiMuMiZhenComplete = False
    #     self.DaTi = False
    #     self.x, self.y = pyautogui.size()
    #
    #     self.Y = str(sm.now())[0:4]
    #     self.M = str(sm.now())[5:7]
    #     self.D = str(sm.now())[8:10]

    # useless

    # def jing_ying_ren_wu(self, run_times=10,
    #                      wait_time=100, extra_time=0, ge_su=4):
    #     logger.info("Start JingYingRenWu at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'TianFu'
    #
    #     _yin_xiong_jie_mian(ge_su)
    #
    #     for j in range(run_times):
    #         time.sleep(1)
    #         pyautogui.click(509, 567)
    #         time.sleep(1)
    #         pyautogui.click(509, 567)
    #         time.sleep(wait_time+extra_time)
    #
    #         time.sleep(1)
    #         pyautogui.click(628, 206)
    #         time.sleep(1)
    #
    #         time.sleep(1)
    #         pyautogui.click(613, 510)
    #         time.sleep(1)
    #
    #     logger.info("JingYingRenWu complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.JingYingRenWuComplete = True

    # def ta_fang_feng_mo(self, feng_mo_time):
    #     logger.info("Start TaFangFengMo at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'TaFangFengMo'
    #
    #     # self._BaoWuShenDunJieMian()
    #     for jj in range(feng_mo_time):
    #         _go_feng_mo_npc()
    #         time.sleep(6)
    #         # jin ru feng mo gu
    #         time.sleep(1)
    #         pyautogui.click(506, 592)
    #
    #         # xiao chu jie mian
    #         time.sleep(1)
    #         pyautogui.press('esc')
    #
    #         time.sleep(1)
    #         pyautogui.press('esc')
    #
    #         # kai shi shua guai
    #         time.sleep(1)
    #         pyautogui.click(701, 458)
    #
    #         for ii in range(2):
    #             # dian
    #             pyautogui.click(322, 456)
    #
    #             # dao lu dian ji dian, ren wu qian jin
    #             pyautogui.click(765, 359, button='right', clicks=1)
    #
    #             # du
    #             pyautogui.click(414, 456)
    #
    #             # dao lu dian ji dian, ren wu qian jin
    #             pyautogui.click(765, 359, button='right', clicks=1)
    #
    #             # bin
    #             pyautogui.click(509, 456)
    #
    #             # dao lu dian ji dian, ren wu qian jin
    #             pyautogui.click(765, 359, button='right', clicks=1)
    #
    #             # bao
    #             pyautogui.click(605, 456)
    #
    #             # dao lu dian ji dian, ren wu qian jin
    #             pyautogui.click(765, 359, button='right', clicks=1)
    #
    #         # deng dai jie shu
    #         time.sleep(420)
    #
    #         # lin qu jiang li
    #         time.sleep(5)
    #         pyautogui.click(606, 382)
    #
    #     logger.info("TaFangFengMo Complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.TaFangFengMoComplete = True

    # def chuang_tian_guan(self, extra_time=0):
    #     logger.info("Start ChuangTianGuan at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'ChuangTianGuan'
    #
    #     time.sleep(1)
    #
    #     _go_gua_ji_npc()
    #
    #     time.sleep(1)
    #     pyautogui.click(1013, 632)
    #     time.sleep(5)
    #
    #     time.sleep(1)
    #     pyautogui.click(507, 600)
    #     if self.zhuan_shen_level == 0:
    #         time.sleep(190 + extra_time)
    #     elif self.zhuan_shen_level == 1:
    #         time.sleep(230 + extra_time)
    #     elif self.zhuan_shen_level == 2:
    #         time.sleep(430 + extra_time)
    #     elif self.zhuan_shen_level == 3:
    #         time.sleep(600 + extra_time)
    #     elif self.zhuan_shen_level == 4:
    #         time.sleep(790 + extra_time)
    #     elif self.zhuan_shen_level == 5:
    #         time.sleep(860 + extra_time)
    #     elif self.zhuan_shen_level == 6:
    #         time.sleep(960 + extra_time)
    #     else:
    #         time.sleep(1500 + extra_time)
    #     pyautogui.click(511, 514)
    #     logger.info("ChuangTianGuan Complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.ChuangTianGuanComplete = True
    #
    # def cai_liao_fu_ben(self, fu_ben_time=2,
    #                     which_one=7, basic_time=75, extra_time=0):
    #     logger.info("Start CaiLiaoFuBen at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'CaiLiaoFuBen'
    #     time.sleep(1)
    #     _bao_wu_shen_dun_jie_mian()
    #     for i in range(fu_ben_time):
    #         if which_one == 1:
    #             for j in [1]:
    #                 # dian ji NPC
    #                 time.sleep(1)
    #                 pyautogui.click(604, 359)
    #                 time.sleep(1)
    #                 pyautogui.click(514, (398 + (j * cai_liao_move_value)))
    #                 time.sleep(1)
    #                 pyautogui.click(499, 583)
    #
    #                 # zi dong zhan dou
    #                 time.sleep(1)
    #                 pyautogui.press('z')
    #                 if j < 3:
    #                     time.sleep(10+basic_time+extra_time)
    #                 elif j == 3:
    #                     time.sleep(35+basic_time+extra_time)
    #                 elif j == 4:
    #                     time.sleep(195+basic_time+extra_time)
    #                 elif j == 5:
    #                     time.sleep(basic_time+extra_time)
    #                 elif j == 6:
    #                     time.sleep(55+basic_time+extra_time)
    #                 else:
    #                     time.sleep(50+basic_time+extra_time)
    #                 _boss_hui_shou()
    #                 # li kai fu ben / mian fei lin qu jiang li
    #                 time.sleep(1)
    #                 pyautogui.click(860, 528)
    #         elif which_one == 2:
    #             for j in [1, 4]:
    #                 # dian ji NPC
    #                 time.sleep(1)
    #                 pyautogui.click(604, 359)
    #                 time.sleep(1)
    #                 pyautogui.click(514, (398 + (j * cai_liao_move_value)))
    #
    #                 time.sleep(1)
    #                 pyautogui.click(499, 583)
    #
    #                 # zi dong zhan dou
    #                 time.sleep(1)
    #                 pyautogui.press('z')
    #                 if j < 3:
    #                     time.sleep(10+basic_time+extra_time)
    #                 elif j == 3:
    #                     time.sleep(35+basic_time+extra_time)
    #                 elif j == 4:
    #                     time.sleep(195+basic_time+extra_time)
    #                 elif j == 5:
    #                     time.sleep(basic_time+extra_time)
    #                 elif j == 6:
    #                     time.sleep(55+basic_time+extra_time)
    #                 else:
    #                     time.sleep(50+basic_time+extra_time)
    #                 _boss_hui_shou()
    #                 # li kai fu ben / mian fei lin qu jiang li
    #                 time.sleep(1)
    #                 pyautogui.click(860, 528)
    #         elif which_one == 3:
    #             for j in [1, 4, 6]:
    #                 # dian ji NPC
    #                 time.sleep(1)
    #                 pyautogui.click(604, 359)
    #                 time.sleep(1)
    #                 pyautogui.click(514, (398 + (j * cai_liao_move_value)))
    #
    #                 time.sleep(1)
    #                 pyautogui.click(499, 583)
    #
    #                 # zi dong zhan dou
    #                 time.sleep(1)
    #                 pyautogui.press('z')
    #                 if j < 3:
    #                     time.sleep(10+basic_time+extra_time)
    #                 elif j == 3:
    #                     time.sleep(35+basic_time+extra_time)
    #                 elif j == 4:
    #                     time.sleep(195+basic_time+extra_time)
    #                 elif j == 5:
    #                     time.sleep(basic_time+extra_time)
    #                 elif j == 6:
    #                     time.sleep(55+basic_time+extra_time)
    #                 else:
    #                     time.sleep(50+basic_time+extra_time)
    #                 _boss_hui_shou()
    #                 # li kai fu ben / mian fei lin qu jiang li
    #                 time.sleep(1)
    #                 pyautogui.click(860, 528)
    #         elif which_one == 4:
    #             for j in [1, 4, 5, 6]:
    #                 # dian ji NPC
    #                 time.sleep(1)
    #                 pyautogui.click(604, 359)
    #                 time.sleep(1)
    #                 pyautogui.click(514, (398 + (j * cai_liao_move_value)))
    #
    #                 time.sleep(1)
    #                 pyautogui.click(499, 583)
    #
    #                 # zi dong zhan dou
    #                 time.sleep(1)
    #                 pyautogui.press('z')
    #                 if j < 3:
    #                     time.sleep(10+basic_time+extra_time)
    #                 elif j == 3:
    #                     time.sleep(35+basic_time+extra_time)
    #                 elif j == 4:
    #                     time.sleep(195+basic_time+extra_time)
    #                 elif j == 5:
    #                     time.sleep(basic_time+extra_time)
    #                 elif j == 6:
    #                     time.sleep(55+basic_time+extra_time)
    #                 else:
    #                     time.sleep(50+basic_time+extra_time)
    #                 _boss_hui_shou()
    #                 # li kai fu ben / mian fei lin qu jiang li
    #                 time.sleep(1)
    #                 pyautogui.click(860, 528)
    #         else:
    #             for j in range(0, 7):
    #                 # dian ji NPC
    #                 time.sleep(1)
    #                 pyautogui.click(604, 359)
    #                 time.sleep(1)
    #                 pyautogui.click(514, (398 + (j * cai_liao_move_value)))
    #
    #                 time.sleep(1)
    #                 pyautogui.click(499, 583)
    #
    #                 # zi dong zhan dou
    #                 time.sleep(1)
    #                 pyautogui.press('z')
    #                 if j < 3:
    #                     time.sleep(10+basic_time+extra_time)
    #                 elif j == 3:
    #                     time.sleep(35+basic_time+extra_time)
    #                 elif j == 4:
    #                     time.sleep(195+basic_time+extra_time)
    #                 elif j == 5:
    #                     time.sleep(basic_time+extra_time)
    #                 elif j == 6:
    #                     time.sleep(55+basic_time+extra_time)
    #                 else:
    #                     time.sleep(50+basic_time+extra_time)
    #                 _boss_hui_shou()
    #                 # li kai fu ben / mian fei lin qu jiang li
    #                 time.sleep(1)
    #                 pyautogui.click(860, 528)
    #
    #         # self.hui_shou_full()
    #     logger.info("CaiLiaoFuBen Complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.CaiLiaoFuBenComplete = True
    #
    # def wei_wang_ren_wu(self):
    #     logger.info("Start WeiWangRenWu at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'WeiWangRenWu'
    #
    #     _go_wei_wang_npc()
    #
    #     # ############ task 1 #########################################
    #     # click ren wu ming cheng
    #     time.sleep(1)
    #     pyautogui.click(322, 258)
    #     time.sleep(1)
    #
    #     # jie shou xuan shang
    #     pyautogui.click(645, 525)
    #     time.sleep(1)
    #
    #     # chuan
    #     pyautogui.click(684, 488)
    #     time.sleep(1)
    #
    #     pyautogui.press('esc')
    #     time.sleep(1)
    #     # shou ji 1
    #     pyautogui.click(533, 399)
    #     time.sleep(22)
    #
    #     # shou ji 2
    #     pyautogui.click(547, 307)
    #     time.sleep(22)
    #
    #     # shou ji 3
    #     pyautogui.click(451, 403)
    #     time.sleep(22)
    #
    #     # shou ji 4
    #     pyautogui.click(450, 317)
    #     time.sleep(22)
    #
    #     # wan cheng ren wu dian chuan
    #     _go_wei_wang_npc()
    #
    #     # wan cheng ren wu
    #     pyautogui.click(645, 526)
    #     time.sleep(1)
    #
    #     # task 2
    #     # jie qu ren wu
    #     pyautogui.click(327, 307)
    #     time.sleep(1)
    #     pyautogui.click(645, 525)
    #     time.sleep(1)
    #
    #     pyautogui.click(709, 490)
    #     time.sleep(1)
    #
    #     pyautogui.press('esc')
    #     time.sleep(1)
    #     # deng dai wan cheng
    #     time.sleep(50)
    #
    #     # chuan
    #     _go_wei_wang_npc()
    #     # wan cheng ren wu
    #     pyautogui.click(645, 526)
    #     time.sleep(1)
    #
    #     # task 3
    #     # ri chang ren wu
    #     time.sleep(1)
    #     pyautogui.click(335, 402)
    #     time.sleep(1)
    #     # jie shou xuan shang
    #     pyautogui.click(645, 525)
    #     time.sleep(1)
    #     pyautogui.click(696, 489)
    #     time.sleep(1)
    #     pyautogui.press('esc')
    #     time.sleep(1)
    #     # deng dai wan cheng
    #     time.sleep(50)
    #
    #     # chuan
    #     _go_wei_wang_npc()
    #
    #     # wan cheng ren wu
    #     pyautogui.click(645, 526)
    #     time.sleep(2)
    #
    #     # task 4
    #     pyautogui.click(334, 452)
    #
    #     # jie qu ren wu
    #     time.sleep(1)
    #     pyautogui.click(645, 525)
    #     time.sleep(1)
    #     pyautogui.click(684, 487)
    #     pyautogui.press('esc')
    #     time.sleep(1)
    #     time.sleep(35)
    #
    #     # chuan
    #     _go_wei_wang_npc()
    #
    #     # wan cheng ren wu
    #     pyautogui.click(645, 526)
    #     time.sleep(2)
    #
    #     # lin qu jiang li
    #     pyautogui.click(336, 600)
    #     time.sleep(2)
    #     pyautogui.click(450, 600)
    #     time.sleep(2)
    #     pyautogui.click(566, 600)
    #     time.sleep(2)
    #
    #     pyautogui.press('esc')
    #     logger.info("WeiWangRenWu complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.WeiWangRenWuComplete = True
    #
    # def chu_mo_ren_wu(self, chu_mo_time, go_to_true=True):
    #     logger.info("Start ChuMoRenWu at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'ChuMoRenWu'
    #
    #     # chuan dao Zhang TianShi
    #     go_chu_mo_npc()
    #
    #     # jin ru jiang jun mu
    #     time.sleep(2)
    #     pyautogui.click(544, 497)
    #     time.sleep(1)
    #
    #     pyautogui.press('esc')
    #     time.sleep(2)
    #     if go_to_true:
    #         _go_to(63, 25)
    #         # da pai zi
    #         time.sleep(10)
    #         _xiao_chu_jie_mian()
    #         pyautogui.press('z')
    #         time.sleep(chu_mo_time*60)
    #     else:
    #         _xiao_chu_jie_mian()
    #         pyautogui.press('z')
    #         time.sleep(chu_mo_time*60)
    #     customize_init()
    #     go_chu_mo_npc()
    #     for i in range(5):
    #         time.sleep(1)
    #         pyautogui.click(551, 571)
    #     time.sleep(1)
    #     pyautogui.press('esc')
    #     logger.info("ChuMoRenWu complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.ChuMoRenWuComplete = True

    # def hui_shou_full(self):
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'HuiShou'
    #
    #     for i in range(3):
    #         time.sleep(0.5)
    #         pyautogui.press('q')
    #         time.sleep(0.5)
    #         pyautogui.press('q')
    #         time.sleep(0.5)
    #         pyautogui.press('w')
    #         time.sleep(0.5)
    #         pyautogui.press('w')
    #
    #     # lie mo ji fen
    #     time.sleep(1)
    #     pyautogui.click(713, 116)
    #     time.sleep(1)
    #     pyautogui.click(594, 200)
    #     time.sleep(1)
    #     pyautogui.click(716, 617)
    #     time.sleep(1)
    #     pyautogui.press('esc')

    # def gua_ji(self, hh, mm=0, ss=0):
    #     logger.info("Start Guaji at {}".format(current_date_time()))
    #     self.GuaJiFlag = True
    #     self.CurStatus = 'GuaJi'
    #
    #     go_gua_ji_npc()
    #     time.sleep(1)
    #     if self.CurrentLevel > 80:
    #         if self.zhuan_shen_level == 0:
    #             pyautogui.click(394, 418)
    #         elif self.zhuan_shen_level == 1:
    #             pyautogui.click(493, 419)
    #         elif self.zhuan_shen_level == 2:
    #             pyautogui.click(595, 418)
    #         elif self.zhuan_shen_level == 3:
    #             pyautogui.click(595, 418)
    #         elif self.zhuan_shen_level == 4:
    #             pyautogui.click(393, 449)
    #         else:
    #             pyautogui.click(494, 446)
    #     else:
    #         pyautogui.click(593, 390)
    #
    #     # sui ji
    #     time.sleep(1)
    #     pyautogui.click(678, 728)
    #     time.sleep(1)
    #     xiao_chu_jie_mian()
    #     pyautogui.press('z')
    #
    #     logger.info("GuaJi shijian is ", seconds_change(self._time_diff(hh, mm, ss)))
    #     time.sleep(self._time_diff(hh, mm, ss))
    #     logger.info("GuaJi complete at {}".format(current_date_time()))
    #     customize_init()

    # ri chang
    # def ri_mo_bai_cheng_zhu(self):
    #     logger.info("Start MoBaiChengZhu at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'MoBaiChengZhu'
    #
    #     time.sleep(1)
    #     _huo_dong_jie_mian()
    #     pyautogui.click(701, 458)
    #
    #     for i in range(10):
    #         time.sleep(1)
    #         for j in range(4):
    #             time.sleep(0.5)
    #             pyautogui.click(582, 598)
    #             time.sleep(0.1)
    #             pyautogui.click(582, 598)
    #             time.sleep(0.1)
    #             pyautogui.click(582, 598)
    #             time.sleep(0.1)
    #         time.sleep(0.5)
    #         pyautogui.click(797, 520)
    #     time.sleep(0.5)
    #     pyautogui.press('esc')
    #     time.sleep(0.5)
    #     pyautogui.press('r')
    #     time.sleep(0.5)
    #     pyautogui.press('esc')
    #     time.sleep(0.5)
    #     pyautogui.press('r')
    #     logger.info("MoBaiChengZhu complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.MoBaiChengZhuComplete = True
    #
    # def ri_ye_zhan_bi_qi(self):
    #     logger.info("Start YeZhanBiQi at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'YeZhanBiQi'
    #
    #     _huo_dong_jie_mian()
    #
    #     pyautogui.click(508, 609)
    #     time.sleep(1)
    #     pyautogui.press('esc')
    #     time.sleep(1200)
    #     logger.info("YeZhanBiQi complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.YeZhanBiQiComplete = True
    #
    # # To Do, add pic diff part
    # def ri_shen_wei(self, shen_wei_time):
    #     logger.info("Start ShenWei at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'ShenWei'
    #
    #     _huo_dong_jie_mian()
    #     time.sleep(0.5)
    #     # jin ru shen wei
    #     pyautogui.click(510, 607)
    #     time.sleep(1)
    #
    #     _xiao_chu_jie_mian()
    #     time.sleep(1)
    #     pyautogui.press('z')
    #     time.sleep(self.Seconds*shen_wei_time)
    #     for i in range(10):
    #         if i == 6:
    #             pyautogui.click(889, 578)
    #             time.sleep(5)
    #             pyautogui.click(889, 578)
    #             time.sleep(68)
    #             pyautogui.click(511, 600)
    #         else:
    #             pyautogui.click(889, 578)
    #             time.sleep(5)
    #             pyautogui.click(889, 578)
    #             time.sleep(52)
    #             pyautogui.click(511, 600)
    #     # li kai
    #     time.sleep(1)
    #     pyautogui.click(911, 566)
    #     # que ding
    #     time.sleep(1)
    #     pyautogui.click(448, 455)
    #     logger.info("ShenWei complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.ShenWeiComplete = True
    #
    # def ri_world_boss(self):
    #     logger.info("Start WorldBoss at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'WorldBoss'
    #
    #     time.sleep(1)
    #     _huo_dong_jie_mian()
    #     pyautogui.click(510, 598)
    #     time.sleep(1)
    #     pyautogui.press('esc')
    #     time.sleep(1)
    #     pyautogui.press('z')
    #     time.sleep(2000)
    #
    #     # jia bei
    #     for i in range(10):
    #         pyautogui.click(454, 548)
    #         time.sleep(1)
    #     # pyautogui.press('e')
    #     logger.info("WorldBoss complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.WorldBossComplete = True
    #
    # def ri_jin_zhu_song_li(self):
    #     logger.info("Start JinZhuSongLi at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'JinZhuSongLi'
    #
    #     _huo_dong_jie_mian()
    #
    #     # can yu huo dong
    #     time.sleep(2)
    #     pyautogui.click(508, 596)
    #
    #     time.sleep(1)
    #     pyautogui.rightClick(949, 699)
    #
    #     time.sleep(1)
    #     pyautogui.press('z')
    #
    #     time.sleep(300)
    #     logger.info("JinZhuSongLi complete at {}".format(current_date_time()))
    #     customize_init()

    # def ge_ren_boss(self, extra_time=0):
    #     logger.info("Start GeRenBoss at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'GeRenBoss'
    #
    #     if self.zhuan_shen_level == 0:
    #         for i in range(3):
    #             # ge ren boss
    #             _bao_wu_jie_mian(2)
    #             time.sleep(1)
    #             pyautogui.click(792, 595)
    #
    #             time.sleep(1)
    #             pyautogui.click(348, 198)
    #
    #             # boss ming zi
    #             time.sleep(1)
    #             pyautogui.click(261, (255 + (i * 40)))
    #             time.sleep(1)
    #             pyautogui.click(785, 617)
    #             time.sleep(0.5)
    #             pyautogui.press('z')
    #             time.sleep(1)
    #             if i == 0:
    #                 time.sleep(35 + (i * 15) + extra_time)
    #             elif i == 1:
    #                 time.sleep(50 + (i * 15) + extra_time)
    #             else:
    #                 time.sleep(70 + (i * 15) + extra_time)
    #             time.sleep(1)
    #             _boss_hui_shou()
    #             time.sleep(1)
    #             pyautogui.click(859, 533)
    #     elif 0 < self.zhuan_shen_level <= 2:
    #         for i in range(4):
    #             # ge ren boss
    #             _bao_wu_jie_mian(2)
    #             time.sleep(1)
    #             pyautogui.click(792, 595)
    #
    #             time.sleep(1)
    #             pyautogui.click(348, 198)
    #
    #             # boss ming zi
    #             time.sleep(1)
    #             pyautogui.click(261, (255 + (i * 40)))
    #             time.sleep(1)
    #             pyautogui.click(785, 617)
    #             time.sleep(0.5)
    #             pyautogui.press('z')
    #             time.sleep(1)
    #             if i == 0:
    #                 time.sleep(35 + (i * ge_ren_boss_time) + extra_time)
    #             elif i == 1:
    #                 time.sleep(50 + (i * ge_ren_boss_time) + extra_time)
    #             elif i == 2:
    #                 time.sleep(70 + (i * ge_ren_boss_time) + extra_time)
    #             else:
    #                 time.sleep(90 + (i * ge_ren_boss_time) + extra_time)
    #             time.sleep(1)
    #             _boss_hui_shou()
    #             time.sleep(1)
    #             pyautogui.click(859, 533)
    #     elif 2 < self.zhuan_shen_level <= 4:
    #         for i in range(5):
    #             # ge ren boss
    #             _bao_wu_jie_mian(2)
    #             time.sleep(1)
    #             pyautogui.click(792, 595)
    #
    #             time.sleep(1)
    #             pyautogui.click(348, 198)
    #
    #             # boss ming zi
    #             time.sleep(1)
    #             pyautogui.click(261, (255 + (i * 40)))
    #             time.sleep(1)
    #             pyautogui.click(785, 617)
    #             time.sleep(0.5)
    #             pyautogui.press('z')
    #             time.sleep(1)
    #             if i == 0:
    #                 time.sleep(35 + (i * ge_ren_boss_time) + extra_time)
    #             elif i == 1:
    #                 time.sleep(45 + (i * ge_ren_boss_time) + extra_time)
    #             elif i == 2:
    #                 time.sleep(55 + (i * ge_ren_boss_time) + extra_time)
    #             elif i == 3:
    #                 time.sleep(70 + (i * ge_ren_boss_time) + extra_time)
    #             else:
    #                 time.sleep(80 + (i * ge_ren_boss_time) + extra_time)
    #             time.sleep(1)
    #             _boss_hui_shou()
    #             time.sleep(1)
    #             pyautogui.click(859, 533)
    #     else:
    #         for i in range(6):
    #             # ge ren boss
    #             _bao_wu_jie_mian(2)
    #             time.sleep(1)
    #             pyautogui.click(792, 595)
    #
    #             time.sleep(1)
    #             pyautogui.click(348, 198)
    #
    #             # boss ming zi
    #             time.sleep(1)
    #             pyautogui.click(261, (255 + (i * 40)))
    #             time.sleep(1)
    #             pyautogui.click(785, 617)
    #             time.sleep(0.5)
    #             pyautogui.press('z')
    #             time.sleep(1)
    #             if i == 0:
    #                 time.sleep(35 + (i * ge_ren_boss_time) + extra_time)
    #             elif i == 1:
    #                 time.sleep(45 + (i * ge_ren_boss_time) + extra_time)
    #             elif i == 2:
    #                 time.sleep(60 + (i * ge_ren_boss_time) + extra_time)
    #             elif i == 3:
    #                 time.sleep(70 + (i * ge_ren_boss_time) + extra_time)
    #             elif i == 4:
    #                 time.sleep(90 + (i * ge_ren_boss_time) + extra_time)
    #             else:
    #                 time.sleep(100 + (i * ge_ren_boss_time) + extra_time)
    #             time.sleep(1)
    #             _boss_hui_shou()
    #             time.sleep(1)
    #             pyautogui.click(859, 533)
    #     logger.info("GeRenBoss complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.GeRenBossiComplete = True

    # def ri_bi_guan(self):
    #     logger.info("Start BiGuan at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'BiGuan'
    #
    #     time.sleep(1)
    #     huo_dong_jie_mian()
    #     pyautogui.click(509, 609)
    #
    #     # xiao chu jie mian
    #     xiao_chu_jie_mian()
    #
    #     # To do, improve it
    #     # di tu
    #     time.sleep(1)
    #     pyautogui.press('m')
    #
    #     if self.zhuan_shen_level == 0:
    #         # zuo biao x
    #         time.sleep(1)
    #         pyautogui.click(612, 192)
    #         time.sleep(1)
    #         pyautogui.typewrite('26')
    #
    #         # zuo biao y
    #         time.sleep(1)
    #         pyautogui.click(710, 192)
    #         time.sleep(1)
    #         pyautogui.typewrite('34')
    #     elif 0 < self.zhuan_shen_level <= 2:
    #         # zuo biao x
    #         time.sleep(1)
    #         pyautogui.click(613, 192)
    #         time.sleep(1)
    #         pyautogui.typewrite('26')
    #
    #         # zuo biao y
    #         time.sleep(1)
    #         pyautogui.click(713, 192)
    #         time.sleep(1)
    #         pyautogui.typewrite('34')
    #
    #     elif 2 < self.zhuan_shen_level <= 4:
    #         # zuo biao x
    #         time.sleep(1)
    #         pyautogui.click(613, 192)
    #         time.sleep(1)
    #         pyautogui.typewrite('26')
    #
    #         # zuo biao y
    #         time.sleep(1)
    #         pyautogui.click(713, 192)
    #         time.sleep(1)
    #         pyautogui.typewrite('34')
    #
    #     elif 4 < self.zhuan_shen_level <= 6:
    #         # zuo biao x
    #         time.sleep(1)
    #         pyautogui.click(613, 192)
    #         time.sleep(1)
    #         pyautogui.typewrite('26')
    #
    #         # zuo biao y
    #         time.sleep(1)
    #         pyautogui.click(713, 192)
    #         time.sleep(1)
    #         pyautogui.typewrite('34')
    #
    #     else:
    #         # zuo biao x
    #         time.sleep(1)
    #         pyautogui.click(613, 192)
    #         time.sleep(1)
    #         pyautogui.typewrite('22')
    #
    #         # zuo biao y
    #         time.sleep(1)
    #         pyautogui.click(713, 192)
    #         time.sleep(1)
    #         pyautogui.typewrite('30')
    #
    #     # qian wang di dian
    #     time.sleep(1)
    #     pyautogui.click(770, 192)
    #
    #     # zai ci dian ji
    #     time.sleep(1)
    #     pyautogui.click(770, 192)
    #     time.sleep(1200)
    #
    #     time.sleep(1)
    #     pyautogui.press('esc')
    #     logger.info("BiGuan complete at {}".format(current_date_time()))
    #     customize_init()
    #     # flag
    #     self.BiGuanComplete = True
    #
    # def ri_guai_wu_gong_cheng(self):
    #     logger.info("Start GuaiWuGongCheng at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'GuaiWuGongCheng'
    #
    #     time.sleep(1)
    #
    #     # self._HuoDongJieMian()
    #     bao_wu_jie_mian(5)
    #
    #     # Qian Wang
    #     pyautogui.click(793, 581)
    #     time.sleep(1)
    #
    #     # can yu huo dong
    #     pyautogui.click(509, 596)
    #     time.sleep(1)
    #
    #     # _huo_dong_jie_mian()
    #     # time.sleep(1)
    #     #
    #     # pyautogui.click(508, 609)
    #     # time.sleep(1)
    #
    #     # su ji
    #     pyautogui.click(679, 728)
    #     time.sleep(1)
    #
    #     xiao_chu_jie_mian()
    #     time.sleep(1)
    #     pyautogui.press('z')
    #     time.sleep(1750)
    #     logger.info("GuaiWuGongCheng complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.GuaiWuGongChengComplete = True
    #
    # def ri_suo_yao_ta(self):
    #     logger.info("Start RiSuoYaoTa at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'RiSuoYaoTa'
    #
    #     time.sleep(1)
    #
    #     huo_dong_jie_mian()
    #     pyautogui.click(510, 396)
    #     # gua ji ban ge xiao shi
    #     time.sleep(1)
    #     pyautogui.press('z')
    #     time.sleep(1750)
    #     logger.info("RiSuoYaoTa complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.SuoYaoTaComplete = True
    #
    # # To Do, improve with pic diff and run times
    # def ri_duo_bei_ya_song(self):
    #     logger.info("Start RiDuoBeiYaSong at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'RiDuoBeiYaSong'
    #
    #     time.sleep(1)
    #
    #     for ii in range(3):
    #         bao_wu_jie_mian(3)
    #
    #         # qian wang
    #         time.sleep(1)
    #         pyautogui.click(793, 551)
    #
    #         # jie qu ren wu
    #         time.sleep(1)
    #         pyautogui.click(509, 582)
    #
    #         # shua xin
    #         for i in range(10):
    #             time.sleep(1)
    #             pyautogui.click(649, 551)
    #         # hu song
    #         time.sleep(1)
    #         pyautogui.click(936, 550)
    #
    #         if ii == 0:
    #             time.sleep(45)
    #         else:
    #             time.sleep(165)
    #
    #         # que ding
    #         time.sleep(1)
    #         pyautogui.click(581, 502)
    #
    #     logger.info("RiDuoBeiYaSong complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.DuoBeiYaSongComplete = True
    #
    # def ri_san_bei_lian_gong(self, lian_gong_time):
    #     logger.info("Start SanBeiLianGong at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'SanBeiLianGong'
    #
    #     lian_gong(lian_gong_time)
    #     logger.info("SanBeiLianGong complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.SanBeiLianGongComplete = True
    #
    # def ri_jia_lan_shen_dian(self, jia_lan_time):
    #     logger.info("Start JiaLanShenDian at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'JiaLanShenDian'
    #
    #     time.sleep(1)
    #
    #     huo_dong_jie_mian()
    #     pyautogui.click(510, 599)
    #     time.sleep(1)
    #
    #     xiao_chu_jie_mian()
    #     time.sleep(1)
    #     pyautogui.press('z')
    #     time.sleep(jia_lan_time)
    #     logger.info("JiaLanShenDian complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.JiaLanShenDianComplete = True
    #
    # # To Do
    # def ri_hai_tian_sheng_yan(self):
    #     logger.info("Start HaiTianShengYan at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'HaiTianShengYan'
    #
    #     time.sleep(1)
    #
    #     huo_dong_jie_mian()
    #     pyautogui.click(508, 607)
    #     time.sleep(1)
    #     xiao_chu_jie_mian()
    #     pyautogui.press('z')
    #     time.sleep(900)
    #
    #     # NPC part and delay part
    #     logger.info("HaiTianShengYan complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.HaiTianShengYanComplete = True
    #
    # def ri_shi_mu(self):
    #     logger.info("Start ShiMuMiZhen at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'RiShiMuMiZhen'
    #
    #     time.sleep(1)
    #
    #     huo_dong_jie_mian()
    #
    #     # Jin ru huo dong
    #     time.sleep(0.5)
    #     pyautogui.click(510, 599)
    #     time.sleep(10)
    #     # ToDo
    #     # NPC part and delay part
    #     logger.info("ShiMuMiZhen complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.ShiMuMiZhenComplete = True

    # ToDo
    # def da_boss(self):
    #     pass

    # def ri_da_ti(self):
    #     logger.info("Start DaTi at {}".format(current_date_time()))
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'RiDaTi'
    #
    #     time.sleep(1)
    #
    #     huo_dong_jie_mian()
    #
    #     # Jin ru huo dong
    #     time.sleep(0.5)
    #     pyautogui.click(509, 581)
    #     time.sleep(900)
    #     # ToDo
    #     # NPC part and delay part
    #     logger.info("DaTi complete at {}".format(current_date_time()))
    #     customize_init()
    #     self.DaTi = True

    # To Do

    # To Do

    # To Do

    # def BFunction(self):
    #     pass

# To Do, improve cancel depedency


# To Do, replace with _WoYaoBianQiang Jie mian


# To Do, improve with HuoYueDu


# To do, replace with Bao Wu Jie Mian


# def capture_pic(cur_time):
#     _huo_dong_jie_mian_no_click()
#     hwnd = win32gui.GetForegroundWindow()
#     ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
#
#     coordinate = (rect.left + 2, rect.top + 2, rect.right - 2, rect.bottom - 2)
#     pic = ImageGrab.grab(coordinate)
#     path = "C:\\xingqi{}".format(xing_qi_ji)
#     if os.path.exists(path):
#         pic.save(path + "\\" + "xingqi" + str(xing_qi_ji) + "_" + str(cur_time) + ".png", quality=100)
#     else:
#         os.mkdir(path)
#         pic.save(path + "\\" + "xingqi" + str(xing_qi_ji) + "_" + str(cur_time) + ".png", quality=100)
#     time.sleep(1)
#     pyautogui.press('esc')
#     time.sleep(1)


# To Do Improve it


# To Do
