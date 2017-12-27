import pyautogui
import time

pyautogui.PAUSE = 1.5

class AW():
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

    def TabQieHuan(self):
        time.sleep(1)
        try:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
        except:
            print "except"
        self.GuaJiFlag = False

    def GongXunRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'JinYanGongXun'
        self.EventTime += 1
        time.sleep(1)

        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=1)
        time.sleep(1)
        pyautogui.click()

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(518, 636, duration=1)
        time.sleep(1)
        pyautogui.click()

        #clict "zi dong shua xin"
        pyautogui.moveTo(622, 544)
        time.sleep(1)
        pyautogui.click(622, 544)
        time.sleep(8)

        # clict "jie shou ren wu"/" qu wan cheng ren wu"
        pyautogui.click(508, 585)
        time.sleep(1)
        pyautogui.click(508, 585)

        # deng dai ren wu wan cheng
        time.sleep(102)

        # press esc for "wa kuang" ren wu
        time.sleep(1)
        pyautogui.press('esc')

        # click wan cheng "chuan"
        time.sleep(0.5)
        pyautogui.click(901, 423)
        time.sleep(1)

        # click "san bei jiang li"
        pyautogui.click(609, 529)
        time.sleep(1)

        for i in range(9):
            # clict "zi dong shua xin"
            pyautogui.moveTo(622, 544)
            time.sleep(1)
            pyautogui.click(622, 544)
            time.sleep(8)

            # clict "jie shou ren wu"/" qu wan cheng ren wu"
            pyautogui.click(508, 585)
            time.sleep(1)
            pyautogui.click(508, 585)

            # deng dai ren wu wan cheng
            time.sleep(102)

            # press esc for "wa kuang" ren wu
            time.sleep(1)
            pyautogui.press('esc')

            # click wan cheng "chuan"
            time.sleep(0.5)
            pyautogui.click(901, 423)
            time.sleep(1)

            # click "san bei jiang li"
            pyautogui.click(609, 529)
            time.sleep(1)

        self.GongXunRenWuComplete = True

    def JingYingRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'TianFu'
        self.EventTime += 1

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=1)
        time.sleep(1)
        pyautogui.click()

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(518, 636, duration=1)
        time.sleep(1)
        pyautogui.click()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('esc')

        time.sleep(1)
        pyautogui.moveTo(680, 517,duration=1)
        time.sleep(1)
        pyautogui.click(button='right', clicks=1)
        time.sleep(1)
        pyautogui.click(button='right', clicks=1)

        # click NPC
        time.sleep(1)
        pyautogui.moveTo(748, 341,duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # clict "jie shou ren wu"/" qu wan cheng ren wu"
        time.sleep(1)
        pyautogui.moveTo(508, 585,duration=0.5)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(110)

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=1)
        time.sleep(1)
        pyautogui.click()

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(518, 636, duration=1)
        time.sleep(1)
        pyautogui.click()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('esc')

        time.sleep(1)
        pyautogui.moveTo(680, 517,duration=1)
        time.sleep(1)
        pyautogui.click(button='right', clicks=1)
        time.sleep(1)
        pyautogui.click(button='right', clicks=1)

        # click NPC
        time.sleep(1)
        pyautogui.moveTo(748, 341,duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # click "san bei jiang li"
        time.sleep(1)
        pyautogui.moveTo(610, 528)
        pyautogui.click()


        for j in range(9):
            # clict "jie shou ren wu"/" qu wan cheng ren wu"
            pyautogui.moveTo(508, 585)

            pyautogui.click()

            pyautogui.click()
            time.sleep(240)
            # pyautogui.PAUSE = 240

            time.sleep(1)
            # da kai jie mian
            pyautogui.press('j')

            # ri chang ren wu
            time.sleep(1)
            pyautogui.moveTo(285, 225, duration=1)
            time.sleep(1)
            pyautogui.click()

            # jie qu ren wu
            time.sleep(1)
            pyautogui.moveTo(518, 636, duration=1)
            time.sleep(1)
            pyautogui.click()

            time.sleep(1)
            # da kai jie mian
            pyautogui.press('esc')

            time.sleep(1)
            pyautogui.moveTo(680, 517, duration=1)
            time.sleep(1)
            pyautogui.click(button='right', clicks=1)
            time.sleep(1)
            pyautogui.click(button='right', clicks=1)

            # click NPC
            time.sleep(1)
            pyautogui.moveTo(748, 341, duration=0.5)
            pyautogui.click()
            time.sleep(1)

            # click "san bei jiang li"
            pyautogui.moveTo(610, 528)

            pyautogui.click()

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
        x, y = pyautogui.size()
        pyautogui.moveTo(x / 2, y / 2, duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=1)
        time.sleep(1)
        pyautogui.click()

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(750, 633, duration=1)
        time.sleep(1)
        pyautogui.click()

        pyautogui.moveTo(308, 327,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # jie shou xuan shang
        pyautogui.moveTo(647, 546,duration=0.5)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        # chuan
        pyautogui.moveTo(707, 507,duration=0.5)
        time.sleep(1)
        pyautogui.click()
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
        x, y = pyautogui.size()
        pyautogui.moveTo(x / 2, y / 2, duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=1)
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
        x, y = pyautogui.size()
        pyautogui.moveTo(x / 2, y / 2, duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=1)
        time.sleep(1)
        pyautogui.click()

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(750, 633, duration=1)
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

        for jj in range(3):
            time.sleep(1)
            # da kai jie mian
            pyautogui.press('j')

            # ri chang ren wu
            time.sleep(1)
            pyautogui.moveTo(281, 227,duration=1)
            time.sleep(1)
            pyautogui.click()

            # jie qu ren wu
            time.sleep(1)
            pyautogui.moveTo(278, 635,duration=1)
            time.sleep(1)
            pyautogui.click()

            # jin ru feng mo gu
            pyautogui.moveTo(505, 611,duration=1)
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
            time.sleep(500)

            # lin qu jiang li
            pyautogui.moveTo(604, 398,duration=1)
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
        pyautogui.moveTo(359, 225, duration=1)
        time.sleep(1)
        pyautogui.click()

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(281, 470, duration=1)
        time.sleep(1)
        pyautogui.click()

        for i in range(2):
            for iii in range(0, 7):
                moveValue = 30;

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
        pyautogui.moveTo(932, 462,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()

        # jiao shu
        time.sleep(1)
        pyautogui.moveTo(545, 588,duration=1)
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
        pyautogui.moveTo(945, 238,duration=1)
        time.sleep(1)
        pyautogui.click()

        # xiao chu wu yong dui hua kuang
        time.sleep(1)
        pyautogui.press('esc')
        pyautogui.click()
        time.sleep(1)

        # click NPC
        pyautogui.moveTo(316, 133,duration=1)
        time.sleep(1)
        pyautogui.click()

        # jin ru chuang tian guan
        pyautogui.moveTo(507, 618,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(900)
        time.sleep(1)
        pyautogui.moveTo(511, 533,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1800)

        self.ChuMoRenWuComplete = True

    def HuiShou(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HuiShou'
        self.EventTime += 1

        # da kai bei bao jie mian
        time.sleep(1)
        pyautogui.press('b')
        time.sleep(1)
        pyautogui.moveTo(627, 627)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(521, 427)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        # hui shou kuang shi
        pyautogui.moveTo(602, 575)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        # hui shou zhuang bei
        pyautogui.moveTo(804, 575)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        pyautogui.press('esc')
        time.sleep(0.5)
        self.InIt()
        time.sleep(0.5)

        self.InIt()

        for i in range(2):
            time.sleep(0.5)
            # pyautogui.press('e')
            # time.sleep(0.5)
            # pyautogui.press('e')
            # time.sleep(0.5)
            pyautogui.press('q')
            time.sleep(0.5)
            pyautogui.press('q')
            time.sleep(0.5)
            pyautogui.press('w')
            time.sleep(0.5)
            pyautogui.press('w')
            # time.sleep(0.5)
            # pyautogui.press('f')

        self._WoYaoBianQaing()

        # wo yao zhuang bei
        time.sleep(1)
        pyautogui.moveTo(408, 279, duration=0.5)
        time.sleep(1)
        pyautogui.click(408, 279, )

        # tiao zhan boss
        time.sleep(1)
        pyautogui.moveTo(891, 301, duration=0.5)
        time.sleep(1)
        pyautogui.click(891, 301)

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
        pyautogui.moveTo(627, 627)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(521, 427)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        # hui shou kuang shi
        pyautogui.moveTo(602, 575)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        # hui shou zhuang bei
        pyautogui.moveTo(804, 575)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        pyautogui.press('esc')
        time.sleep(0.5)
        self.InIt()
        time.sleep(0.5)

        self.InIt()

        for i in range(2):
            time.sleep(0.5)
            # pyautogui.press('e')
            # time.sleep(0.5)
            # pyautogui.press('e')
            # time.sleep(0.5)
            pyautogui.press('q')
            time.sleep(0.5)
            pyautogui.press('q')
            time.sleep(0.5)
            pyautogui.press('w')
            time.sleep(0.5)
            pyautogui.press('w')
            # time.sleep(0.5)
            # pyautogui.press('f')

        pyautogui.press('esc')

    def GuaJi(self):
        self.GuaJiFlag = True
        self.CurStatus = 'GuaJi'
        self.EventTime += 1

        # move click gua ji
        pyautogui.moveTo(913, 576,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        pyautogui.moveTo(594, 435,duration=1)

        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        pyautogui.press('z')

    def WaKuang(self):
        self.GuaJiFlag = True
        self.CurStatus = 'WaKuang'
        self.EventTime += 1
        time.sleep(1)
        pyautogui.moveTo(1220, 611)
        time.sleep(1)
        time.sleep(100)
        pyautogui.click()
        time.sleep(1)

    def MoBaiChengZhu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'MoBaiChengZhu'
        self.EventTime += 1

        time.sleep(1)
        # pyautogui.moveTo(669, 474,duration=1)
        # time.sleep(1)
        # pyautogui.click()
        # time.sleep(1)
        self.RiChangHuoDong()

        for i in range(9):
            time.sleep(1)
            pyautogui.moveTo(587, 613,duration=1)
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
            pyautogui.moveTo(799, 535,duration=1)
            pyautogui.click()

        self.MoBaiChengZhuComplete =True

    def YeZhanBiQi(self):
        self.GuaJiFlag = False
        self.CurStatus = 'YeZhanBiQi'
        self.EventTime += 1

        self.RiChangHuoDong()
        pyautogui.press('z')
        time.sleep(1200)

        self.YeZhanBiQiComplete = True

    def ShenWei(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ShenWei'
        self.EventTime += 1

        self.RiChangHuoDong()
        pyautogui.press('z')
        time.sleep(3600)
        time.sleep(3600)

        self.ShenWeiComplete = True

    def WorldBoss(self):
        self.GuaJiFlag = False
        self.CurStatus = 'WorldBoss'
        self.EventTime += 1

        time.sleep(1)
        self.RiChangHuoDong()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1)
        time.sleep(2000)

        self.WorldBossComplete = True

    def JinZhuSongLi(self):
        self.GuaJiFlag = False
        self.CurStatus = 'JinZhuSongLi'
        self.EventTime += 1

        self.RiChangHuoDong()

        pyautogui.press('z')
        time.sleep(1)
        time.sleep(900)

        self.JingYingRenWuComplete = True

    def GeRenBoss(self):
        self.GuaJiFlag = False
        self.CurStatus = 'GeRenBoss'
        self.EventTime += 1

        for i in range(0,5):
            # time.sleep(1)
            # # da kai jie mian
            # pyautogui.press('c')
            #
            # # wo yao bian qiang
            # time.sleep(1)
            # pyautogui.moveTo(1020, 833, duration=0.5)
            # time.sleep(1)
            # pyautogui.click(1020, 833)

            self._WoYaoBianQaing()

            # wo yao zhuang bei
            time.sleep(1)
            pyautogui.moveTo(408, 279, duration=0.5)
            time.sleep(1)
            pyautogui.click(408, 279,)

            # tiao zhan boss
            time.sleep(1)
            pyautogui.moveTo(891, 301, duration=0.5)
            time.sleep(1)
            pyautogui.click(891, 301)

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
            time.sleep(1)
            self.InIt()
            time.sleep(1)
            pyautogui.press('z')
            time.sleep(1)

            time.sleep(30 + (i*18))

            # wan cheng ren wu
            time.sleep(1)
            pyautogui.moveTo(860, 608, duration=0.5)
            time.sleep(1)
            pyautogui.click(860, 608)

            self.HuiShou()

        self.GeRenBossiComplete = False

    def InIt(self):
        time.sleep(1)
        x, y = pyautogui.size()
        pyautogui.moveTo(x/2, y/2,duration=0.5)
        time.sleep(0.5)
        pyautogui.click(x/2, y/2)
        time.sleep(0.5)
        pyautogui.press('esc')
        # time.sleep(0.5)
        # pyautogui.click(x/2, y/2)
        # time.sleep(0.5)
        # pyautogui.press('esc')
        # time.sleep(0.5)

    def _WoYaoBianQaing(self):
        time.sleep(1)
        # da kai jie mian
        pyautogui.press('c')

        # wo yao bian qiang
        time.sleep(1)
        pyautogui.moveTo(577, 616, duration=0.5)
        time.sleep(1)
        pyautogui.click(577, 616)

    def GoFengMoNPC(self):
        time.sleep(1)
        # da kai jie mian
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(285, 225, duration=1)
        time.sleep(1)
        pyautogui.click()

        # jie qu ren wu
        time.sleep(1)
        pyautogui.moveTo(518, 636, duration=1)
        time.sleep(1)
        pyautogui.click()

        time.sleep(1)
        # da kai jie mian
        pyautogui.press('esc')

    def RiChangHuoDong(self):
        time.sleep(1)
        # da kai jie mian
        self.InIt()
        pyautogui.press('j')

        # ri chang ren wu
        time.sleep(1)
        pyautogui.moveTo(751, 633, duration=1)
        time.sleep(1)
        pyautogui.click(751, 633)

        # jin ru huo dong
        time.sleep(1)
        pyautogui.moveTo(511, 627, duration=1)
        time.sleep(1)
        pyautogui.click(511, 627)

        # xiao chu jie mian
        time.sleep(1)
        pyautogui.press('esc')

    def BiGuan(self):
        # time.sleep(1)
        # # da kai jie mian
        # self.InIt()
        # pyautogui.press('j')
        #
        # # ri chang ren wu
        # time.sleep(1)
        # pyautogui.moveTo(751, 633, duration=1)
        # time.sleep(1)
        # pyautogui.click(751, 633)
        #
        # # jin ru huo dong
        # time.sleep(1)
        # pyautogui.moveTo(511, 627, duration=1)
        # time.sleep(1)
        # pyautogui.click(511, 627)
        #
        # # xiao chu jie mian
        # time.sleep(1)
        # pyautogui.press('esc')
        #
        # # di tu
        # time.sleep(1)
        # pyautogui.press('m')

        self.RiChangHuoDong()

        # di tu
        time.sleep(1)
        pyautogui.press('m')

        # zuo biao x
        time.sleep(1)
        pyautogui.moveTo(613, 210, duration=1)
        time.sleep(1)
        pyautogui.click(613, 210)
        time.sleep(1)
        pyautogui.typewrite('31')

        # zuo biao y
        time.sleep(1)
        pyautogui.moveTo(713, 209, duration=1)
        time.sleep(1)
        pyautogui.click(713, 209)
        time.sleep(1)
        pyautogui.typewrite('26')

        # qian wang di dian
        time.sleep(1)
        pyautogui.moveTo(770, 209, duration=1)
        time.sleep(1)
        pyautogui.click(770, 209)

        # flag
        self.BiGuanComplete = False

    def GuaiWuGongCheng(self):
        self.GuaJiFlag = False
        self.CurStatus = 'GuaiWuGongCheng'
        self.EventTime += 1
        time.sleep(1)

        self.RiChangHuoDong()

        # gua ji ban ge xiao shi
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1750)

        self.GuaiWuGongChengComplete = False












