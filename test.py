import pyautogui
import time
import ctypes
import os
import win32gui

from PIL import ImageGrab
from datetime import datetime as sm
from ScreenShot import RECT

pyautogui.PAUSE = 1.5
GongXunTime = 120
JinYinTime = 160
cai_liao_move_value = 30

rect = RECT()


class AW1(object):

    def __init__(self, current_level):
        self.CurrentLevel = current_level
        self.GuaJiFlag = True
        self.CurStatus = 'null'
        self.Complete = False
        self.EventTime = 0
        self.Seconds = 60
        self.GongXunRenWuComplete = False
        self.JingYingRenWuComplete = False
        self.WeiWangRenWuComplete = False
        self.TaFangFengMoComplete = False
        self.CaiLiaoFuBenComplete = False
        self.ChuMoRenWuComplete = False
        self.ChuangTianGuanComplete = False
        self.MoBaiChengZhuComplete = False
        self.YeZhanBiQiComplete = False
        self.ShenWeiComplete = False
        self.WorldBossComplete = False
        self.JinZhuSongLiComplete = False
        self.YeZhanBiQiComplete = False
        self.GeRenBossiComplete = False
        self.GuaiWuGongChengComplete = False
        self.BiGuanComplete = False
        self.SuoYaoTaComplete = False
        self.DuoBeiYaSongComplete = False
        self.HaiTianShengYanComplete = False
        self.JiaLanShenDianComplete = False
        self.SanBeiLianGongComplete = False
        self.ShiMuMiZhenComplete = False
        self.DaTi = False
        self.x, self.y = pyautogui.size()

        self.Y = str(sm.now())[0:4]
        self.M = str(sm.now())[5:7]
        self.D = str(sm.now())[8:10]

    def tab_qie_huan(self):
        time.sleep(1)
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        self.GuaJiFlag = False

    def gong_xun_ren_wu(self, run_times, wait_time):
        print "Start GongXunRenWu at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'JinYanGongXun'
        self.EventTime += 1
        # time.sleep(1)
        # pyautogui.click(943, 347)

        _bao_wu_jie_mian(3)
        time.sleep(1)
        pyautogui.click(793, 583)

        for i in range(run_times):
            # time.sleep(1)
            # pyautogui.press('esc')

            # shu xin
            time.sleep(1)
            pyautogui.click(622, 527)
            time.sleep(8)

            # jie shou ren wu
            pyautogui.click(509, 567)
            time.sleep(1)

            # qian wang wan cheng ren wu
            pyautogui.click(509, 567)

            # deng dai wan cheng
            time.sleep(wait_time)

            # dian ji di mian (fang zi wa kuang cuo wo)
            # pyautogui.click(522, 537)
            # time.sleep(1)
            # time.sleep(1)
            # pyautogui.click(963, 581)
            # click chuan
            time.sleep(1)
            pyautogui.click(793, 583)

            # wan cheng ren wu - san bei jiang li
            time.sleep(2)
            pyautogui.click(610, 511)
            time.sleep(1)
        # for i in range(run_times-1):
        #     time.sleep(1)
        #     pyautogui.click(622, 527)
        #     time.sleep(8)
        #     pyautogui.click(509, 567)
        #     time.sleep(1)
        #
        #     pyautogui.click(509, 567)
        #     time.sleep(GongXunTime)
        #     # dian ji di mian (fang zi wa kuang cuo wo)
        #     pyautogui.click(522, 537)
        #     time.sleep(1)
        #     pyautogui.click(900, 345)
        #     time.sleep(1)
        #     pyautogui.click(613, 510)
        #     time.sleep(1)
        print "GongXunRenWu complete at {}".format(current_date_time())
        customize_init()
        self.GongXunRenWuComplete = True

    def jing_ying_ren_wu(self, run_times, wait_time):
        print "Start JingYingRenWu at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'TianFu'
        self.EventTime += 1

        # time.sleep(1)
        # pyautogui.click(943, 347)
        _yin_xiong_jie_mian(3)

        for j in range(run_times):
            time.sleep(1)
            pyautogui.click(509, 567)
            time.sleep(1)
            pyautogui.click(509, 567)
            time.sleep(wait_time)

            time.sleep(1)
            # pyautogui.click(901, 346)
            pyautogui.click(628, 206)
            time.sleep(1)

            time.sleep(1)
            pyautogui.click(613, 510)
            time.sleep(1)

        # for j in range(run_times):
        #     pyautogui.click(509, 567)
        #     time.sleep(1)
        #     pyautogui.click(509, 567)
        #     time.sleep(JinYinTime)
        #
        #     time.sleep(1)
        #     pyautogui.click(901, 346)
        #
        #     time.sleep(1)
        #     pyautogui.click(613, 510)
        #     time.sleep(1)
        print "JingYingRenWu complete at {}".format(current_date_time())
        customize_init()
        self.JingYingRenWuComplete = True

    def ta_fang_feng_mo(self, feng_mo_time):
        print "Start TaFangFengMo at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'TaFangFengMo'
        self.EventTime += 1

        # self._BaoWuShenDunJieMian()
        for jj in range(feng_mo_time):
            # self._GoFengMoNPC()
            _go_feng_mo_npc()
            # # dian NPC
            # time.sleep(1)
            # pyautogui.click(610, 337)
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

            # self._GoFengMoNPC()
            # # lin qu jiang li
            # pyautogui.click(606, 382)
        print "TaFangFengMo Complete at {}".format(current_date_time())
        customize_init()
        self.TaFangFengMoComplete = True

    def chuang_tian_guan(self):
        print "Start ChuangTianGuan at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'ChuangTianGuan'
        self.EventTime += 1

        time.sleep(1)
        pyautogui.click(911, 503)

        time.sleep(1)
        pyautogui.click(507, 600)
        if self.CurrentLevel == 0:
            time.sleep(190)
        elif 0 < self.CurrentLevel <= 2:
            time.sleep(430)
        elif 2 < self.CurrentLevel <= 4:
            time.sleep(790)
        else:
            time.sleep(1300)
        pyautogui.click(511, 514)
        print "ChuangTianGuan Complete at {}".format(current_date_time())
        customize_init()
        self.ChuangTianGuanComplete = True

    def cai_liao_fu_ben(self, fu_ben_time=2):
        print "Start CaiLiaoFuBen at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'CaiLiaoFuBen'
        self.EventTime += 1
        time.sleep(1)
        _bao_wu_shen_dun_jie_mian()
        for i in range(fu_ben_time):
            if self.CurrentLevel == 0:
                for iii in range(1, 2):
                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (iii * cai_liao_move_value)))

                    time.sleep(1)
                    pyautogui.click(499, 583)

                    # zi dong zhan dou
                    time.sleep(1)
                    pyautogui.press('z')
                    if iii < 3:
                        time.sleep(88)
                    elif iii == 3:
                        time.sleep(110)
                    elif iii == 4:
                        time.sleep(270)
                    elif iii == 5:
                        time.sleep(75)
                    elif iii == 6:
                        time.sleep(130)
                    else:
                        time.sleep(130)
                    _boss_hui_shou()
                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            elif 0 < self.CurrentLevel <= 4:
                for iii in range(1, 5, 3):

                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (iii * cai_liao_move_value)))

                    time.sleep(1)
                    pyautogui.click(499, 583)

                    # zi dong zhan dou
                    time.sleep(1)
                    pyautogui.press('z')
                    if iii < 3:
                        time.sleep(88)
                    elif iii == 3:
                        time.sleep(110)
                    elif iii == 4:
                        time.sleep(270)
                    elif iii == 5:
                        time.sleep(75)
                    elif iii == 6:
                        time.sleep(130)
                    else:
                        time.sleep(130)
                    _boss_hui_shou()
                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            else:
                for iii in range(0, 7):

                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (iii * cai_liao_move_value)))

                    time.sleep(1)
                    pyautogui.click(499, 583)

                    # zi dong zhan dou
                    time.sleep(1)
                    pyautogui.press('z')
                    if iii < 3:
                        time.sleep(88)
                    elif iii == 3:
                        time.sleep(110)
                    elif iii == 4:
                        time.sleep(270)
                    elif iii == 5:
                        time.sleep(75)
                    elif iii == 6:
                        time.sleep(130)
                    else:
                        time.sleep(130)
                    _boss_hui_shou()
                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            # time.sleep(1)
            self.hui_shou_full()
        print "CaiLiaoFuBen Complete at {}".format(current_date_time())
        customize_init()
        self.CaiLiaoFuBenComplete = True

    def wei_wang_ren_wu(self):
        print "Start WeiWangRenWu at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'WeiWangRenWu'
        self.EventTime += 1

        _go_wei_wang_npc()

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
        # pyautogui.click(901, 347)
        # time.sleep(1)
        _go_wei_wang_npc()

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

        # deng dai wan cheng
        time.sleep(50)

        # chuan
        # pyautogui.click(900, 346)
        # time.sleep(1)
        _go_wei_wang_npc()
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

        # deng dai wan cheng
        time.sleep(50)

        # chuan
        _go_wei_wang_npc()

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
        time.sleep(35)

        # chuan
        _go_wei_wang_npc()

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
        print "WeiWangRenWu complete at {}".format(current_date_time())
        customize_init()
        self.WeiWangRenWuComplete = True

    def chu_mo_ren_wu(self, chu_mo_time):
        print "Start ChuMoRenWu at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'ChuMoRenWu'
        self.EventTime += 1

        # chuan dao Zhang TianShi
        go_chu_mo_npc()

        # jin ru jiang jun mu
        time.sleep(2)
        pyautogui.click(544, 497)
        time.sleep(1)

        pyautogui.press('esc')
        time.sleep(1)
        # pyautogui.click(462, 352)
        # time.sleep(2)
        time.sleep(1)
        _go_to(63, 25)
        # da pai zi
        time.sleep(10)
        _xiao_chu_jie_mian()
        pyautogui.press('z')
        time.sleep(chu_mo_time*60)
        customize_init()
        go_chu_mo_npc()
        for i in range(5):
            time.sleep(1)
            pyautogui.click(551, 571)
        time.sleep(1)
        pyautogui.press('esc')
        print "ChuMoRenWu complete at {}".format(current_date_time())
        customize_init()
        self.ChuMoRenWuComplete = True

    def hui_shou_full(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HuiShou'
        self.EventTime += 1

        for i in range(3):
            time.sleep(0.5)
            pyautogui.press('q')
            time.sleep(0.5)
            pyautogui.press('q')
            time.sleep(0.5)
            pyautogui.press('w')
            time.sleep(0.5)
            pyautogui.press('w')

        # lie mo ji fen
        time.sleep(1)
        pyautogui.click(713, 116)
        time.sleep(1)
        pyautogui.click(594, 200)
        time.sleep(1)
        pyautogui.click(716, 617)
        time.sleep(1)
        pyautogui.press('esc')

    def gua_ji(self, hh, mm=0, ss=0):
        print "Start Guaji at {}".format(current_date_time())
        self.GuaJiFlag = True
        self.CurStatus = 'GuaJi'
        self.EventTime += 1

        _go_gua_ji_npc()
        time.sleep(1)
        if self.CurrentLevel == 0:
            pyautogui.click(394, 418)
        elif 0 < self.CurrentLevel <= 2:
            pyautogui.click(595, 418)
        elif 2 < self.CurrentLevel <= 4:
            pyautogui.click(595, 418)
        else:
            pyautogui.click(494, 446)

        _xiao_chu_jie_mian()
        pyautogui.press('z')

        print "GuaJi shijian is ", seconds_change(self._time_diff(hh, mm, ss))
        time.sleep(abs(self._time_diff(hh, mm, ss)-10))
        print "GuaJi complete at {}".format(current_date_time())
        customize_init()

    # ToDo imporve it
    def wa_kuang(self, wa_kuang_time):
        print "Start WaKuang at {}".format(current_date_time())
        self.GuaJiFlag = True
        self.CurStatus = 'WaKuang'
        self.EventTime += 1

        time.sleep(wa_kuang_time*self.Seconds)
        pyautogui.click(1220, 611)
        time.sleep(1)
        print "WaKuang Complete at {}".format(current_date_time())
        customize_init()

    def ri_mo_bai_cheng_zhu(self):
        print "Start MoBaiChengZhu at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'MoBaiChengZhu'
        self.EventTime += 1

        time.sleep(1)
        _huo_dong_jie_mian()
        pyautogui.click(701, 458)

        for i in range(9):
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
        print "MoBaiChengZhu complete at {}".format(current_date_time())
        customize_init()
        self.MoBaiChengZhuComplete = True

    def ri_ye_zhan_bi_qi(self):
        print "Start YeZhanBiQi at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'YeZhanBiQi'
        self.EventTime += 1

        _huo_dong_jie_mian()
        # pyautogui.click(701, 458)
        # time.sleep(1)
        pyautogui.click(508, 609)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1200)
        print "YeZhanBiQi complete at {}".format(current_date_time())
        customize_init()
        self.YeZhanBiQiComplete = True

    # To Do, add pic diff part
    def ri_shen_wei(self, shen_wei_time):
        print "Start ShenWei at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'ShenWei'
        self.EventTime += 1

        _huo_dong_jie_mian()
        time.sleep(0.5)
        # jin ru shen wei
        pyautogui.click(510, 607)
        time.sleep(1)
        # pyautogui.click(701, 458)
        # time.sleep(1)
        # pyautogui.click(508, 606)
        # time.sleep(1)

        _xiao_chu_jie_mian()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(self.Seconds*shen_wei_time)
        for i in range(9):
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
                time.sleep(42)
                pyautogui.click(511, 600)
        # li kai
        time.sleep(1)
        pyautogui.click(911, 566)
        # que ding
        time.sleep(1)
        pyautogui.click(448, 455)
        print "ShenWei complete at {}".format(current_date_time())
        customize_init()
        self.ShenWeiComplete = True

    def ri_world_boss(self):
        print "Start WorldBoss at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'WorldBoss'
        self.EventTime += 1

        time.sleep(1)
        _huo_dong_jie_mian()
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
        print "WorldBoss complete at {}".format(current_date_time())
        customize_init()
        self.WorldBossComplete = True

    def ri_jin_zhu_song_li(self):
        print "Start JinZhuSongLi at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'JinZhuSongLi'
        self.EventTime += 1

        _huo_dong_jie_mian()

        # can yu huo dong
        time.sleep(2)
        pyautogui.click(508, 596)
        time.sleep(2)
        # pyautogui.press('esc')
        # time.sleep(1)
        # pyautogui.press('z')
        # time.sleep(1)
        time.sleep(300)
        print "JinZhuSongLi complete at {}".format(current_date_time())
        customize_init()
        # self.JingYingRenWuComplete = True

    def ge_ren_boss(self):
        print "Start GeRenBoss at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'GeRenBoss'
        self.EventTime += 1

        if self.CurrentLevel == 0:
            for i in range(3):
                # ge ren boss
                # time.sleep(1)
                # pyautogui.click(713, 116)
                # time.sleep(1)
                # pyautogui.click(346, 196)
                _bao_wu_jie_mian(2)
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
                    time.sleep(35 + (i * 15))
                elif i == 1:
                    time.sleep(50 + (i * 15))
                else:
                    time.sleep(70 + (i * 15))
                time.sleep(1)
                _boss_hui_shou()
                time.sleep(1)
                pyautogui.click(859, 533)
        elif 0 < self.CurrentLevel <= 2:
            for i in range(4):
                # ge ren boss
                _bao_wu_jie_mian(2)
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
                    time.sleep(35 + (i * 15))
                elif i == 1:
                    time.sleep(50 + (i * 15))
                elif i == 2:
                    time.sleep(70 + (i * 15))
                else:
                    time.sleep(90 + (i * 15))
                time.sleep(1)
                _boss_hui_shou()
                time.sleep(1)
                pyautogui.click(859, 533)
        elif 2 < self.CurrentLevel <= 4:
            for i in range(5):
                # ge ren boss
                _bao_wu_jie_mian(2)
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
                    time.sleep(35 + (i * 15))
                elif i == 1:
                    time.sleep(45 + (i * 15))
                elif i == 2:
                    time.sleep(55 + (i * 15))
                elif i == 3:
                    time.sleep(70 + (i * 15))
                else:
                    time.sleep(80 + (i * 15))
                time.sleep(1)
                _boss_hui_shou()
                time.sleep(1)
                pyautogui.click(859, 533)
        else:
            for i in range(6):
                # ge ren boss
                _bao_wu_jie_mian(2)
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
                    time.sleep(35 + (i * 15))
                elif i == 1:
                    time.sleep(45 + (i * 15))
                elif i == 2:
                    time.sleep(60 + (i * 15))
                elif i == 3:
                    time.sleep(70 + (i * 15))
                elif i == 4:
                    time.sleep(90 + (i * 15))
                else:
                    time.sleep(100 + (i * 18))
                time.sleep(1)
                _boss_hui_shou()
                time.sleep(1)
                pyautogui.click(859, 533)
        print "GeRenBoss complete at {}".format(current_date_time())
        customize_init()
        self.GeRenBossiComplete = True

    def ri_bi_guan(self):
        print "Start BiGuan at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'BiGuan'
        self.EventTime += 1
        time.sleep(1)
        _huo_dong_jie_mian()
        pyautogui.click(509, 609)

        # xiao chu jie mian
        _xiao_chu_jie_mian()

        # To do, improve it
        # di tu
        time.sleep(1)
        pyautogui.press('m')

        if self.CurrentLevel == 0:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(613, 210)
            time.sleep(1)
            pyautogui.typewrite('26')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(713, 209)
            time.sleep(1)
            pyautogui.typewrite('34')
        elif 0 < self.CurrentLevel < 4:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(613, 210)
            time.sleep(1)
            pyautogui.typewrite('26')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(713, 209)
            time.sleep(1)
            pyautogui.typewrite('34')
        else:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(613, 210)
            time.sleep(1)
            pyautogui.typewrite('22')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(713, 209)
            time.sleep(1)
            pyautogui.typewrite('30')

        # qian wang di dian
        time.sleep(1)
        pyautogui.click(770, 209)

        # zai ci dian ji
        time.sleep(1)
        pyautogui.click(770, 209)
        time.sleep(1200)

        time.sleep(1)
        pyautogui.press('esc')
        print "BiGuan complete at {}".format(current_date_time())
        customize_init()
        # flag
        self.BiGuanComplete = True

    def ri_guai_wu_gong_cheng(self):
        print "Start GuaiWuGongCheng at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'GuaiWuGongCheng'
        self.EventTime += 1
        time.sleep(1)

        # self._HuoDongJieMian()
        _bao_wu_jie_mian(4)

        # Qian Wang
        pyautogui.click(793, 581)
        time.sleep(1)

        # can yu huo dong
        pyautogui.click(509, 596)
        time.sleep(1)

        # su ji
        pyautogui.click(679, 728)
        time.sleep(1)

        _xiao_chu_jie_mian()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1750)
        print "GuaiWuGongCheng complete at {}".format(current_date_time())
        customize_init()
        self.GuaiWuGongChengComplete = True

    def ri_suo_yao_ta(self):
        print "Start RiSuoYaoTa at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'RiSuoYaoTa'
        self.EventTime += 1
        time.sleep(1)

        _huo_dong_jie_mian()
        pyautogui.click(510, 396)
        # gua ji ban ge xiao shi
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1750)
        print "RiSuoYaoTa complete at {}".format(current_date_time())
        customize_init()
        self.SuoYaoTaComplete = True

    # To Do, improve with pic diff and run times
    def ri_duo_bei_ya_song(self):
        print "Start RiDuoBeiYaSong at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'RiDuoBeiYaSong'
        self.EventTime += 1
        time.sleep(1)
        # for i in range(3):
        # self._HuoDongJieMian()
        # pyautogui.click(885, 601)
        # time.sleep(1)
        for ii in range(3):
            _bao_wu_jie_mian(3)

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

            # # que ding bu shi shuang bei
            # time.sleep(1)
            # pyautogui.click(509, 454)

            if ii == 0:
                time.sleep(45)
                # pyautogui.press('esc')
            else:
                time.sleep(165)
                # pyautogui.press('esc')

            # que ding
            time.sleep(1)
            pyautogui.click(581, 502)

        print "RiDuoBeiYaSong complete at {}".format(current_date_time())
        customize_init()
        self.DuoBeiYaSongComplete = True

    def ri_san_bei_lian_gong(self, lian_gong_time):
        print "Start SanBeiLianGong at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'SanBeiLianGong'
        self.EventTime += 1

        lian_gong(lian_gong_time)
        print "SanBeiLianGong complete at {}".format(current_date_time())
        customize_init()
        self.SanBeiLianGongComplete = True

    def ri_jia_lan_shen_dian(self, jia_lan_time):
        print "Start JiaLanShenDian at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'JiaLanShenDian'
        self.EventTime += 1
        time.sleep(1)

        _huo_dong_jie_mian()
        pyautogui.click(510, 599)
        time.sleep(1)

        _xiao_chu_jie_mian()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(jia_lan_time)
        print "JiaLanShenDian complete at {}".format(current_date_time())
        customize_init()
        self.JiaLanShenDianComplete = True

    # To Do
    def ri_hai_tian_sheng_yan(self):
        print "Start HaiTianShengYan at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'HaiTianShengYan'
        self.EventTime += 1
        time.sleep(1)

        _huo_dong_jie_mian()
        pyautogui.click(508, 607)
        # time.sleep(1)
        # pyautogui.press('esc')
        # time.sleep(1)
        _xiao_chu_jie_mian()
        pyautogui.press('z')
        time.sleep(900)

        # NPC part and delay part
        print "HaiTianShengYan complete at {}".format(current_date_time())
        customize_init()
        self.HaiTianShengYanComplete = True

    def ri_shi_mu(self):
        print "Start ShiMuMiZhen at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'RiShiMuMiZhen'
        self.EventTime += 1
        time.sleep(1)

        _huo_dong_jie_mian()

        # Jin ru huo dong
        time.sleep(0.5)
        pyautogui.click(510, 599)
        time.sleep(10)
        # ToDo
        # NPC part and delay part
        print "ShiMuMiZhen complete at {}".format(current_date_time())
        customize_init()
        self.ShiMuMiZhenComplete = True

    # # To Do, improve cancel depedency
    # def _BossJieMian(self):
    #     # da kai boss jie mian
    #     time.sleep(1)
    #     pyautogui.click(715, 188)
    #     time.sleep(1)

    def _time_diff(self, hh, mm=0, ss=0):
        current_time = sm.now()
        target_times = self.Y+'-'+self.M+'-'+self.D+' '+str(hh)+':'+str(mm)+':'+str(ss)+'.0'
        target_time = sm.strptime(target_times, "%Y-%m-%d %H:%M:%S.%f")

        return (target_time-current_time).seconds

    # ToDo
    def da_boss(self):
        pass

    def _wo_yao_bian_qiang_jie_mian(self):
        pass

    # To Do
    def re_start(self):
        pass

    # To Do
    def gua_suo_yao_ta(self):
        _go_gua_ji_npc()
        _xiao_chu_jie_mian()

        time.sleep(1)
        pyautogui.click(654, 390)

        if self.CurrentLevel == 0:
            time.sleep(1)
            pyautogui.click(515, 397)
        elif 0 < self.CurrentLevel <= 2:
            time.sleep(1)
            pyautogui.click(515, 426)
        elif 2 < self.CurrentLevel <= 4:
            time.sleep(1)
            pyautogui.click(515, 453)
        elif 4 < self.CurrentLevel <= 6:
            time.sleep(1)
            pyautogui.click(515, 483)
        elif 6 < self.CurrentLevel <= 8:
            time.sleep(1)
            pyautogui.click(515, 511)
        else:
            time.sleep(1)
            pyautogui.click(515, 539)
        while True:
            _xiao_chu_jie_mian()
            time.sleep(0.5)
            pyautogui.press('z')
            time.sleep(600)
            pyautogui.click(854, 684)
            time.sleep(1)
            pyautogui.click(310, 204)
            time.sleep(1)
            for i in range(8):
                time.sleep(2)
                pyautogui.doubleClick(197, 271)
                time.sleep(0.5)
            pyautogui.press('esc')
            _xiao_chu_jie_mian()
            time.sleep(360000)

    def da_suo_yao_ta(self, da_time):
        _go_gua_ji_npc()
        _xiao_chu_jie_mian()

        time.sleep(1)
        pyautogui.click(654, 390)

        if self.CurrentLevel == 0:
            time.sleep(1)
            pyautogui.click(515, 397)
        elif 0 < self.CurrentLevel <= 2:
            time.sleep(1)
            pyautogui.click(515, 426)
        elif 2 < self.CurrentLevel <= 4:
            time.sleep(1)
            pyautogui.click(515, 453)
        elif 4 < self.CurrentLevel <= 6:
            time.sleep(1)
            pyautogui.click(515, 483)
        elif 6 < self.CurrentLevel <= 8:
            time.sleep(1)
            pyautogui.click(515, 511)
        else:
            time.sleep(1)
            pyautogui.click(515, 539)

        _xiao_chu_jie_mian()
        pyautogui.press('z')
        time.sleep(self.Seconds*da_time)
        customize_init()

    def ri_da_ti(self):
        print "Start DaTi at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'RiDaTi'
        self.EventTime += 1
        time.sleep(1)

        _huo_dong_jie_mian()

        # Jin ru huo dong
        time.sleep(0.5)
        pyautogui.click(509, 581)
        time.sleep(900)
        # ToDo
        # NPC part and delay part
        print "DaTi complete at {}".format(current_date_time())
        customize_init()
        self.DaTi = True

    def bang_hui_huo_dong(self):
        print "Start BangHui at {}".format(current_date_time())
        self.GuaJiFlag = False
        self.CurStatus = 'BangHui'
        self.EventTime += 1
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

        print "DaTi complete at {}".format(current_date_time())
        customize_init()
        self.DaTi = True

    # To Do
    def di_xia_gong_dian(self):
        pass

    # To Do
    def zu_ma_boss(self):
        pass

    # To Do
    def mi_jin(self):
        pass


