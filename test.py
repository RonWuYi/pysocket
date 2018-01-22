import pyautogui
import time

pyautogui.PAUSE = 1.5

GongXunTime = 120
JinYinTime = 160

class AW1():
    def __init__(self):
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
        self.InIt()
        self.GongXunRenWuComplete = True

    def JingYingRenWu(self, Rtimes, Wtimes):
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
        self.InIt()
        self.JingYingRenWuComplete = True

    def TaFangFengMo(self, FengMoTime):
        self.GuaJiFlag = False
        self.CurStatus = 'TaFangFengMo'
        self.EventTime += 1

        # self._BaoWuShenDunJieMian()
        for jj in range(FengMoTime):
            self._GoFengMoNPC()
            time.sleep(1)
            pyautogui.click(931, 387)

            # jie qu ren wu
            time.sleep(1)
            pyautogui.click(505, 593)

            # jin ru feng mo gu
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
        self.InIt()
        self.TaFangFengMoComplete = True

    def ChuangTianGuan(self, TianGuanTime):
        self.GuaJiFlag = False
        self.CurStatus = 'ChuangTianGuan'
        self.EventTime += 1

        time.sleep(1)
        pyautogui.click(911, 503)

        time.sleep(1)
        pyautogui.click(507, 600)
        time.sleep(TianGuanTime)
        time.sleep(1)
        pyautogui.click(511, 514)
        self.InIt()
        self.ChuangTianGuanComplete = True

    def CaiLiaoFuBen(self):
        self.GuaJiFlag = False
        self.CurStatus = 'CaiLiaoFuBen'

        self.EventTime += 1
        time.sleep(1)

        for i in range(2):
            for iii in range(0, 7):
                moveValue = 30

                # xiao chu dui hua kuang
                time.sleep(1)
                pyautogui.press('esc')
                time.sleep(1)
                pyautogui.click(939, 425)
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
            self.HuiShouLess()
        self.InIt()
        self.CaiLiaoFuBenComplete = True
        
    # Todo
    def WeiWangRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'WeiWangRenWu'
        self.EventTime += 1

        # x, y = pyautogui.size()
        # pyautogui.moveTo(x/2, y/2,duration=0.5)
        # time.sleep(0.5)
        # pyautogui.click()
        #
        # time.sleep(1)
        # # da kai jie mian
        # pyautogui.press('j')
        #
        # # ri chang ren wu
        # time.sleep(1)
        # pyautogui.moveTo(285, 225, duration=1)
        # time.sleep(1)
        # pyautogui.click()
        #
        # # jie qu ren wu
        # time.sleep(1)
        # pyautogui.moveTo(750, 633, duration=1)
        # time.sleep(1)
        # pyautogui.click()
        #
        # ############ task 1 #########################################
        # # click ren wu ming cheng
        # time.sleep(1)
        # pyautogui.moveTo(304, 279,duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        # time.sleep(1)
        #
        # # jie shou xuan shang
        # pyautogui.moveTo(647, 546,duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        # time.sleep(1)
        #
        # # chuan
        # pyautogui.moveTo(683, 508,duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        # time.sleep(1)
        #
        # # na dong xi
        # x, y = pyautogui.size()
        # pyautogui.moveTo(x/2, y/2,duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        #
        # # deng dai wan cheng
        # time.sleep(30)
        #
        # # chuan
        # pyautogui.moveTo(1466, 503,duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        # time.sleep(1)
        #
        # # wan cheng ren wu
        # pyautogui.moveTo(929, 605,duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        # time.sleep(1)

        ############ task 2 #########################################
        self._ClickCenter()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.click(285, 225)

        # jie qu ren wu
        time.sleep(1)
        pyautogui.click(750, 633)
        time.sleep(1)
        pyautogui.click(308, 327)
        time.sleep(1)

        # jie shou xuan shang
        pyautogui.click(647, 546)
        time.sleep(1)

        # chuan
        pyautogui.click(707, 507)
        time.sleep(1)

        # deng dai wan cheng
        time.sleep(12)

        # chuan
        pyautogui.click(1466, 503)
        time.sleep(1)

        # wan cheng ren wu
        pyautogui.click(929, 605)
        time.sleep(1)

        ############ task 3 #########################################
        self._ClickCenter()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.click(285, 225)

        # jie shou xuan shang
        pyautogui.click(647, 546)
        time.sleep(1)
        pyautogui.click(697, 506)
        time.sleep(1)

        # jie shou xuan shang
        pyautogui.click(929, 605)
        time.sleep(1)

        # chuan
        pyautogui.click(967, 570)
        time.sleep(1)

        # deng dai wan cheng
        time.sleep(22)

        # chuan
        pyautogui.click(1466, 503)
        time.sleep(1)

        # wan cheng ren wu
        pyautogui.click(929, 605)
        time.sleep(1)

        ############ task 4 #########################################
        self._ClickCenter()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.click(285, 225)

        # jie qu ren wu
        time.sleep(1)
        pyautogui.click(750, 633)
        time.sleep(1)
        pyautogui.click(315, 424)
        time.sleep(1)

        # jie shou xuan shang
        pyautogui.click(647, 546)
        time.sleep(1)

        # chuan
        pyautogui.click(684, 506)
        time.sleep(1)

        # deng dai wan cheng
        time.sleep(30)

        # chuan
        pyautogui.click(1466, 503)
        time.sleep(1)

        # wan cheng ren wu
        pyautogui.click(929, 605,)
        time.sleep(1)
        self.InIt()
        self.WeiWangRenWuComplete = True

    def ChuMoRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ChuMoRenWu'
        self.EventTime += 1

        # chuan dao Zhang TianShi
        time.sleep(1)
        pyautogui.click(931, 425)
        for i in range(6):
            time.sleep(1)
            pyautogui.click(551, 571)

        time.sleep(1)
        pyautogui.press('esc')
        self.InIt()
        self.ChuMoRenWuComplete = True

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

        # hui shou kuang shi
        pyautogui.click(598, 556)
        time.sleep(2)

        # hui shou zhuang bei
        pyautogui.click(799, 556)
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

    def HuiShouLess(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HuiShou'
        self.EventTime += 1

        # da kai bei bao jie mian
        time.sleep(1)
        pyautogui.press('b')
        time.sleep(1)
        pyautogui.click(627, 627)
        time.sleep(1)
        pyautogui.click(521, 427)
        time.sleep(2)

        pyautogui.click(602, 575)
        time.sleep(2)

        # hui shou zhuang bei
        pyautogui.click(804, 575)
        time.sleep(2)

        pyautogui.press('esc')
        time.sleep(0.5)

    def GuaJi(self):
        self.GuaJiFlag = True
        self.CurStatus = 'GuaJi'
        self.EventTime += 1

        self.InIt()
        self._GuJiNPC()

        time.sleep(1)
        pyautogui.click(595, 418)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('z')

    # ToDo imporve it
    def WaKuang(self):
        self.GuaJiFlag = True
        self.CurStatus = 'WaKuang'
        self.EventTime += 1

        time.sleep(100)
        pyautogui.click(1220, 611)
        time.sleep(1)

    def RiMoBaiChengZhu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'MoBaiChengZhu'
        self.EventTime += 1

        time.sleep(1)
        self._HuoDongJieMian()

        for i in range(9):
            time.sleep(1)
            for i in range(3):
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

        self.InIt()
        self.MoBaiChengZhuComplete = True

    def RiYeZhanBiQi(self):
        self.GuaJiFlag = False
        self.CurStatus = 'YeZhanBiQi'
        self.EventTime += 1

        self._HuoDongJieMian()
        time.sleep(1)
        pyautogui.click(509, 606)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1200)

        self.InIt()
        self.YeZhanBiQiComplete = True

    def RiShenWei(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ShenWei'
        self.EventTime += 1

        self._HuoDongJieMian()
        time.sleep(1)
        pyautogui.click(508, 606)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('z')
        # time.sleep(1200)
        time.sleep(2)
        for i in range(9):
            pyautogui.click(889, 578)
            time.sleep(1)
            pyautogui.click(889, 578)
            time.sleep(45)
            pyautogui.click(511, 600)
        time.sleep(3600)

        self.InIt()
        self.ShenWeiComplete = True

    def RiWorldBoss(self):
        self.GuaJiFlag = False
        self.CurStatus = 'WorldBoss'
        self.EventTime += 1

        time.sleep(1)
        self._HuoDongJieMian()
        time.sleep(1)
        pyautogui.click(509, 595)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(2000)
        pyautogui.click(909, 685)
        time.sleep(1)
        pyautogui.press('e')

        self.InIt()
        self.WorldBossComplete = True

    def RiJinZhuSongLi(self):
        self.GuaJiFlag = False
        self.CurStatus = 'JinZhuSongLi'
        self.EventTime += 1

        self._HuoDongJieMian()
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1)
        time.sleep(900)

        self.InIt()
        self.JingYingRenWuComplete = True

        # ToDo imporve it

    def GeRenBoss(self, GeRenBossTime):
        self.GuaJiFlag = False
        self.CurStatus = 'GeRenBoss'
        self.EventTime += 1

        for i in range(GeRenBossTime):
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
        pyautogui.press('esc')

    def _WoYaoBianQaing(self):
        time.sleep(1)
        # da kai jie mian
        pyautogui.press('c')

        time.sleep(1)
        pyautogui.click(573, 580)

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
        time.sleep(1)
        pyautogui.click(614, 339)

        time.sleep(1)
        pyautogui.click(518, 636)

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('esc')

    def _HuoDongJieMian(self):
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        x, y = pyautogui.size()
        pyautogui.click(x, y)
        time.sleep(1)
        pyautogui.press('j')
        time.sleep(1)
        pyautogui.click(750, 615)

    def RiBiGuan(self):
        self._HuoDongJieMian()

        # di tu
        time.sleep(1)
        pyautogui.press('m')

        # zuo biao x
        time.sleep(1)
        pyautogui.click(613, 210)
        time.sleep(1)
        pyautogui.typewrite('31')

        # zuo biao y
        # time.sleep(1)
        # pyautogui.moveTo(713, 209, duration=0.5)
        time.sleep(1)
        pyautogui.click(713, 209)
        time.sleep(1)
        pyautogui.typewrite('26')

        # qian wang di dian
        # time.sleep(1)
        # pyautogui.moveTo(770, 209, duration=0.5)
        time.sleep(1)
        pyautogui.click(770, 209)
        time.sleep(1)
        pyautogui.click(770, 209)
        time.sleep(1200)

        time.sleep(1)
        pyautogui.press('esc')

        self.InIt()
        # flag
        self.BiGuanComplete = True

    def RiGuaiWuGongCheng(self):
        self.GuaJiFlag = False
        self.CurStatus = 'GuaiWuGongCheng'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()

        # gua ji ban ge xiao shi
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1750)

        self.InIt()
        self.GuaiWuGongChengComplete = False

    def RiSuoYaoTa(self):
        self.GuaJiFlag = False
        self.CurStatus = 'RiSuoYaoTa'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()

        # gua ji ban ge xiao shi
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1750)

        self.InIt()
        self.SuoYaoTaComplete = True

        # ToDo

    def RiDuoBeiYaSong(self):
        self.GuaJiFlag = False
        self.CurStatus = 'RiDuoBeiYaSong'
        self.EventTime += 1
        time.sleep(1)
        for i in range(3):
            self._HuoDongJieMian()
            time.sleep(1)
            for i in range(8):
                time.sleep(1)
                pyautogui.click(649, 542)
            time.sleep(1)
            pyautogui.click(938, 549)
            if i == 0:
                pyautogui.press('esc')
                time.sleep(300)
                # time.sleep(300)
            else:
                pyautogui.press('esc')
                time.sleep(300)
            # pyautogui.press('esc')
            pyautogui.click(582, 499)

        self.InIt()
        self.DuoBeiYaSongComplete = True

    def RiSanBeiLianGong(self):
        self.GuaJiFlag = False
        self.CurStatus = 'SanBeiLianGong'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()

        # ToDo
        # NPC part and delay part
        self.InIt()
        self.SanBeiLianGongComplete = True

    def RiJiaLanShenDian(self):
        self.GuaJiFlag = False
        self.CurStatus = 'JiaLanShenDian'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()
        time.sleep(3600)
        # ToDo
        # NPC part and delay part

        self.InIt()
        self.JiaLanShenDianComplete = True

    def RiHaiTianShengYan(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HaiTianShengYan'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()

        # ToDo
        # NPC part and delay part
        self.InIt()
        self.HaiTianShengYanComplete = True

    def RiShiMuMiZhen(self):
        self.GuaJiFlag = False
        self.CurStatus = 'RiShiMuMiZhen'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()
        time.sleep(300)
        # ToDo
        # NPC part and delay part
        self.InIt()
        self.ShiMuMiZhenComplete = True

    def _BossJieMian(self):
        # da kai boss jie mian
        time.sleep(1)
        pyautogui.click(715, 188)
        time.sleep(1)

    def _GuJiNPC(self):
        time.sleep(0.5)
        pyautogui.click(951, 714)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('c')
        # time.sleep(1)
        time.sleep(1)
        pyautogui.click(577, 598)
        time.sleep(1)
        pyautogui.click(412, 216)
        time.sleep(1)
        pyautogui.click(410, 215)
        time.sleep(1)
        pyautogui.click(892, 605)
        time.sleep(1)

    def _BaoWuShenDunJieMian(self):
        # da kai bao wu jie mian
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.click(197, 250)
        time.sleep(1)
        pyautogui.click(792, 591)
        time.sleep(1)

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

    def _ManyNPC(self, Coox, Cooy):
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(0.5)
        pyautogui.moveTo(self.x / 2, self.y / 2, duration=0.5)
        time.sleep(0.5)
        pyautogui.click(self.x / 2, self.y / 2)
        time.sleep(0.5)
        # di tu
        time.sleep(1)
        pyautogui.press('m')
        time.sleep(0.1)
        pyautogui.doubleClick(844, 564)
        time.sleep(0.1)
        pyautogui.doubleClick(844, 564)
        time.sleep(0.1)
        pyautogui.doubleClick(844, 564)
        time.sleep(0.1)
        pyautogui.doubleClick(844, 564)
        pyautogui.scroll(-100)
        time.sleep(1)
        pyautogui.scroll(-100)
        time.sleep(1)
        pyautogui.scroll(-100, Coox, Cooy)
        time.sleep(1)
        pyautogui.scroll(-100, Coox, Cooy)
        time.sleep(1)
        pyautogui.scroll(-100, Coox, Cooy)
        time.sleep(1)
        pyautogui.scroll(-100, Coox, Cooy)

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