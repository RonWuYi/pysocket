import pyautogui
import time

pyautogui.PAUSE = 1.5

class AW():
    def __init__(self):
        self.GuaJiFlag = True
        self.CurStatus = 'null'
        self.Complete = False
        self.EventTime = 0

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
        self.Complete = False
        self.EventTime += 1
        time.sleep(1)

        x, y = pyautogui.size()
        pyautogui.moveTo(x/2, y/2,duration=0.5)
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

        self.Complete = True

    def JingYingRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'TianFu'
        self.Complete = False
        self.EventTime += 1

        x, y = pyautogui.size()
        pyautogui.moveTo(x/2, y/2,duration=0.5)
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
        time.sleep(140)
        # pyautogui.PAUSE = 240

        # # wei wan cheng "chuan"
        # pyautogui.moveTo(943, 422, duration=1, tween=pyautogui.easeInOutQuad)
        # pyautogui.click()
        # time.sleep(20)
        #
        # # wei wan cheng "chuan"
        # pyautogui.moveTo(943, 422, duration=1, tween=pyautogui.easeInOutQuad)
        # pyautogui.click()
        # time.sleep(20)
        #
        # # wei wan cheng "chuan"
        # pyautogui.moveTo(943, 422, duration=1, tween=pyautogui.easeInOutQuad)
        # pyautogui.click()
        # time.sleep(20)

        # yi wan cheng "chuan"
        pyautogui.moveTo(901, 422)
        pyautogui.click()

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

            # chuan
            pyautogui.moveTo(901, 422)

            pyautogui.click()

            # click "san bei jiang li"
            pyautogui.moveTo(610, 528)

            pyautogui.click()

        self.Complete = True
    # Todo
    def WeiWangRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'WeiWangRenWu'
        self.Complete = False
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

        self.Complete = True

    def TaFangFengMo(self):
        self.GuaJiFlag = False
        self.CurStatus = 'TaFangFengMo'
        self.Complete = False
        self.EventTime += 1

        x, y = pyautogui.size()
        pyautogui.moveTo(x/2, y/2,duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

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

        self.Complete = True

    def CaiLiaoFuBen(self):
        self.GuaJiFlag = False
        self.CurStatus = 'CaiLiaoFuBen'
        self.Complete = False
        self.EventTime += 1
        time.sleep(1)

        x, y = pyautogui.size()
        pyautogui.moveTo(x / 2, y / 2, duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(1)
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
            for iii in range(1, 7):
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

        self.Complete = True

    def ChuMoRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ChuMoRenWu'
        self.Complete = False
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

        self.Complete = True

    # Todo
    def ChuangTianGuan(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ChuangTianGuan'
        self.Complete = False
        self.EventTime += 1

        x, y = pyautogui.size()
        pyautogui.moveTo(x/2, y/2,duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

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
        # pyautogui.click(button='right', clicks=1)
        # time.sleep(1)
        # pyautogui.click(button='right', clicks=1)
        # time.sleep(1)
        # pyautogui.click(button='right', clicks=1)

        # jin ru chuang tian guan
        pyautogui.moveTo(507, 618,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(900)
        time.sleep(1)
        pyautogui.moveTo(511, 533,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

        self.Complete = True

    def HuiShou(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HuiShou'
        #################################################
        # hui shou
        #################################################
        x, y = pyautogui.size()
        pyautogui.moveTo(x/2, y/2,duration=0.5)
        time.sleep(0.5)
        pyautogui.click()
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
        pyautogui.moveTo(602, 575)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        # pyautogui.click()
        # time.sleep(2)
        pyautogui.moveTo(804, 575)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        # pyautogui.click()
        # time.sleep(1)

    def GuaJi(self):
        self.GuaJiFlag = False
        self.CurStatus = 'GuaJi'
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
        time.sleep(1)
        pyautogui.moveTo(1220, 611)
        time.sleep(1)
        time.sleep(100)
        pyautogui.click()
        time.sleep(1)

    def ShuangBeiGuaJi(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ChuangTianGuan'
        self.Complete = False
        self.EventTime += 1
        time.sleep(1)
        pyautogui.moveTo(662, 474,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        # time.sleep(1)
        # pyautogui.click()
        # time.sleep(1)
        pyautogui.moveTo(594, 435,duration=1)
        time.sleep(1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        pyautogui.press('z')
        time.sleep(3500)
        while self.Progress:
            if time.localtime()[4] < 10:
                CT = str(time.localtime()[3]) + '0' + str(time.localtime()[4])
            else:
                CT = str(time.localtime()[3]) + str(time.localtime()[4])
            if int(CT) - 1730 <= 0:
                self.Complete = True
            break

    def MoBaiChengZhu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'MoBaiChengZhu'
        self.Complete = False
        self.EventTime += 1
        time.sleep(1)
        pyautogui.moveTo(669, 474,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        # time.sleep(1)
        # pyautogui.click()
        for i in range(1):
            time.sleep(1)
            pyautogui.moveTo(587, 613,duration=1)
            time.sleep(1)
            for i in range(4):
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
            pyautogui.moveTo(799, 535,duration=1)
            pyautogui.click()
        self.Complete = True

    def YeZhanBiQi(self):
        self.GuaJiFlag = False
        self.CurStatus = 'MoBaiChengZhu'
        self.Complete = False
        self.EventTime += 1
        time.sleep(1)
        pyautogui.moveTo(669, 474,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1)

    def ShenWei(self):
        self.GuaJiFlag = False
        self.CurStatus = 'MoBaiChengZhu'
        self.Complete = False
        self.EventTime += 1
        time.sleep(1)
        pyautogui.moveTo(669, 474,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1)

    def WorldBoss(self):
        self.GuaJiFlag = False
        self.CurStatus = 'MoBaiChengZhu'
        self.Complete = False
        self.EventTime += 1
        time.sleep(1)
        pyautogui.moveTo(669, 474,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('z')
        time.sleep(1)

    def InIt(self):
        time.sleep(1)
        pyautogui.moveTo(1016, 398,duration=1)
        for i in range(13):
            time.sleep(0.4)
            pyautogui.click()
            time.sleep(0.4)