def _go_feng_mo_npc():
    time.sleep(1)
    pyautogui.click(337, 674)
    time.sleep(1)
    pyautogui.click(575, 598)
    time.sleep(1)
    pyautogui.click(412, 214)
    time.sleep(1)
    pyautogui.click(892, 220)


# To Do, improve cancel depedency
def _boss_jie_mian():
    # da kai boss jie mian
    time.sleep(1)
    pyautogui.click(715, 188)
    time.sleep(1)


def _huo_dong_jie_mian():
    time.sleep(0.5)
    pyautogui.click(951, 714)
    time.sleep(0.5)
    pyautogui.press('j')
    time.sleep(1)
    pyautogui.click(750, 615)
    time.sleep(0.5)


def _xiao_chu_jie_mian():
    time.sleep(0.5)
    pyautogui.click(951, 714, button='right')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(0.5)


def customize_init():
    _xiao_chu_jie_mian()
    pyautogui.press('b')
    time.sleep(0.5)
    pyautogui.click(625, 611)
    time.sleep(0.5)
    pyautogui.click(521, 410)
    time.sleep(1)
    # hui shou kuangshi
    pyautogui.click(602, 555)
    time.sleep(2)
    # hui shou zhuang bei
    pyautogui.click(801, 554)
    time.sleep(2)
    pyautogui.press('esc')


