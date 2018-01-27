import pyautogui
import time

from datetime import datetime as sm

pyautogui.PAUSE = 1.5

GongXunTime = 120
JinYinTime = 160

class AW1(object):
    def __init__(self, CurrentLevel):
        self.CurrentLevel = CurrentLevel
        self.GuaJiFlag = True
        self.CurStatus = 'null'
        self.Complete = False
        self.EventTime = 0
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
        print "Start GongXunRenWu at {}".format(self.CurrentDateTime())
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
        print "GongXunRenWu complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.GongXunRenWuComplete = True

    def JingYingRenWu(self, Rtimes, Wtimes):
        print "Start JingYingRenWu at {}".format(self.CurrentDateTime())
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
        print "JingYingRenWu complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.JingYingRenWuComplete = True

    def TaFangFengMo(self, FengMoTime):
        print "Start TaFangFengMo at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = False
        self.CurStatus = 'TaFangFengMo'
        self.EventTime += 1

        # self._BaoWuShenDunJieMian()
        for jj in range(FengMoTime):
            self._GoFengMoNPC()

            # dian NPC
            time.sleep(1)
            pyautogui.click(610, 337)

            # jin ru feng mo gu
            time.sleep(1)
            pyautogui.click(505, 593)

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
            pyautogui.click(606, 381)
        print "TaFangFengMo Complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.TaFangFengMoComplete = True

    def ChuangTianGuan(self):
        print "Start ChuangTianGuan at {}".format(self.CurrentDateTime())
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
        print "ChuangTianGuan Complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.ChuangTianGuanComplete = True

    def CaiLiaoFuBen(self):
        print "Start CaiLiaoFuBen at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = False
        self.CurStatus = 'CaiLiaoFuBen'
        self.EventTime += 1
        time.sleep(1)

        for i in range(2):
            if self.CurrentLevel == 0:
                for iii in range(1, 2):
                    moveValue = 30

                    # xiao chu dui hua kuang
                    self.GoCaiLiaoNPC()

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

                    # xiao chu dui hua kuang
                    self.GoCaiLiaoNPC()

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

                    # xiao chu dui hua kuang
                    self.GoCaiLiaoNPC()

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

                    # xiao chu dui hua kuang
                    self.GoCaiLiaoNPC()

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
        print "CaiLiaoFuBen Complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.CaiLiaoFuBenComplete = True

    def WeiWangRenWu(self):
        print "Start WeiWangRenWu at {}".format(self.CurrentDateTime())
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
        pyautogui.press('esc')
        print "WeiWangRenWu complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.WeiWangRenWuComplete = True

    def ChuMoRenWu(self):
        print "Start ChuMoRenWu at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = False
        self.CurStatus = 'ChuMoRenWu'
        self.EventTime += 1

        # chuan dao Zhang TianShi
        self.GoChuMoNPC()

        # jin ru jiang jun mu
        time.sleep(2)
        pyautogui.click(544, 497)
        # sui ji fei
        time.sleep(1)
        pyautogui.press('e')

        # da pai zi
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(3600)
        self.GoChuMoNPC()
        for i in range(5):
            time.sleep(1)
            pyautogui.click(551, 571)
        time.sleep(1)
        pyautogui.press('esc')
        print "ChuMoRenWu complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.ChuMoRenWuComplete = True

    def LianGong(self):
        print "Start LianGong at {}".format(self.CurrentDateTime())
        self.GoGuJiNPC()
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
        time.sleep(1200)
        print "LianGong complete at {}".format(self.CurrentDateTime())
        self.InIt()

    def HuiShou(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HuiShou'
        self.EventTime += 1

        # da kai bei bao jie mian
        time.sleep(1)
        pyautogui.click(883, 578)
        time.sleep(1)
        pyautogui.click(522, 413)
        time.sleep(2)

        # hui shou kuangshi
        pyautogui.click(602, 555)
        time.sleep(2)
        # hui shou zhuang bei
        pyautogui.click(801, 554)
        time.sleep(2)

        pyautogui.press('esc')
        time.sleep(0.5)

        for i in range(2):
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
        print "Start Guaji at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = True
        self.CurStatus = 'GuaJi'
        self.EventTime += 1

        # self.InIt()
        self.GoGuJiNPC()

        time.sleep(1)
        if self.CurrentLevel == 0:
            pyautogui.click(394, 418)
        elif self.CurrentLevel >0 and self.CurrentLevel <= 2:
            pyautogui.click(595, 418)
        elif self.CurrentLevel >2 and self.CurrentLevel <= 4:
            pyautogui.click(494, 446)
        else:
            pyautogui.click(494, 446)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('z')
        # CurrentTime = sm.now()
        # TargetTimeS = self.Y+'-'+self.M+'-'+self.D+' '+str(HH)+':'+str(MM)+':'+str(SS)+'.0'
        # TargetTime = sm.strptime(TargetTimeS, "%Y-%m-%d %H:%M:%S.%f")
        # self._TimeDiff(HH, MM, SS)
        time.sleep(self._TimeDiff(HH, MM, SS))
        print "GuaJi complete at {}".format(self.CurrentDateTime())
        self.InIt()

    # ToDo imporve it
    def WaKuang(self):
        print "Start WaKuang at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = True
        self.CurStatus = 'WaKuang'
        self.EventTime += 1

        time.sleep(100)
        pyautogui.click(1220, 611)
        time.sleep(1)
        print "WaKuang Complete at {}".format(self.CurrentDateTime())
        self.InIt()

    def RiMoBaiChengZhu(self):
        print "Start MoBaiChengZhu at {}".format(self.CurrentDateTime())
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
        print "MoBaiChengZhu complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.MoBaiChengZhuComplete = True

    def RiYeZhanBiQi(self):
        print "Start YeZhanBiQi at {}".format(self.CurrentDateTime())
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
        print "YeZhanBiQi complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.YeZhanBiQiComplete = True

    def RiShenWei(self):
        print "Start ShenWei at {}".format(self.CurrentDateTime())
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
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(900)
        time.sleep(2)
        for i in range(9):
            pyautogui.click(889, 578)
            time.sleep(1)
            pyautogui.click(889, 578)
            time.sleep(45)
            pyautogui.click(511, 600)
        # li kai
        time.sleep(1)
        pyautogui.click(911, 566)
        # que ding
        time.sleep(1)
        pyautogui.click(448, 455)
        print "ShenWei complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.ShenWeiComplete = True

    def RiWorldBoss(self):
        print "Start WorldBoss at {}".format(self.CurrentDateTime())
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
        # pyautogui.click(909, 685)
        # time.sleep(1)
        # pyautogui.press('e')
        print "WorldBoss complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.WorldBossComplete = True

    def RiJinZhuSongLi(self):
        print "Start JinZhuSongLi at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = False
        self.CurStatus = 'JinZhuSongLi'
        self.EventTime += 1

        self._HuoDongJieMian()
        # can yu huo dong
        pyautogui.click(508, 596)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1)
        time.sleep(900)
        print "JinZhuSongLi complete at {}".format(self.CurrentDateTime())
        self.InIt()
        # self.JingYingRenWuComplete = True

    def GeRenBoss(self):
        print "Start GeRenBoss at {}".format(self.CurrentDateTime())
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
                time.sleep(30 + (i * 18))
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
                time.sleep(30 + (i * 18))
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
                time.sleep(30 + (i * 18))
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
                time.sleep(30 + (i * 18))
                time.sleep(1)
                pyautogui.click(859, 533)
        print "GeRenBoss complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.GeRenBossiComplete = True

    def InIt(self):
        time.sleep(0.5)
        pyautogui.click(951, 714)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(0.5)
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

    def _WoYaoBianQaing(self):
        time.sleep(1)
        pyautogui.click(335, 673)
        time.sleep(1)
        pyautogui.click(199, 212)
        time.sleep(1)
        pyautogui.click(576, 601)
        time.sleep(1)
        pyautogui.click(946, 413)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.click(462, 352)

    def _GoFengMoNPC(self):
        time.sleep(1)
        pyautogui.click(337, 674)
        time.sleep(1)
        pyautogui.click(575, 598)
        time.sleep(1)
        pyautogui.click(412, 214)
        time.sleep(1)
        pyautogui.click(946, 221)
        time.sleep(1)
        pyautogui.press('esc')
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

    def RiBiGuan(self):
        print "Start BiGuan at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = False
        self.CurStatus = 'BiGuan'
        self.EventTime += 1
        time.sleep(1)
        self._HuoDongJieMian()
        pyautogui.click(509, 609)
        # di tu
        time.sleep(1)
        pyautogui.press('m')

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

        # qian wang di dian
        time.sleep(1)
        pyautogui.click(770, 209)
        time.sleep(1)
        pyautogui.click(770, 209)
        time.sleep(1200)

        time.sleep(1)
        pyautogui.press('esc')
        print "BiGuan complete at {}".format(self.CurrentDateTime())
        self.InIt()
        # flag
        self.BiGuanComplete = True

    def RiGuaiWuGongCheng(self):
        print "Start GuaiWuGongCheng at {}".format(self.CurrentDateTime())
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
        print "GuaiWuGongCheng complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.GuaiWuGongChengComplete = False

    def RiSuoYaoTa(self):
        print "Start RiSuoYaoTa at {}".format(self.CurrentDateTime())
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
        print "RiSuoYaoTa complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.SuoYaoTaComplete = True

    def RiDuoBeiYaSong(self):
        print "Start RiDuoBeiYaSong at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = False
        self.CurStatus = 'RiDuoBeiYaSong'
        self.EventTime += 1
        time.sleep(1)
        for i in range(3):
            self._HuoDongJieMian()
            pyautogui.click(510, 582)
            time.sleep(1)
            for i in range(8):
                time.sleep(1)
                pyautogui.click(649, 542)
            time.sleep(1)
            pyautogui.click(938, 549)
            if i == 0:
                pyautogui.press('esc')
                time.sleep(300)
            else:
                pyautogui.press('esc')
                time.sleep(300)
            pyautogui.click(582, 499)
        print "RiDuoBeiYaSong complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.DuoBeiYaSongComplete = True

    def RiSanBeiLianGong(self):
        print "Start SanBeiLianGong at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = False
        self.CurStatus = 'SanBeiLianGong'
        self.EventTime += 1

        self.LianGong()
        print "SanBeiLianGong complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.SanBeiLianGongComplete = True

    def RiJiaLanShenDian(self):
        print "Start JiaLanShenDian at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = False
        self.CurStatus = 'JiaLanShenDian'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()
        pyautogui.click(510, 599)
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(3600)
        print "JiaLanShenDian complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.JiaLanShenDianComplete = True

    def RiHaiTianShengYan(self):
        print "Start HaiTianShengYan at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = False
        self.CurStatus = 'HaiTianShengYan'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()
        pyautogui.click(508, 607)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(900)

        # NPC part and delay part
        print "HaiTianShengYan complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.HaiTianShengYanComplete = True

    def RiShiMuMiZhen(self):
        print "Start ShiMuMiZhen at {}".format(self.CurrentDateTime())
        self.GuaJiFlag = False
        self.CurStatus = 'RiShiMuMiZhen'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()
        pyautogui.click(508, 597)
        time.sleep(5)
        # ToDo
        # NPC part and delay part
        print "ShiMuMiZhen complete at {}".format(self.CurrentDateTime())
        self.InIt()
        self.ShiMuMiZhenComplete = True

    def _BossJieMian(self):
        # da kai boss jie mian
        time.sleep(1)
        pyautogui.click(715, 188)
        time.sleep(1)

    def GoGuJiNPC(self):
        self.InIt()
        time.sleep(1)
        pyautogui.click(570, 677)
        time.sleep(1)
        pyautogui.click(200, 212)
        time.sleep(1)
        pyautogui.click(793, 610)
        time.sleep(1)

    def GoChuMoNPC(self):
        # self.InIt()
        self._WoYaoBianQaing()

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

    def _BaoWuGuanZhiJieMian(self):
        # da kai bao wu jie mian
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.click(197, 304)
        time.sleep(1)
        pyautogui.click(792, 591)
        time.sleep(1)

    def _BaoWuLongHunJieMian(self):
        # da kai bao wu jie mian
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.click(197, 359)
        time.sleep(1)
        pyautogui.click(792, 591)
        time.sleep(1)

    def _BaoWuLongPoJieMian(self):
        # da kai bao wu jie mian
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.click(197, 410)
        time.sleep(1)
        pyautogui.click(792, 591)
        time.sleep(1)

    def BaoWuXueYuJieMian(self):
        # da kai bao wu jie mian
        pyautogui.click(569, 636)

    def BaoWuShenDunJieMian(self):
        # da kai bao wu jie mian
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.click(197, 250)

    def BaoWuGuanZhiJieMian(self):
        # da kai bao wu jie mian
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.click(197, 304)

    def BaoWuLongHunJieMian(self):
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.click(197, 359)

    def BaoWuLongPoJieMian(self):
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.click(197, 410)
        time.sleep(1)

    def JinYinRenWuNPC(self):
        self._ClickCenter()
        time.sleep(1)
        pyautogui.click(792, 591)
        time.sleep(1)
        pyautogui.press('esc')

    def _ClickCenter(self):
        time.sleep(0.5)
        pyautogui.click(self.x / 2, self.y / 2)
        time.sleep(0.5)

    # To Do
    def _GoTo(self, xx, yy):
        self._ClickCenter()
        # di tu
        time.sleep(1)
        pyautogui.press('m')
        time.sleep(1)
        pyautogui.click(612, 175)
        time.sleep(1)
        pyautogui.typewrite(xx)

        # zuo biao y
        time.sleep(1)
        pyautogui.click(709, 176)
        time.sleep(1)
        pyautogui.typewrite(yy)

        # to do

    def _TestScorll(self, ScorValue):
        print ScorValue
        time.sleep(5)
        pyautogui.scroll(100)
        time.sleep(0.5)
        pyautogui.scroll(100)
        time.sleep(0.5)
        pyautogui.scroll(100)
        time.sleep(0.5)
        pyautogui.scroll(100)
        time.sleep(0.5)
        pyautogui.scroll(100)
        time.sleep(0.5)
        pyautogui.scroll(100)
        time.sleep(5)
        pyautogui.scroll(-100)
        time.sleep(0.5)
        pyautogui.scroll(-100)
        time.sleep(0.5)
        pyautogui.scroll(-100)
        time.sleep(0.5)
        pyautogui.scroll(-100)
        time.sleep(0.5)
        pyautogui.scroll(-100)
        time.sleep(0.5)
        pyautogui.scroll(-100)

    def _TimeDiff(self, HH, MM, SS):
        CurrentTime = sm.now()
        TargetTimeS = self.Y+'-'+self.M+'-'+self.D+' '+str(HH)+':'+str(MM)+':'+str(SS)+'.0'
        TargetTime = sm.strptime(TargetTimeS, "%Y-%m-%d %H:%M:%S.%f")

        print "Gua ji shi jian is {} minutes".format(((TargetTime-CurrentTime).total_seconds())/60)
        return (abs((TargetTime-CurrentTime).seconds-10))

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