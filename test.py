import pyautogui
import time
import win32gui
import ctypes
import os
import unittest

from datetime import datetime as sm
from PIL import ImageGrab
from ScreenShot import RECT

pyautogui.PAUSE = 1.5

GongXunTime = 120
JinYinTime = 160

rect = RECT()

class AW1(object):
    def __init__(self, CurrentLevel):
        self.CurrentLevel = CurrentLevel
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
        self.XingQi = self.XingQiJi()
        self.x, self.y = pyautogui.size()

        self.Y = str(sm.now())[0:4]
        self.M = str(sm.now())[5:7]
        self.D = str(sm.now())[8:10]

    def TabQieHuan(self):
        time.sleep(1)
        try:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
        except:
            print "except"
        self.GuaJiFlag = False

    def GongXunRenWu(self, Rtimes, Wtimes):
        print "Start GongXunRenWu at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'JinYanGongXun'
        self.EventTime += 1
        time.sleep(1)
        pyautogui.click(943, 347)

        time.sleep(1)
        pyautogui.click(622, 527)
        time.sleep(8)

        pyautogui.click(509, 567)
        time.sleep(1)

        pyautogui.click(509, 567)

        # deng dai wan cheng
        time.sleep(Wtimes)

        # dian ji di mian (fang zi wa kuang cuo wo)
        pyautogui.click(522, 537)
        time.sleep(1)

        # click chuan
        pyautogui.click(900, 345)
        time.sleep(1)
        pyautogui.click(613, 510)
        time.sleep(1)
        for i in range(Rtimes):
            time.sleep(1)
            pyautogui.click(622, 527)
            time.sleep(8)
            pyautogui.click(509, 567)
            time.sleep(1)

            pyautogui.click(509, 567)
            time.sleep(GongXunTime)
            # dian ji di mian (fang zi wa kuang cuo wo)
            pyautogui.click(522, 537)
            time.sleep(1)
            pyautogui.click(900, 345)
            time.sleep(1)
            pyautogui.click(613, 510)
            time.sleep(1)
        print "GongXunRenWu complete at {}".format(sm.now())
        self.InIt()
        self.GongXunRenWuComplete = True

    def JingYingRenWu(self, Rtimes, Wtimes):
        print "Start JingYingRenWu at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'TianFu'
        self.EventTime += 1

        time.sleep(1)
        pyautogui.click(943, 347)
        time.sleep(1)
        pyautogui.click(509, 567)
        time.sleep(1)
        pyautogui.click(509, 567)
        time.sleep(Wtimes)

        time.sleep(1)
        pyautogui.click(901, 346)

        time.sleep(1)
        pyautogui.click(613, 510)
        time.sleep(1)

        for j in range(Rtimes):
            pyautogui.click(509, 567)
            time.sleep(1)
            pyautogui.click(509, 567)
            time.sleep(JinYinTime)

            time.sleep(1)
            pyautogui.click(901, 346)

            time.sleep(1)
            pyautogui.click(613, 510)
            time.sleep(1)
        print "JingYingRenWu complete at {}".format(sm.now())
        self.InIt()
        self.JingYingRenWuComplete = True

    def TaFangFengMo(self, FengMoTime):
        print "Start TaFangFengMo at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'TaFangFengMo'
        self.EventTime += 1

        # self._BaoWuShenDunJieMian()
        for jj in range(FengMoTime):
            self._GoFengMoNPC()

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
        print "TaFangFengMo Complete at {}".format(sm.now())
        self.InIt()
        self.TaFangFengMoComplete = True

    def ChuangTianGuan(self):
        print "Start ChuangTianGuan at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'ChuangTianGuan'
        self.EventTime += 1

        time.sleep(1)
        pyautogui.click(911, 503)

        time.sleep(1)
        pyautogui.click(507, 600)
        if self.CurrentLevel == 0:
            time.sleep(190)
        elif self.CurrentLevel >0 and self.CurrentLevel <= 2:
            time.sleep(430)
        elif self.CurrentLevel >2 and self.CurrentLevel <= 4:
            time.sleep(790)
        else:
            time.sleep(1300)
        pyautogui.click(511, 514)
        print "ChuangTianGuan Complete at {}".format(sm.now())
        self.InIt()
        self.ChuangTianGuanComplete = True

    def CaiLiaoFuBen(self):
        print "Start CaiLiaoFuBen at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'CaiLiaoFuBen'
        self.EventTime += 1
        time.sleep(1)
        self.GoCaiLiaoNPC()
        for i in range(2):
            if self.CurrentLevel == 0:
                for iii in range(1, 2):
                    moveValue = 30

                    # xiao chu dui hua kuang
                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (iii * moveValue)))

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

                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            elif self.CurrentLevel > 0 and self.CurrentLevel <= 2:
                for iii in range(1, 5, 3):
                    moveValue = 30

                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (iii * moveValue)))

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

                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            elif self.CurrentLevel > 2 and self.CurrentLevel <= 4:
                for iii in range(0, 7):
                    moveValue = 30

                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (iii * moveValue)))

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

                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            else:
                for iii in range(0, 7):
                    moveValue = 30

                    # dian ji NPC
                    time.sleep(1)
                    pyautogui.click(604, 359)
                    time.sleep(1)
                    pyautogui.click(514, (398 + (iii * moveValue)))

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

                    # li kai fu ben / mian fei lin qu jiang li
                    time.sleep(1)
                    pyautogui.click(860, 528)
            # time.sleep(1)
            self.HuiShou()
        print "CaiLiaoFuBen Complete at {}".format(sm.now())
        self.InIt()
        self.CaiLiaoFuBenComplete = True

    def WeiWangRenWu(self):
        print "Start WeiWangRenWu at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'WeiWangRenWu'
        self.EventTime += 1

        self._GoWeiWangNPC()

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
        self._GoWeiWangNPC()

        # wan cheng ren wu
        pyautogui.click(645, 526)
        time.sleep(1)

        ############ task 2 #########################################

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
        self._GoWeiWangNPC()
        # wan cheng ren wu
        pyautogui.click(645, 526)
        time.sleep(1)

        ############ task 3 #########################################
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
        self._GoWeiWangNPC()

        # wan cheng ren wu
        pyautogui.click(645, 526)
        time.sleep(2)

        ############ task 4 #########################################
        pyautogui.click(334, 452)

        # jie qu ren wu
        time.sleep(1)
        pyautogui.click(645, 525)
        time.sleep(1)
        pyautogui.click(684, 487)
        time.sleep(35)

        # chuan
        self._GoWeiWangNPC()

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
        print "WeiWangRenWu complete at {}".format(sm.now())
        self.InIt()
        self.WeiWangRenWuComplete = True

    # def ChuMoRenWu(self, RenWuTime):
    #     print "Start ChuMoRenWu at {}".format(sm.now())
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'ChuMoRenWu'
    #     self.EventTime += 1
    #
    #     # chuan dao Zhang TianShi
    #     self.GoChuMoNPC()
    #
    #     # jin ru jiang jun mu
    #     time.sleep(2)
    #     pyautogui.click(544, 497)
    #     time.sleep(1)
    #
    #     pyautogui.press('esc')
    #     time.sleep(1)
    #     # pyautogui.click(462, 352)
    #     # time.sleep(2)
    #     time.sleep(1)
    #     self._GoTo(63, 25)
    #     # da pai zi
    #     time.sleep(10)
    #     time.sleep(1)
    #     pyautogui.press('esc')
    #     time.sleep(1)
    #     pyautogui.press('z')
    #     time.sleep(RenWuTime*60)
    #     self.GoChuMoNPC()
    #     for i in range(5):
    #         time.sleep(1)
    #         pyautogui.click(551, 571)
    #     time.sleep(1)
    #     pyautogui.press('esc')
    #     print "ChuMoRenWu complete at {}".format(sm.now())
    #     self.InIt()
    #     self.ChuMoRenWuComplete = True

    def ChuMoRenWu(self, RenWuTime):
        print "Start ChuMoRenWu at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'ChuMoRenWu'
        self.EventTime += 1

        # chuan dao Zhang TianShi
        self.GoChuMoNPC()

        # jin ru jiang jun mu
        time.sleep(2)
        pyautogui.click(544, 497)
        time.sleep(1)

        pyautogui.press('esc')
        time.sleep(1)
        # pyautogui.click(462, 352)
        # time.sleep(2)
        time.sleep(1)
        self._GoTo(63, 25)
        # da pai zi
        time.sleep(10)
        self._XiaoChuJieMian()
        pyautogui.press('z')
        time.sleep(RenWuTime*60)
        self.InIt()
        self.GoChuMoNPC()
        for i in range(5):
            time.sleep(1)
            pyautogui.click(551, 571)
        time.sleep(1)
        pyautogui.press('esc')
        print "ChuMoRenWu complete at {}".format(sm.now())
        self.InIt()
        self.ChuMoRenWuComplete = True

    def LianGong(self, LianGongTime):
        print "Start LianGong at {}".format(sm.now())
        self._GoGuJiNPC()
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
        time.sleep(LianGongTime*60)
        print "LianGong complete at {}".format(sm.now())
        self.InIt()

    def HuiShou(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HuiShou'
        self.EventTime += 1

        # # da kai bei bao jie mian
        # time.sleep(1)
        # pyautogui.click(883, 578)
        # time.sleep(1)
        # pyautogui.click(522, 413)
        # time.sleep(2)
        #
        # # hui shou kuangshi
        # pyautogui.click(602, 555)
        # time.sleep(2)
        # # hui shou zhuang bei
        # pyautogui.click(801, 554)
        # time.sleep(2)

        # pyautogui.press('esc')
        # time.sleep(0.5)

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

    def GuaJi(self, HH, MM, SS = 0):
        print "Start Guaji at {}".format(sm.now())
        # print type(self._TimeDiff(HH, MM, SS))
        self.GuaJiFlag = True
        self.CurStatus = 'GuaJi'
        self.EventTime += 1

        self._GoGuJiNPC()
        time.sleep(1)
        if self.CurrentLevel == 0:
            pyautogui.click(394, 418)
        elif self.CurrentLevel >0 and self.CurrentLevel <= 2:
            pyautogui.click(595, 418)
        elif self.CurrentLevel >2 and self.CurrentLevel <= 4:
            pyautogui.click(595, 418)
        else:
            pyautogui.click(494, 446)
        # time.sleep(1)
        # pyautogui.press('esc')
        # time.sleep(1)
        self._XiaoChuJieMian()
        pyautogui.press('z')
        # CurrentTime = sm.now()
        # TargetTimeS = self.Y+'-'+self.M+'-'+self.D+' '+str(HH)+':'+str(MM)+':'+str(SS)+'.0'
        # TargetTime = sm.strptime(TargetTimeS, "%Y-%m-%d %H:%M:%S.%f")
        # self._TimeDiff(HH, MM, SS)
        print "GuaJi shijian is ", self.SecondsChange(self._TimeDiff(HH, MM, SS))
        time.sleep(self._TimeDiff(HH, MM, SS)-10)
        print "GuaJi complete at {}".format(sm.now())
        self.InIt()

    # ToDo imporve it
    def WaKuang(self):
        print "Start WaKuang at {}".format(sm.now())
        self.GuaJiFlag = True
        self.CurStatus = 'WaKuang'
        self.EventTime += 1

        time.sleep(100)
        pyautogui.click(1220, 611)
        time.sleep(1)
        print "WaKuang Complete at {}".format(sm.now())
        self.InIt()

    def RiMoBaiChengZhu(self):
        print "Start MoBaiChengZhu at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'MoBaiChengZhu'
        self.EventTime += 1

        time.sleep(1)
        self._HuoDongJieMian()
        pyautogui.click(701, 458)

        for i in range(9):
            time.sleep(1)
            for i in range(4):
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
        print "MoBaiChengZhu complete at {}".format(sm.now())
        self.InIt()
        self.MoBaiChengZhuComplete = True

    def RiYeZhanBiQi(self):
        print "Start YeZhanBiQi at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'YeZhanBiQi'
        self.EventTime += 1

        self._HuoDongJieMian()
        # pyautogui.click(701, 458)
        # time.sleep(1)
        pyautogui.click(508, 609)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1200)
        print "YeZhanBiQi complete at {}".format(sm.now())
        self.InIt()
        self.YeZhanBiQiComplete = True

    def RiShenWei(self, ShenWeiTimeMinutes):
        print "Start ShenWei at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'ShenWei'
        self.EventTime += 1

        self._HuoDongJieMian()

        # jin ru shen wei
        pyautogui.click(510, 607)
        time.sleep(1)
        # pyautogui.click(701, 458)
        # time.sleep(1)
        # pyautogui.click(508, 606)
        # time.sleep(1)

        self._XiaoChuJieMian()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(self.Seconds*ShenWeiTimeMinutes)
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
        print "ShenWei complete at {}".format(sm.now())
        self.InIt()
        self.ShenWeiComplete = True

    def RiWorldBoss(self):
        print "Start WorldBoss at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'WorldBoss'
        self.EventTime += 1

        time.sleep(1)
        self._HuoDongJieMian()
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
        print "WorldBoss complete at {}".format(sm.now())
        self.InIt()
        self.WorldBossComplete = True

    def RiJinZhuSongLi(self):
        print "Start JinZhuSongLi at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'JinZhuSongLi'
        self.EventTime += 1

        self._HuoDongJieMian()

        # can yu huo dong
        time.sleep(2)
        pyautogui.click(508, 596)
        time.sleep(2)
        # pyautogui.press('esc')
        # time.sleep(1)
        # pyautogui.press('z')
        # time.sleep(1)
        time.sleep(300)
        print "JinZhuSongLi complete at {}".format(sm.now())
        self.InIt()
        # self.JingYingRenWuComplete = True

    def GeRenBoss(self):
        print "Start GeRenBoss at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'GeRenBoss'
        self.EventTime += 1

        if self.CurrentLevel == 0:
            for i in range(3):
                # ge ren boss
                time.sleep(1)
                pyautogui.click(713, 116)
                time.sleep(1)
                pyautogui.click(346, 196)

                # boss ming zi
                time.sleep(1)
                pyautogui.click(261, (255 + (i * 40)))
                time.sleep(1)
                pyautogui.click(785, 617)
                time.sleep(0.5)
                pyautogui.press('z')
                time.sleep(1)
                if i == 0:
                    time.sleep(30 + (i * 15))
                elif i == 1:
                    time.sleep(40 + (i * 15))
                else:
                    time.sleep(50 + (i * 15))
                time.sleep(1)
                pyautogui.click(859, 533)
        elif self.CurrentLevel > 0 and self.CurrentLevel <= 2:
            for i in range(4):
                # ge ren boss
                time.sleep(1)
                pyautogui.click(713, 116)
                time.sleep(1)
                pyautogui.click(346, 196)

                # boss ming zi
                time.sleep(1)
                pyautogui.click(261, (255 + (i * 40)))
                time.sleep(1)
                pyautogui.click(785, 617)
                time.sleep(0.5)
                pyautogui.press('z')
                time.sleep(1)
                if i == 0:
                    time.sleep(30 + (i * 15))
                elif i == 1:
                    time.sleep(40 + (i * 15))
                elif i == 2:
                    time.sleep(50 + (i * 15))
                else:
                    time.sleep(60 + (i * 15))
                time.sleep(1)
                pyautogui.click(859, 533)
        elif self.CurrentLevel > 2 and self.CurrentLevel <= 4:
            for i in range(5):
                # ge ren boss
                time.sleep(1)
                pyautogui.click(713, 116)
                time.sleep(1)
                pyautogui.click(346, 196)

                # boss ming zi
                time.sleep(1)
                pyautogui.click(261, (255 + (i * 40)))
                time.sleep(1)
                pyautogui.click(785, 617)
                time.sleep(0.5)
                pyautogui.press('z')
                time.sleep(1)
                if i == 0:
                    time.sleep(30 + (i * 15))
                elif i == 1:
                    time.sleep(40 + (i * 15))
                elif i == 2:
                    time.sleep(50 + (i * 15))
                elif i == 3:
                    time.sleep(55 + (i * 15))
                else:
                    time.sleep(60 + (i * 15))
                time.sleep(1)
                pyautogui.click(859, 533)
        else:
            for i in range(6):
                # ge ren boss
                time.sleep(1)
                pyautogui.click(713, 116)
                time.sleep(1)
                pyautogui.click(346, 196)

                # boss ming zi
                time.sleep(1)
                pyautogui.click(261, (255 + (i * 40)))
                time.sleep(1)
                pyautogui.click(785, 617)
                time.sleep(0.5)
                pyautogui.press('z')
                time.sleep(1)
                if i == 0:
                    time.sleep(30 + (i * 15))
                elif i == 1:
                    time.sleep(40 + (i * 15))
                elif i == 2:
                    time.sleep(50 + (i * 15))
                elif i == 3:
                    time.sleep(53 + (i * 15))
                elif i == 4:
                    time.sleep(58 + (i * 15))
                else:
                    time.sleep(65 + (i * 18))
                time.sleep(1)
                pyautogui.click(859, 533)
        print "GeRenBoss complete at {}".format(sm.now())
        self.InIt()
        self.GeRenBossiComplete = True

    def InIt(self):
        # time.sleep(0.5)
        # pyautogui.click(951, 714)
        # time.sleep(1)
        # pyautogui.press('esc')
        # time.sleep(0.5)
        self._XiaoChuJieMian()
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

    def _WoYaoShengJi(self):
        time.sleep(1)
        pyautogui.click(335, 673)
        time.sleep(1)
        pyautogui.click(199, 212)
        time.sleep(1)
        pyautogui.click(576, 601)
        time.sleep(1)
        pyautogui.click(410, 214)
        time.sleep(1)

    def _GoFengMoNPC(self):
        time.sleep(1)
        pyautogui.click(337, 674)
        time.sleep(1)
        pyautogui.click(575, 598)
        time.sleep(1)
        pyautogui.click(412, 214)
        time.sleep(1)
        pyautogui.click(892, 220)
        # time.sleep(1)
        # pyautogui.click(614, 339)
        # time.sleep(1)
        # pyautogui.click(518, 636)
        # time.sleep(1)
        # pyautogui.press('esc')

    def _GoWeiWangNPC(self):
        self.InIt()
        time.sleep(1)
        pyautogui.click(777, 206, button='right')
        time.sleep(1)
        pyautogui.click(659, 205)
        time.sleep(2)

    def _HuoDongJieMian(self):
        time.sleep(0.5)
        pyautogui.click(951, 714)
        time.sleep(0.5)
        pyautogui.press('j')
        time.sleep(1)
        pyautogui.click(750, 615)
        time.sleep(0.5)

    def _ViewHuoDongJieMianNoClick(self):
        time.sleep(0.5)
        pyautogui.click(951, 714)
        time.sleep(0.5)
        pyautogui.press('j')
        # time.sleep(1)
        # pyautogui.click(750, 615)
        time.sleep(0.5)

    def RiBiGuan(self):
        print "Start BiGuan at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'BiGuan'
        self.EventTime += 1
        time.sleep(1)
        self._HuoDongJieMian()
        pyautogui.click(509, 609)

        # xiao chu jie mian
        time.sleep(0.5)
        pyautogui.press('esc')

        # di tu
        time.sleep(1)
        pyautogui.press('m')

        if self.CurrentLevel >=4:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(613, 210)
            time.sleep(1)
            pyautogui.typewrite('31')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(713, 209)
            time.sleep(1)
            pyautogui.typewrite('26')
        elif self.CurrentLevel == 0:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(613, 210)
            time.sleep(1)
            pyautogui.typewrite('27')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(713, 209)
            time.sleep(1)
            pyautogui.typewrite('30')
        elif self.CurrentLevel > 0 and self.CurrentLevel < 4:
            # zuo biao x
            time.sleep(1)
            pyautogui.click(613, 210)
            time.sleep(1)
            pyautogui.typewrite('32')

            # zuo biao y
            time.sleep(1)
            pyautogui.click(713, 209)
            time.sleep(1)
            pyautogui.typewrite('35')

        # qian wang di dian
        time.sleep(1)
        pyautogui.click(770, 209)

        # zai ci dian ji
        time.sleep(1)
        pyautogui.click(770, 209)
        time.sleep(1200)

        time.sleep(1)
        pyautogui.press('esc')
        print "BiGuan complete at {}".format(sm.now())
        self.InIt()
        # flag
        self.BiGuanComplete = True

    def RiGuaiWuGongCheng(self):
        print "Start GuaiWuGongCheng at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'GuaiWuGongCheng'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()
        pyautogui.click(701, 458)
        # gua ji ban ge xiao shi
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1750)
        print "GuaiWuGongCheng complete at {}".format(sm.now())
        self.InIt()
        self.GuaiWuGongChengComplete = False

    def RiSuoYaoTa(self):
        print "Start RiSuoYaoTa at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'RiSuoYaoTa'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()
        pyautogui.click(510, 396)
        # gua ji ban ge xiao shi
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1750)
        print "RiSuoYaoTa complete at {}".format(sm.now())
        self.InIt()
        self.SuoYaoTaComplete = True

    def RiDuoBeiYaSong(self):
        print "Start RiDuoBeiYaSong at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'RiDuoBeiYaSong'
        self.EventTime += 1
        time.sleep(1)
        # for i in range(3):
        # self._HuoDongJieMian()
        # pyautogui.click(885, 601)
        # time.sleep(1)
        for ii in range(3):
            self._BaoWuJieMian(3)

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
        # # ji xu ya yun
        # time.sleep(1)
        # pyautogui.click(436, 500)

        # jie qu ren wu jie mian dian ji
        # pyautogui.click(510, 582)
        # time.sleep(1)
        #
        # # shua xin
        # for i in range(10):
        #     time.sleep(1)
        #     pyautogui.click(471, 551)
        # # hu song
        # time.sleep(1)
        # pyautogui.click(758, 550)
        # time.sleep(300)
        #
        # # ji xu ya yun
        # time.sleep(1)
        # pyautogui.click(436, 500)
        #
        # # jie qu ren wu jie mian dian ji
        # pyautogui.click(510, 582)
        # time.sleep(1)
        #
        # # shua xin
        # for i in range(10):
        #     time.sleep(1)
        #     pyautogui.click(471, 551)
        # # hu song
        # time.sleep(1)
        # pyautogui.click(758, 550)
        # time.sleep(300)
        # # if i == 0:
        # #     pyautogui.press('esc')
        # #     time.sleep(300)
        # # else:
        # # pyautogui.press('esc')
        # # time.sleep(900)
        # # pyautogui.click(582, 499)
        # # que ding
        # time.sleep(1)
        # pyautogui.click(581, 502)
        # time.sleep(1)
        print "RiDuoBeiYaSong complete at {}".format(sm.now())
        self.InIt()
        self.DuoBeiYaSongComplete = True

    def RiSanBeiLianGong(self, LTime):
        print "Start SanBeiLianGong at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'SanBeiLianGong'
        self.EventTime += 1

        self.LianGong(LTime)
        print "SanBeiLianGong complete at {}".format(sm.now())
        self.InIt()
        self.SanBeiLianGongComplete = True

    def RiJiaLanShenDian(self):
        print "Start JiaLanShenDian at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'JiaLanShenDian'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()
        pyautogui.click(510, 599)
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(20)
        print "JiaLanShenDian complete at {}".format(sm.now())
        self.InIt()
        self.JiaLanShenDianComplete = True

    # To Do
    def RiHaiTianShengYan(self):
        print "Start HaiTianShengYan at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'HaiTianShengYan'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()
        pyautogui.click(508, 607)
        # time.sleep(1)
        # pyautogui.press('esc')
        # time.sleep(1)
        self._XiaoChuJieMian()
        pyautogui.press('z')
        time.sleep(900)

        # NPC part and delay part
        print "HaiTianShengYan complete at {}".format(sm.now())
        self.InIt()
        self.HaiTianShengYanComplete = True

    def RiShiMuMiZhen(self):
        print "Start ShiMuMiZhen at {}".format(sm.now())
        self.GuaJiFlag = False
        self.CurStatus = 'RiShiMuMiZhen'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()
        pyautogui.click(508, 597)
        time.sleep(5)
        # ToDo
        # NPC part and delay part
        print "ShiMuMiZhen complete at {}".format(sm.now())
        self.InIt()
        self.ShiMuMiZhenComplete = True

    def _BossJieMian(self):
        # da kai boss jie mian
        time.sleep(1)
        pyautogui.click(715, 188)
        time.sleep(1)

    def _GoGuJiNPC(self):
        self._XiaoChuJieMian()
        time.sleep(1)
        pyautogui.click(570, 677)
        time.sleep(1)
        pyautogui.click(200, 212)
        time.sleep(1)
        pyautogui.click(793, 610)
        time.sleep(1)

    def GoChuMoNPC(self):
        self._WoYaoShengJi()
        pyautogui.click(893, 413)
        time.sleep(11)

    def GoCaiLiaoNPC(self):
        self._BaoWuShenDunJieMian()

    def _BaoWuShenDunJieMian(self):
        # da kai bao wu jie mian
        self.InIt()
        time.sleep(1)
        pyautogui.click(570, 677)
        time.sleep(1)
        pyautogui.click(198, 269)
        time.sleep(1)
        pyautogui.click(793, 569)
        time.sleep(1)
        pyautogui.press('esc')

    # def _BaoWuGuanZhiJieMian(self):
    #     # da kai bao wu jie mian
    #     time.sleep(1)
    #     pyautogui.click(569, 636)
    #     time.sleep(1)
    #     pyautogui.click(197, 304)
    #     time.sleep(1)
    #     pyautogui.click(792, 591)
    #     time.sleep(1)
    #
    # def _BaoWuLongHunJieMian(self):
    #     # da kai bao wu jie mian
    #     time.sleep(1)
    #     pyautogui.click(569, 636)
    #     time.sleep(1)
    #     pyautogui.click(197, 359)
    #     time.sleep(1)
    #     pyautogui.click(792, 591)
    #     time.sleep(1)

    def _BaoWuJieMian(self, level):
        # da kai bao wu jie mian
        self._XiaoChuJieMian()
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
        # time.sleep(1)
        # if SubLevel == 1:
        #     time.sleep(1)
        #     pyautogui.click(793, 551)
        # elif level == 2:
        #     pyautogui.click(792, 591)
        #     time.sleep(1)

    # def BaoWuXueYuJieMian(self):
    #     # da kai bao wu jie mian
    #     pyautogui.click(569, 636)
    #
    # def BaoWuShenDunJieMian(self):
    #     # da kai bao wu jie mian
    #     time.sleep(1)
    #     pyautogui.click(569, 636)
    #     time.sleep(1)
    #     pyautogui.click(197, 250)
    #
    # def BaoWuGuanZhiJieMian(self):
    #     # da kai bao wu jie mian
    #     pyautogui.click(569, 636)
    #     time.sleep(1)
    #     pyautogui.click(197, 304)
    #
    # def BaoWuLongHunJieMian(self):
    #     time.sleep(1)
    #     pyautogui.click(569, 636)
    #     time.sleep(1)
    #     pyautogui.click(197, 359)
    #
    # def BaoWuLongPoJieMian(self):
    #     time.sleep(1)
    #     pyautogui.click(569, 636)
    #     time.sleep(1)
    #     pyautogui.click(197, 410)
    #     time.sleep(1)
    #
    # def JinYinRenWuNPC(self):
    #     self._ClickCenter()
    #     time.sleep(1)
    #     pyautogui.click(792, 591)
    #     time.sleep(1)
    #     pyautogui.press('esc')

    # def _ClickCenter(self):
    #     time.sleep(0.5)
    #     pyautogui.click(self.x / 2, self.y / 2)
    #     time.sleep(0.5)

    # To Do
    def _GoTo(self, xx, yy):
        self._XiaoChuJieMian()
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

    # def _TestScorll(self, ScorValue):
    #     print ScorValue
    #     time.sleep(5)
    #     pyautogui.scroll(100)
    #     time.sleep(0.5)
    #     pyautogui.scroll(100)
    #     time.sleep(0.5)
    #     pyautogui.scroll(100)
    #     time.sleep(0.5)
    #     pyautogui.scroll(100)
    #     time.sleep(0.5)
    #     pyautogui.scroll(100)
    #     time.sleep(0.5)
    #     pyautogui.scroll(100)
    #     time.sleep(5)
    #     pyautogui.scroll(-100)
    #     time.sleep(0.5)
    #     pyautogui.scroll(-100)
    #     time.sleep(0.5)
    #     pyautogui.scroll(-100)
    #     time.sleep(0.5)
    #     pyautogui.scroll(-100)
    #     time.sleep(0.5)
    #     pyautogui.scroll(-100)
    #     time.sleep(0.5)
    #     pyautogui.scroll(-100)

    #@classmethod
    def _TimeDiff(self, HH, MM = 0, SS = 0):
        CurrentTime = sm.now()
        TargetTimeS = self.Y+'-'+self.M+'-'+self.D+' '+str(HH)+':'+str(MM)+':'+str(SS)+'.0'
        TargetTime = sm.strptime(TargetTimeS, "%Y-%m-%d %H:%M:%S.%f")

        return (TargetTime-CurrentTime).seconds

    def CeShi(self, HH, MM, SS):
        CurrentyTime = sm.now()
        # ta = time.strptime(sm.now(), "%Y-%m-%d %H:%M:%S")
        print "CurrentyTime = ", CurrentyTime

        TargetTimeS = self.Y+'-'+self.M+'-'+self.D+' '+str(HH)+':'+str(MM)+':'+str(SS)+'.0'
        # TargetTime = sm.strptime(self.Y, self.M, self.D, HH, MM, SS)

        TargetTime = sm.strptime(TargetTimeS, "%Y-%m-%d %H:%M:%S.%f")
        # tb = time.strptime(TargetTime, "%Y-%m-%d %H:%M:%S")
        print "TargetTime = ", TargetTime

        print (TargetTime - CurrentyTime)
        print (TargetTime - CurrentyTime).seconds

    def CurrentDateTime(self):
        x = str(sm.now())
        return x[5:19]

    def TestPlay(self, s):
        print "start play in %s" %(s)
        print sm.now()

    def TestGuaJi(self, HH, MM, SS):
        print "StartGuaJi"
        print self._TimeDiff(HH, MM, SS)

        #print time.localtime(self._TimeDiff(HH, MM, SS))


        m, s = divmod(self._TimeDiff(HH, MM, SS), 60)
        h, m = divmod(m, 60)

        print "%02d:%02d:%02d" % (h, m, s)
        time.sleep(self._TimeDiff(HH, MM, SS)+10)

    @classmethod
    def SecondsChange(self, TotalSeconds):
        m, s = divmod(TotalSeconds, 60)
        h, m = divmod(m, 60)

        return "%02d:%02d:%02d" % (h, m, s)

    def LinQuHuoYueJiangLi(self):
        self._XiaoChuJieMian()
        time.sleep(1)
        pyautogui.click(260, 128)
        for i in range(5):
            time.sleep(1)
            pyautogui.click(766, (373+i*57))
            time.sleep(1)
            # pyautogui.click(766, 602)

    def XingQiJi(self):
        xingqiji = sm.now()
        return xingqiji.weekday()

    def CapturePic(self, CurTime):
        self._ViewHuoDongJieMianNoClick()
        HWND = win32gui.GetForegroundWindow()
        ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))

        coordinate = (rect.left + 2, rect.top + 2, rect.right - 2, rect.bottom - 2)
        pic = ImageGrab.grab(coordinate)
        path = "C:\\xingqi{}".format(self.XingQi)
        if os.path.exists(path):
            pic.save(path + "\\" + "xingqi" + str(self.XingQi) + "_" + str(CurTime) + ".png", quality=100)
        else:
            os.mkdir(path)
            pic.save(path + "\\" + "xingqi" + str(self.XingQi) + "_" + str(CurTime) + ".png", quality=100)
        time.sleep(1)
        # time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)

    # ToDo
    def DaBoss(self):
        pass

    def RunTime(self):
        SS = sm.now()
        # put method below
        DD = sm.now()
        print self.SecondsChange((DD - SS).seconds)

    def _XiaoChuJieMian(self):
        time.sleep(0.5)
        pyautogui.click(951, 714, button='right')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(0.5)

    #To do
    def _WoYaoBianQiangJieMian(self):
        pass

    # To Do
    def ReStart(self):
        pass

    # To Do
    def GuaSuoYaoTa(self, GuaTime):
        self._GoGuJiNPC()
        self._XiaoChuJieMian()

        time.sleep(1)
        pyautogui.click(654, 390)

        if self.CurrentLevel == 0:
            time.sleep(1)
            pyautogui.click(515, 397)
        elif self.CurrentLevel > 0 and self.CurrentLevel <= 2:
            time.sleep(1)
            pyautogui.click(515, 426)
        elif self.CurrentLevel > 2 and self.CurrentLevel <= 4:
            time.sleep(1)
            pyautogui.click(515, 453)
        elif self.CurrentLevel > 4 and self.CurrentLevel <= 6:
            time.sleep(1)
            pyautogui.click(515, 483)
        elif self.CurrentLevel > 6 and self.CurrentLevel <= 8:
            time.sleep(1)
            pyautogui.click(515, 511)
        else:
            time.sleep(1)
            pyautogui.click(515, 539)
        while True:
            self._XiaoChuJieMian()
            pyautogui.press('z')
            time.sleep(self.Seconds * GuaTime)
            pyautogui.click(854, 684)
            time.sleep(1)
            pyautogui.click(310, 204)
            time.sleep(1)
            for i in range(8):
                time.sleep(2)
                pyautogui.doubleClick(197, 271)
                time.sleep(0.5)
            pyautogui.press('esc')
            self._BossHuiShou()
            self._XiaoChuJieMian()
            pyautogui.press('z')

    def DaSuoYaoTa(self,GuaTime):
        self._GoGuJiNPC()
        self._XiaoChuJieMian()

        time.sleep(1)
        pyautogui.click(654, 390)

        if self.CurrentLevel == 0:
            time.sleep(1)
            pyautogui.click(515, 397)
        elif self.CurrentLevel > 0 and self.CurrentLevel <= 2:
            time.sleep(1)
            pyautogui.click(515, 426)
        elif self.CurrentLevel > 2 and self.CurrentLevel <= 4:
            time.sleep(1)
            pyautogui.click(515, 453)
        elif self.CurrentLevel > 4 and self.CurrentLevel <= 6:
            time.sleep(1)
            pyautogui.click(515, 483)
        elif self.CurrentLevel > 6 and self.CurrentLevel <= 8:
            time.sleep(1)
            pyautogui.click(515, 511)
        else:
            time.sleep(1)
            pyautogui.click(515, 539)

        self._XiaoChuJieMian()
        pyautogui.press('z')
        time.sleep(self.Seconds*GuaTime)
        pyautogui.click(854, 684)
        time.sleep(1)
        pyautogui.click(310, 204)
        time.sleep(1)
        for i in range(6):
            time.sleep(2)
            pyautogui.doubleClick(197, 271)
            time.sleep(0.5)
        pyautogui.press('esc')
        self._BossHuiShou()
        self._XiaoChuJieMian()
        pyautogui.press('z')

    def _BossHuiShou(self):
        time.sleep(1)
        pyautogui.click(714, 119)
        time.sleep(1)
        pyautogui.click(597, 197)
        time.sleep(1)
        pyautogui.click(719, 617)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)