def _go_wei_wang_npc():
    customize_init()
    time.sleep(1)
    pyautogui.click(777, 206, button='right')
    time.sleep(1)
    pyautogui.click(659, 205)
    time.sleep(2)


# To Do, replace with _WoYaoBianQiang Jie mian
def _wo_yao_sheng_ji():
    time.sleep(1)
    pyautogui.click(335, 673)
    time.sleep(1)
    pyautogui.click(199, 212)
    time.sleep(1)
    pyautogui.click(576, 601)
    time.sleep(1)
    pyautogui.click(410, 214)
    time.sleep(1)


def _huo_dong_jie_mian_no_click():
    time.sleep(0.5)
    pyautogui.click(951, 714)
    time.sleep(0.5)
    pyautogui.press('j')
    time.sleep(2)


def _go_gua_ji_npc():
    _xiao_chu_jie_mian()
    time.sleep(1)
    pyautogui.click(570, 677)
    time.sleep(1)
    pyautogui.click(200, 212)
    time.sleep(1)
    pyautogui.click(793, 610)
    time.sleep(1)


def current_date_time():
    x = str(sm.now())
    return x[0:19]


# To Do, improve with HuoYueDu
def lin_qu_huo_yue_jiang_li():
    _xiao_chu_jie_mian()
    time.sleep(1)
    pyautogui.click(260, 128)
    for i in range(5):
        time.sleep(1)
        pyautogui.click(766, (373+i*57))
        time.sleep(1)


