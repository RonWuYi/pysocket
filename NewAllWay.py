import pyautogui
import time

pyautogui.PAUSE = 1.5
GongXunTime = 120
JinYinTime = 160

class AW:
    def __init__(self):
        self.GongXunTime = 120
        self.JinYinTime = 240
        self.x, self.y = pyautogui.size()
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

        self.GongXunRenWuNPC()
        # click NPC
        time.sleep(1)
        pyautogui.click(555, 324)

        # zi dong shua xin
        time.sleep(1)
        pyautogui.click(622, 527)
        time.sleep(8)

        #jie qu ren wu
        pyautogui.click(509, 567)
        time.sleep(1)

        # wan chen ren wu
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

        self.GongXunRenWuComplete = True

    def JingYingRenWu(self, Rtimes, Wtimes):
        self.GuaJiFlag = False
        self.CurStatus = 'TianFu'
        self.EventTime += 1

        self.JinYingRenWuNPC(100, 73)

        # click NPC
        time.sleep(1)
        pyautogui.click(556, 363)

        # jie qu ren wu
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

        self.JingYingRenWuComplete = True

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
        # x, y = pyautogui.size()
        pyautogui.moveTo(self.x / 2, self.y / 2, duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=0.5)
        time.sleep(1)
        pyautogui.click(285, 225)

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(750, 633, duration=0.5)
        time.sleep(1)
        pyautogui.click(750, 633)

        pyautogui.moveTo(308, 327, duration=0.5)
        time.sleep(1)
        pyautogui.click(308, 327)
        time.sleep(1)

        # jie shou xuan shang
        pyautogui.moveTo(647, 546, duration=0.5)
        time.sleep(1)
        pyautogui.click(647, 546)
        time.sleep(1)

        # chuan
        pyautogui.moveTo(707, 507,duration=0.5)
        time.sleep(1)
        pyautogui.click(707, 507)
        time.sleep(1)

        # deng dai wan cheng
        time.sleep(12)

        # chuan
        pyautogui.moveTo(1466, 503,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # wan cheng ren wu
        pyautogui.moveTo(929, 605,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        ############ task 3 #########################################
        # x, y = pyautogui.size()
        pyautogui.moveTo(self.x / 2, self.y / 2, duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=0.5)
        time.sleep(1)
        pyautogui.click()

        # jie shou xuan shang
        pyautogui.moveTo(647, 546,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        pyautogui.moveTo(697, 506,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # jie shou xuan shang
        pyautogui.moveTo(929, 605,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # chuan
        pyautogui.moveTo(967, 570,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # deng dai wan cheng
        time.sleep(22)

        # chuan
        pyautogui.moveTo(1466, 503,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # wan cheng ren wu
        pyautogui.moveTo(929, 605,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        ############ task 4 #########################################
        # x, y = pyautogui.size()
        pyautogui.moveTo(self.x / 2, self.y / 2, duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=0.5)
        time.sleep(1)
        pyautogui.click()

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(750, 633, duration=0.5)
        time.sleep(1)
        pyautogui.click()

        pyautogui.moveTo(315, 424,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # jie shou xuan shang
        pyautogui.moveTo(647, 546,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # chuan
        pyautogui.moveTo(684, 506,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # deng dai wan cheng
        time.sleep(30)

        # chuan
        pyautogui.moveTo(1466, 503,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # wan cheng ren wu
        pyautogui.moveTo(929, 605,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        self.WeiWangRenWuComplete = True

    def TaFangFengMo(self):
        self.GuaJiFlag = False
        self.CurStatus = 'TaFangFengMo'
        self.EventTime += 1

        self._BaoWuShenDunJieMian()

        for jj in range(3):
            time.sleep(1)
            # da kai jie mian
            pyautogui.press('j')

            # ri chang ren wu
            time.sleep(1)
            pyautogui.moveTo(281, 227, duration=0.5)
            time.sleep(1)
            pyautogui.click()

            # jie qu ren wu
            time.sleep(1)
            pyautogui.moveTo(278, 635, duration=0.5)
            time.sleep(1)
            pyautogui.click()

            # jin ru feng mo gu
            pyautogui.moveTo(505, 611, duration=0.5)
            pyautogui.click()

            # kai shi shua guai
            pyautogui.moveTo(700, 414)
            pyautogui.click()

            for ii in range(2):
                # dian
                pyautogui.moveTo(320, 415)
                pyautogui.click()

                # dao lu dian ji dian, ren wu qian jin
                pyautogui.moveTo(754, 349)
                # pyautogui.rightClick(clicks=3, interval=0.5)
                pyautogui.click(button='right', clicks=1)

                # du
                pyautogui.moveTo(415, 416)
                pyautogui.click()


                # dao lu dian ji dian, ren wu qian jin
                pyautogui.moveTo(754, 349)
                pyautogui.click(button='right', clicks=1)

                # bin
                pyautogui.moveTo(509, 413)
                pyautogui.click()

                # dao lu dian ji dian, ren wu qian jin
                pyautogui.moveTo(754, 349)
                pyautogui.click(button='right', clicks=1)

                # bao
                pyautogui.moveTo(606, 415)
                pyautogui.click()

                # dao lu dian ji dian, ren wu qian jin
                pyautogui.moveTo(754, 349)
                pyautogui.click(button='right', clicks=1)

            # deng dai jie shu
            time.sleep(420)

            # lin qu jiang li
            pyautogui.moveTo(604, 398, duration=0.5)
            pyautogui.click()

        self.TaFangFengMoComplete = True

    def CaiLiaoFuBen(self):
        self.GuaJiFlag = False
        self.CurStatus = 'CaiLiaoFuBen'

        self.EventTime += 1
        time.sleep(1)
        self.InIt()
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(359, 225, duration=0.5)
        time.sleep(1)
        pyautogui.click()

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(281, 470, duration=0.5)
        time.sleep(1)
        pyautogui.click()

        for i in range(2):
            for iii in range(0, 7):
                moveValue = 30

                # xiao chu dui hua kuang
                time.sleep(1)
                pyautogui.press('esc')
                time.sleep(1)

                # click NPC
                pyautogui.moveTo(605, 370,duration=0.5)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)

                # fu ben ming zi
                # 514, 413
                pyautogui.moveTo(514, (413 + (iii * moveValue)),duration=0.5)
                time.sleep(1)
                pyautogui.click()

                # jin ru fu ben
                time.sleep(1)
                pyautogui.moveTo(498, 600,duration=0.5)
                time.sleep(1)
                pyautogui.click()

                # zi dong zhan dou
                time.sleep(1)
                pyautogui.press('z')
                if iii < 3:
                    time.sleep(88)
                elif iii == 3:
                    time.sleep(110)
                elif iii == 4:
                    time.sleep(300)
                elif iii == 5:
                    time.sleep(75)
                elif iii == 6:
                    time.sleep(130)
                else:
                    time.sleep(130)

                # li kai fu ben / mian fei lin qu jiang li
                time.sleep(1)
                pyautogui.moveTo(859, 604,duration=0.5)
                time.sleep(1)
                pyautogui.click()

        self.CaiLiaoFuBenComplete = True

    def ChuMoRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ChuMoRenWu'
        self.EventTime += 1

        # chuan dao Zhang TianShi
        time.sleep(1)
        pyautogui.moveTo(932, 462, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()

        # jiao shu
        time.sleep(1)
        pyautogui.moveTo(545, 588, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        self.ChuMoRenWuComplete = True

    # Todo
    def ChuangTianGuan(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ChuangTianGuan'
        self.EventTime += 1

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('c')

        # wo yao bian qiang
        time.sleep(1)
        pyautogui.moveTo(576, 616, duration=0.5)
        time.sleep(1)
        pyautogui.click()

        # feng mo gu NPC
        time.sleep(1)
        pyautogui.moveTo(945, 238, duration=0.5)
        time.sleep(1)
        pyautogui.click()

        # xiao chu wu yong dui hua kuang
        time.sleep(1)
        pyautogui.press('esc')
        pyautogui.click()
        time.sleep(1)

        # click NPC
        pyautogui.moveTo(316, 133, duration=0.5)
        time.sleep(1)
        pyautogui.click()

        # jin ru chuang tian guan
        pyautogui.moveTo(507, 618, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(900)
        time.sleep(1)
        pyautogui.moveTo(511, 533, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1800)

        self.ChuangTianGuanComplete = True

    def HuiShou(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HuiShou'
        self.EventTime += 1

        # da kai bei bao jie mian
        time.sleep(1)
        pyautogui.press('b')
        time.sleep(1)
        pyautogui.moveTo(627, 627, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(521, 427, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        # hui shou kuang shi
        pyautogui.moveTo(602, 575, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        # hui shou zhuang bei
        pyautogui.moveTo(804, 575, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        pyautogui.press('esc')
        time.sleep(0.5)
        self.InIt()

        for i in range(2):
            time.sleep(0.5)
            pyautogui.press('q')
            time.sleep(0.5)
            pyautogui.press('q')
            time.sleep(0.5)
            pyautogui.press('w')
            time.sleep(0.5)
            pyautogui.press('w')

        self._BossJieMian()

        # lie mo ji fen
        time.sleep(1)
        pyautogui.moveTo(594, 214, duration=0.5)
        time.sleep(1)
        pyautogui.click(594, 214)

        # yi jian hui shou
        time.sleep(1)
        pyautogui.moveTo(718, 634, duration=0.5)
        time.sleep(1)
        pyautogui.click(718, 634)
        time.sleep(1)
        pyautogui.press('esc')
        # self.InIt()

    def HuiShouLess(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HuiShou'
        self.EventTime += 1

        # da kai bei bao jie mian
        time.sleep(1)
        pyautogui.press('b')
        time.sleep(1)
        pyautogui.moveTo(627, 627, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(521, 427, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        # hui shou kuang shi
        pyautogui.moveTo(602, 575, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        # hui shou zhuang bei
        pyautogui.moveTo(804, 575, duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        pyautogui.press('esc')
        time.sleep(0.5)
        self.InIt()
        # time.sleep(0.5)
        #
        # self.InIt()

        # for i in range(2):
        #     time.sleep(0.5)
        #     pyautogui.press('q')
        #     time.sleep(0.5)
        #     pyautogui.press('q')
        #     time.sleep(0.5)
        #     pyautogui.press('w')
        #     time.sleep(0.5)
        #     pyautogui.press('w')

        pyautogui.press('esc')

    # ToDo imporve it
    def GuaJi(self):
        self.GuaJiFlag = True
        self.CurStatus = 'GuaJi'
        self.EventTime += 1

        self._BaoWuXueYuJieMian()
        # da kai bao wu jie mian
        # pyautogui.moveTo(572, 636, duration=0.5)
        # time.sleep(1)
        # pyautogui.click(572, 636)
        # time.sleep(1)
        # pyautogui.moveTo(195, 234,duration=0.5)
        # time.sleep(1)
        # pyautogui.click(195, 234)
        # time.sleep(1)
        # pyautogui.moveTo(792, 629,duration=0.5)
        # time.sleep(1)
        # pyautogui.click(792, 629)
        # time.sleep(1)


        pyautogui.moveTo(596, 397,duration=0.5)
        time.sleep(1)
        pyautogui.click(596, 397)
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('z')

    # ToDo imporve it
    def WaKuang(self):
        self.GuaJiFlag = True
        self.CurStatus = 'WaKuang'
        self.EventTime += 1
        time.sleep(1)
        pyautogui.moveTo(1220, 611, duration=0.5)
        time.sleep(1)
        time.sleep(100)
        pyautogui.click()
        time.sleep(1)

    def RiMoBaiChengZhu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'MoBaiChengZhu'
        self.EventTime += 1

        time.sleep(1)
        self._HuoDongJieMian()

        for i in range(9):
            time.sleep(1)
            pyautogui.moveTo(587, 613, duration=0.5)
            time.sleep(1)
            for i in range(3):
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
            pyautogui.moveTo(799, 535, duration=0.5)
            pyautogui.click()

        self.MoBaiChengZhuComplete =True

    def RiYeZhanBiQi(self):
        self.GuaJiFlag = False
        self.CurStatus = 'YeZhanBiQi'
        self.EventTime += 1

        self._HuoDongJieMian()
        pyautogui.press('z')
        time.sleep(1200)

        self.YeZhanBiQiComplete = True

    def RiShenWei(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ShenWei'
        self.EventTime += 1

        self._HuoDongJieMian()
        pyautogui.press('z')
        time.sleep(3600)
        time.sleep(3600)

        self.ShenWeiComplete = True

    def RiWorldBoss(self):
        self.GuaJiFlag = False
        self.CurStatus = 'WorldBoss'
        self.EventTime += 1

        time.sleep(1)
        self._HuoDongJieMian()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1)
        time.sleep(2000)

        self.WorldBossComplete = True

    def RiJinZhuSongLi(self):
        self.GuaJiFlag = False
        self.CurStatus = 'JinZhuSongLi'
        self.EventTime += 1

        self._HuoDongJieMian()

        pyautogui.press('z')
        time.sleep(1)
        time.sleep(900)

        self.JingYingRenWuComplete = True

    def RiBiGuan(self):
        self._HuoDongJieMian()

        # di tu
        time.sleep(1)
        pyautogui.press('m')

        # zuo biao x
        time.sleep(1)
        pyautogui.moveTo(613, 210, duration=0.5)
        time.sleep(1)
        pyautogui.click(613, 210)
        time.sleep(1)
        pyautogui.typewrite('31')

        # zuo biao y
        time.sleep(1)
        pyautogui.moveTo(713, 209, duration=0.5)
        time.sleep(1)
        pyautogui.click(713, 209)
        time.sleep(1)
        pyautogui.typewrite('26')

        # qian wang di dian
        time.sleep(1)
        pyautogui.moveTo(770, 209, duration=0.5)
        time.sleep(1)
        pyautogui.click(770, 209)
        time.sleep(1)
        pyautogui.click(770, 209)
        time.sleep(1200)

        time.sleep(1)
        pyautogui.press('esc')
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

        self.SuoYaoTaComplete = True

    # ToDo
    def RiDuoBeiYaSong(self):
        self.GuaJiFlag = False
        self.CurStatus = 'RiDuoBeiYaSong'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()

        # ToDo
        # NPC part and delay part

        self.DuoBeiYaSongComplete = True

    def RiSanBeiLianGong(self):
        self.GuaJiFlag = False
        self.CurStatus = 'SanBeiLianGong'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()

        # ToDo
        # NPC part and delay part

        self.SanBeiLianGongComplete = True

    def RiJiaLanShenDian(self):
        self.GuaJiFlag = False
        self.CurStatus = 'JiaLanShenDian'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()

        # ToDo
        # NPC part and delay part

        self.JiaLanShenDianComplete = True

    def RiHaiTianShengYan(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HaiTianShengYan'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()

        # ToDo
        # NPC part and delay part

        self.HaiTianShengYanComplete = True

    def RiShiMuMiZhen(self):
        self.GuaJiFlag = False
        self.CurStatus = 'RiShiMuMiZhen'
        self.EventTime += 1
        time.sleep(1)

        self._HuoDongJieMian()

        # ToDo
        # NPC part and delay part

        self.ShiMuMiZhenComplete = True

    # ToDo imporve it
    def GeRenBoss(self):
        self.GuaJiFlag = False
        self.CurStatus = 'GeRenBoss'
        self.EventTime += 1

        self.InIt()
        for i in range(4):
            # self._WoYaoBianQaing()
            #
            # # wo yao zhuang bei
            # time.sleep(1)
            # pyautogui.moveTo(408, 279, duration=0.5)
            # time.sleep(1)
            # pyautogui.click(408, 279,)
            #
            # # tiao zhan boss
            # time.sleep(1)
            # pyautogui.moveTo(891, 301, duration=0.5)
            # time.sleep(1)
            # pyautogui.click(891, 301)

            self._BossJieMian()

            # ge ren boss
            time.sleep(1)
            pyautogui.moveTo(348, 217, duration=0.5)
            time.sleep(1)
            pyautogui.click(348, 217)

            # boss ming zi
            time.sleep(1)
            pyautogui.moveTo(261, (255+(i*41)), duration=0.5)
            time.sleep(1)
            pyautogui.click(261, (255+(i*41)))

            # qian wang tiao zhan
            pyautogui.moveTo(783, 634, duration=0.5)
            time.sleep(1)
            pyautogui.click(783, 634)

            # wo yao bian qiang
            # time.sleep(1)
            # pyautogui.press('esc')
            # x, y = pyautogui.size()
            # pyautogui.moveTo(x / 2, y / 2, duration=0.5)
            time.sleep(0.5)
            # pyautogui.click(x / 2, y / 2)
            pyautogui.press('z')
            time.sleep(1)

            time.sleep(30 + (i*18))

            # wan cheng ren wu
            time.sleep(1)
            pyautogui.moveTo(860, 608, duration=0.5)
            time.sleep(1)
            pyautogui.click(860, 608)

            self.HuiShou()

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

        # # wo yao bian qiang Web
        # time.sleep(1)
        # pyautogui.moveTo(577, 616, duration=0.5)
        # time.sleep(1)
        # pyautogui.click(577, 616)

        # wo yao bian qiang UI
        time.sleep(1)
        pyautogui.moveTo(573, 580, duration=0.5)
        time.sleep(1)
        pyautogui.click(573, 580)

    def _GoFengMoNPC(self):
        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=0.5)
        time.sleep(1)
        pyautogui.click()

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(518, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('esc')

    def _HuoDongJieMian(self):
        time.sleep(1)
        # da kai jie mian
        self.InIt()
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(751, 633, duration=0.5)
        time.sleep(1)
        pyautogui.click(751, 633)

        # jin ru huo dong
        time.sleep(1)
        pyautogui.moveTo(511, 627, duration=0.5)
        time.sleep(1)
        pyautogui.click(511, 627)

        # xiao chu jie mian
        time.sleep(1)
        pyautogui.press('esc')

    def _BossJieMian(self):
        # da kai boss jie mian
        time.sleep(1)
        pyautogui.moveTo(715, 188, duration=0.5)
        time.sleep(1)
        pyautogui.click(715, 188)
        time.sleep(1)

    def _BaoWuXueYuJieMian(self):
        # da kai bao wu jie mian
        pyautogui.moveTo(571, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(571, 636)
        time.sleep(1)
        # pyautogui.moveTo(197, 192,duration=0.5)
        # time.sleep(1)
        # pyautogui.click(197, 192)
        # time.sleep(1)
        # pyautogui.moveTo(792, 591,duration=0.5)
        # time.sleep(1)
        # pyautogui.click(792, 591)
        # time.sleep(1)

    def _BaoWuShenDunJieMian(self):
        # da kai bao wu jie mian
        pyautogui.moveTo(569, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.moveTo(197, 250,duration=0.5)
        time.sleep(1)
        pyautogui.click(197, 250)
        time.sleep(1)
        pyautogui.moveTo(792, 591,duration=0.5)
        time.sleep(1)
        pyautogui.click(792, 591)
        time.sleep(1)

    def _BaoWuGuanZhiJieMian(self):
        # da kai bao wu jie mian
        pyautogui.moveTo(569, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.moveTo(197, 304,duration=0.5)
        time.sleep(1)
        pyautogui.click(197, 304)
        time.sleep(1)
        pyautogui.moveTo(792, 591,duration=0.5)
        time.sleep(1)
        pyautogui.click(792, 591)
        time.sleep(1)

    def _BaoWuLongHunJieMian(self):
        # da kai bao wu jie mian
        pyautogui.moveTo(569, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.moveTo(197, 359,duration=0.5)
        time.sleep(1)
        pyautogui.click(197, 359)
        time.sleep(1)
        pyautogui.moveTo(792, 591,duration=0.5)
        time.sleep(1)
        pyautogui.click(792, 591)
        time.sleep(1)

    def _BaoWuLongPoJieMian(self):
        # da kai bao wu jie mian
        pyautogui.moveTo(569, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.moveTo(197, 410,duration=0.5)
        time.sleep(1)
        pyautogui.click(197, 410)
        time.sleep(1)
        pyautogui.moveTo(792, 591,duration=0.5)
        time.sleep(1)
        pyautogui.click(792, 591)
        time.sleep(1)

    # def BossJieMian(self):
    #     # da kai boss jie mian
    #     time.sleep(1)
    #     pyautogui.moveTo(715, 188, duration=0.5)
    #     time.sleep(1)
    #     pyautogui.click(715, 188)
    #     time.sleep(1)

    def BaoWuXueYuJieMian(self):
        # da kai bao wu jie mian
        pyautogui.moveTo(569, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        # pyautogui.moveTo(197, 192,duration=0.5)
        # time.sleep(1)
        # pyautogui.click(197, 192)
        # time.sleep(1)
        # pyautogui.moveTo(792, 591,duration=0.5)
        # time.sleep(1)
        # pyautogui.click(792, 591)
        # time.sleep(1)

    def BaoWuShenDunJieMian(self):
        # da kai bao wu jie mian
        pyautogui.moveTo(569, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.moveTo(197, 250,duration=0.5)
        time.sleep(1)
        pyautogui.click(197, 250)
        time.sleep(1)
        # pyautogui.moveTo(792, 591,duration=0.5)
        # time.sleep(1)
        # pyautogui.click(792, 591)
        # time.sleep(1)

    def BaoWuGuanZhiJieMian(self):
        # da kai bao wu jie mian
        pyautogui.moveTo(569, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.moveTo(197, 304,duration=0.5)
        time.sleep(1)
        pyautogui.click(197, 304)
        time.sleep(1)
        # pyautogui.moveTo(792, 591,duration=0.5)
        # time.sleep(1)
        # pyautogui.click(792, 591)
        # time.sleep(1)

    def BaoWuLongHunJieMian(self):
        # da kai bao wu jie mian
        pyautogui.moveTo(569, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.moveTo(197, 359,duration=0.5)
        time.sleep(1)
        pyautogui.click(197, 359)
        time.sleep(1)
        # pyautogui.moveTo(792, 591,duration=0.5)
        # time.sleep(1)
        # pyautogui.click(792, 591)
        # time.sleep(1)

    def BaoWuLongPoJieMian(self):
        # da kai bao wu jie mian
        pyautogui.moveTo(569, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(569, 636)
        time.sleep(1)
        pyautogui.moveTo(197, 410,duration=0.5)
        time.sleep(1)
        pyautogui.click(197, 410)
        time.sleep(1)
        # pyautogui.moveTo(792, 591,duration=0.5)
        # time.sleep(1)
        # pyautogui.click(792, 591)
        # time.sleep(1)

    def GongXunRenWuNPC(self):
        time.sleep(1)
        pyautogui.press('j')
        time.sleep(1)
        pyautogui.click(284, 209)
        time.sleep(1)
        pyautogui.click(516, 620)
        time.sleep(1)
        pyautogui.press('esc')

    def JinYingRenWuNPC(self, x, y):
        # self.InIt()
        self._GoTo(str(x), str(y))

    def _ClickCenter(self):
        time.sleep(0.5)
        pyautogui.moveTo(self.x/2, self.y/2,duration=0.5)
        time.sleep(0.5)
        pyautogui.click(self.x/2, self.y/2)
        time.sleep(0.5)

    def _GoTo(self, xx, yy):
        # time.sleep(0.5)
        # pyautogui.moveTo((self.x)/2, (self.y)/2,duration=0.5)
        # time.sleep(0.5)
        # pyautogui.click(self.x/2, self.y/2)
        # time.sleep(0.5)
        #
        # self._ClickCenter()
        # di tu
        time.sleep(1)
        pyautogui.press('m')

        # zuo biao x
        # time.sleep(1)
        # pyautogui.moveTo(612, 175, duration=0.5)
        time.sleep(1)
        pyautogui.click(612, 193)
        time.sleep(1)
        pyautogui.typewrite(xx)

        # zuo biao y
        # time.sleep(1)
        # pyautogui.moveTo(709, 176, duration=0.5)
        time.sleep(1)
        pyautogui.click(710, 193)
        time.sleep(1)
        pyautogui.typewrite(yy)
        time.sleep(1)
        pyautogui.click(770, 193)
        time.sleep(10)
        pyautogui.click(770, 193)
        time.sleep(10)
        pyautogui.press('esc')

    def _ManyNPC(self, Coox, Cooy):
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(0.5)
        pyautogui.moveTo(self.x/2, self.y/2,duration=0.5)
        time.sleep(0.5)
        pyautogui.click(self.x/2, self.y/2)
        time.sleep(0.5)
        # di tu
        time.sleep(1)
        pyautogui.press('m')

        # 817, 438

        # time.sleep(0.5)
        # pyautogui.moveTo(817, 438,duration=0.5)
        # time.sleep(0.5)
        #
        # 844, 564


        time.sleep(0.5)
        pyautogui.moveTo(817, 438,duration=0.5)
        time.sleep(0.1)
        pyautogui.doubleClick(844, 564)
        time.sleep(0.1)
        pyautogui.doubleClick(844, 564)
        time.sleep(0.1)
        pyautogui.doubleClick(844, 564)
        time.sleep(0.1)
        pyautogui.doubleClick(844, 564)

        # pyautogui.click(817, 438)
        # time.sleep(0.5)
        #
        # pyautogui.press('esc')
        # for i in range(30):
        #     time.sleep(0.5)
        #     pyautogui.click(844, 563)
        #     time.sleep(0.5)
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





















