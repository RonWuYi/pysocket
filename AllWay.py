import pyautogui
import time

pyautogui.PAUSE = 1.5

class AW():
    def __init__(self):
        self.GuaJiFlag = True
        self.CurStatus = 'null'

    def TabQieHuan(self):
        time.sleep(1)
        try:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
        except:
            print "except"
        self.GuaJiFlag = False

    def JinYanGongXun(self):
        self.GuaJiFlag = False
        self.CurStatus = 'JinYanGongXun'
        time.sleep(1)
        pyautogui.moveTo(943, 422, duration=1,tween=pyautogui.easeInOutQuad)
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

        for i in range(8):
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

    def TianFu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'TianFu'
        time.sleep(1)
        pyautogui.moveTo(943, 422,duration=1,tween=pyautogui.easeInOutQuad)
        time.sleep(1)
        pyautogui.click()

        # clict "jie shou ren wu"/" qu wan cheng ren wu"
        time.sleep(1)
        pyautogui.moveTo(508, 585)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(30)
        # pyautogui.PAUSE = 240

        # wei wan cheng "chuan"
        pyautogui.moveTo(943, 422, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        time.sleep(20)

        # wei wan cheng "chuan"
        pyautogui.moveTo(943, 422, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        time.sleep(20)

        # wei wan cheng "chuan"
        pyautogui.moveTo(943, 422, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        time.sleep(20)

        # yi wan cheng "chuan"
        pyautogui.moveTo(901, 422)
        pyautogui.click()

        # click "san bei jiang li"
        time.sleep(1)
        pyautogui.moveTo(610, 528)
        pyautogui.click()


        # for j in range(9):
        #     # clict "jie shou ren wu"/" qu wan cheng ren wu"
        #     pyautogui.moveTo(508, 585)
        #
        #     pyautogui.click()
        #
        #     pyautogui.click()
        #     time.sleep(240)
        #     # pyautogui.PAUSE = 240
        #
        #     # chuan
        #     pyautogui.moveTo(901, 422)
        #
        #     pyautogui.click()
        #
        #     # click "san bei jiang li"
        #     pyautogui.moveTo(610, 528)
        #
        #     pyautogui.click()

    # Todo
    def WeiWangRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'WeiWangRenWu'
        ############ task 1 #########################################
        # click NPC
        time.sleep(1)
        pyautogui.moveTo(1466, 504,duration=0.5)
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

        # na dong xi
        x, y = pyautogui.size()
        pyautogui.moveTo(x/2, y/2,duration=0.5)
        time.sleep(1)
        pyautogui.click()

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

        ############ task 2 #########################################
        pyautogui.moveTo(607, 389,duration=0.5)
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
        pyautogui.moveTo(607, 485,duration=0.5)
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
        pyautogui.moveTo(607, 533,duration=0.5)
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

    def TaFangJingYan(self):
        self.GuaJiFlag = False
        self.CurStatus = 'TaFangJingYan'
        #################################################
        # ta fang jing yan
        #################################################
        for jj in range(3):
            # pyautogui.moveTo(1505, 422)
            time.sleep(1)
            pyautogui.moveTo(932, 460,duration=1)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()

            # jin ru feng mo gu
            pyautogui.moveTo(504, 609,duration=1)
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
            # pyautogui.moveTo(990, 545)

            # lin qu jiang li
            pyautogui.moveTo(604, 398,duration=1)
            pyautogui.click()

                # # dao lu dian ji dian
                # pyautogui.moveTo(1300, 410)

    def CaiLiaoFuBen(self):
        self.GuaJiFlag = False
        self.CurStatus = 'CaiLiaoFuBen'
        time.sleep(1)
        for iii in range(0, 7):
            moveValue = 30;
            # chuan
            time.sleep(1)
            pyautogui.moveTo(937, 460,duration=0.5)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            # fu ben ming zi
            # 514, 413
            pyautogui.moveTo(514, (413 + (iii * moveValue)),duration=0.5)
            time.sleep(1)
            pyautogui.click()

            # xia yi 10 pixels
            # pyautogui.moveRel(None, 10)
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
            else:
                time.sleep(130)

            # li kai fu ben / mian fei lin qu jiang li
            time.sleep(1)
            pyautogui.moveTo(859, 604,duration=0.5)
            time.sleep(1)
            pyautogui.click()

    def HuiShou(self):
        self.GuaJiFlag = False
        self.CurStatus = 'HuiShou'
        #################################################
        # hui shou
        #################################################
        pyautogui.moveTo(1460, 540)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(810, 456)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(889, 602)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(1092, 601)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.click()
        time.sleep(1)

    def GuaJi(self):
        self.GuaJiFlag = True
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

        # pyautogui.moveTo(494, 367)
        #
        # pyautogui.click()

    def WaKuang(self):
        self.GuaJiFlag = True
        self.CurStatus = 'WaKuang'
        time.sleep(1)
        pyautogui.moveTo(1220, 611)
        time.sleep(1)
        time.sleep(100)
        pyautogui.click()
        time.sleep(1)

    # Todo
    def ChuMoRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ChuMoRenWu'
        # chuan dao Zhang TianShi
        time.sleep(1)
        pyautogui.moveTo(932, 462,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        # time.sleep(2)
        # pyautogui.press('esc')
        # time.sleep(1)
        # pyautogui.moveTo(397, 495,duration=1)
        # time.sleep(1)
        # pyautogui.click(button='right', clicks=1)

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

    # Todo
    def ChuangTianGuan(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ChuangTianGuan'
        time.sleep(1)
        pyautogui.moveTo(912, 461,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(506, 616,duration=1)
        time.sleep(1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(560)
        time.sleep(1)
        pyautogui.moveTo(510, 533,duration=1)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)