def xing_qi_ji():
    xing_qi = sm.now()
    return xing_qi.weekday()


# To do, replace with Bao Wu Jie Mian
def _bao_wu_shen_dun_jie_mian():
    # da kai bao wu jie mian
    customize_init()
    time.sleep(1)
    pyautogui.click(570, 677)
    time.sleep(1)
    pyautogui.click(198, 269)
    time.sleep(1)
    pyautogui.click(793, 569)
    time.sleep(1)
    pyautogui.press('esc')


def _bao_wu_jie_mian(level):
    # da kai bao wu jie mian
    _xiao_chu_jie_mian()
    time.sleep(1)
    pyautogui.click(569, 679)
    if level == 1:
        time.sleep(1)
        pyautogui.click(200, 217)
    elif level == 2:
        time.sleep(1)
        pyautogui.click(200, (217+(level-1)*54))
    elif level == 3:
        time.sleep(1)
        pyautogui.click(200, (217+(level-1)*54))
    elif level == 4:
        time.sleep(1)
        pyautogui.click(200, (217+(level-1)*54))
    else:
        time.sleep(1)
        pyautogui.click(200, 433)


def _go_to(xx, yy):
    _xiao_chu_jie_mian()
    # di tu
    time.sleep(1)
    pyautogui.press('m')
    time.sleep(1)
    pyautogui.click(610, 194)
    time.sleep(1)
    pyautogui.typewrite(str(xx))

    # zuo biao y
    time.sleep(1)
    pyautogui.click(710, 194)
    time.sleep(1)
    pyautogui.typewrite(str(yy))

    # qian wang
    time.sleep(1)
    pyautogui.click(769, 194)


def lian_gong(lian_gong_time):
    print "Start LianGong at {}".format(current_date_time())
    _go_gua_ji_npc()
    pyautogui.click(495, 616)
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('m')
    time.sleep(1)
    pyautogui.click(712, 328)
    time.sleep(1)
    pyautogui.click(418, 262)
    time.sleep(1)
    pyautogui.click(596, 332)
    time.sleep(1)
    pyautogui.click(864, 580)
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(lian_gong_time*60)
    print "LianGong complete at {}".format(current_date_time())
    customize_init()


def go_chu_mo_npc():
    _wo_yao_sheng_ji()
    pyautogui.click(893, 413)
    time.sleep(11)


def seconds_change(total_seconds):
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    return "%02d:%02d:%02d:%02d" % (d, h, m, s)


def capture_pic(cur_time):
    _huo_dong_jie_mian_no_click()
    hwnd = win32gui.GetForegroundWindow()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))

    coordinate = (rect.left + 2, rect.top + 2, rect.right - 2, rect.bottom - 2)
    pic = ImageGrab.grab(coordinate)
    path = "C:\\xingqi{}".format(xing_qi_ji)
    if os.path.exists(path):
        pic.save(path + "\\" + "xingqi" + str(xing_qi_ji) + "_" + str(cur_time) + ".png", quality=100)
    else:
        os.mkdir(path)
        pic.save(path + "\\" + "xingqi" + str(xing_qi_ji) + "_" + str(cur_time) + ".png", quality=100)
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)


def run_time():
    ss = sm.now()
    # put method below
    dd = sm.now()
    print seconds_change((dd - ss).seconds)


# To Do Improve it
def _boss_hui_shou():
    time.sleep(1)
    pyautogui.click(714, 119)
    time.sleep(1)
    pyautogui.click(597, 197)
    time.sleep(1)
    pyautogui.click(719, 617)
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)


def _yin_xiong_jie_mian(ge_su):
    time.sleep(1)
    pyautogui.click(383, 672)
    time.sleep(1)
    if ge_su == 3:
        pyautogui.click(197, 317)
        time.sleep(1)
    elif ge_su == 4:
        pyautogui.click(197, 317)
        time.sleep(1)
    elif ge_su == 5:
        pyautogui.click(197, 317)
        time.sleep(1)
    else:
        pyautogui.click(197, 317)
        time.sleep(1)

    pyautogui.click(628, 206)
    time.sleep(1)
