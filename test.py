import pyautogui
import time

pyautogui.PAUSE = 1.5

GongXunTime = 100
JinYinTime = 160

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

    def GongXunRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'JinYanGongXun'
        self.EventTime += 1
        time.sleep(1)

        # # da kai jie mian
        # pyautogui.press('j')

        # ri chang ren wu
        # time.sleep(1)
        # pyautogui.moveTo(285, 225, duration=0.5)
        time.sleep(1)
        pyautogui.click(943, 347)

        time.sleep(1)
        pyautogui.click(622, 527)
        time.sleep(8)


        # time.sleep(1)
        pyautogui.click(509, 567)
        time.sleep(1)
        # pyautogui.click(584, 569)

        pyautogui.click(509, 567)
        time.sleep(GongXunTime)
        pyautogui.press('esc')
        time.sleep(0.2)
        pyautogui.press('esc')
        time.sleep(0.2)
        pyautogui.click(900, 345)
        # jie qu ren wu
        # time.sleep(1)
        # pyautogui.moveTo(518, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(613, 510)
        time.sleep(1)
        for i in range(9):
            time.sleep(1)
            pyautogui.click(622, 527)
            time.sleep(8)

            # time.sleep(1)
            pyautogui.click(509, 567)
            time.sleep(1)
            # pyautogui.click(584, 569)

            pyautogui.click(509, 567)
            time.sleep(GongXunTime)
            pyautogui.press('esc')
            time.sleep(0.2)
            pyautogui.press('esc')
            time.sleep(0.2)
            pyautogui.click(900, 345)
            # jie qu ren wu
            # time.sleep(1)
            # pyautogui.moveTo(518, 636, duration=0.5)
            time.sleep(1)
            pyautogui.click(613, 510)
            time.sleep(1)



        # #clict "zi dong shua xin"
        # pyautogui.moveTo(622, 544, duration=0.5)
        # time.sleep(1)
        # pyautogui.click(622, 544)
        # time.sleep(8)
        #
        # # clict "jie shou ren wu"/" qu wan cheng ren wu"
        # pyautogui.click(508, 585)
        # time.sleep(1)
        # pyautogui.click(508, 585)
        #
        # # deng dai ren wu wan cheng
        # time.sleep(GongXunTime)
        #
        # # press esc for "wa kuang" ren wu
        # time.sleep(1)
        # pyautogui.press('esc')
        #
        # # click wan cheng "chuan"
        # time.sleep(0.5)
        # pyautogui.click(901, 423)
        # time.sleep(1)
        #
        # # click "san bei jiang li"
        # pyautogui.click(609, 529)
        # time.sleep(1)
        #
        # for i in range(9):
        #     # clict "zi dong shua xin"
        #     pyautogui.moveTo(622, 544, duration=0.5)
        #     time.sleep(1)
        #     pyautogui.click(622, 544)
        #     time.sleep(8)
        #
        #     # clict "jie shou ren wu"/" qu wan cheng ren wu"
        #     pyautogui.click(508, 585)
        #     time.sleep(1)
        #     pyautogui.click(508, 585)
        #
        #     # deng dai ren wu wan cheng
        #     time.sleep(GongXunTime)
        #
        #     # press esc for "wa kuang" ren wu
        #     time.sleep(1)
        #     pyautogui.press('esc')
        #
        #     # click wan cheng "chuan"
        #     time.sleep(0.5)
        #     pyautogui.click(901, 423)
        #     time.sleep(1)
        #
        #     # click "san bei jiang li"
        #     pyautogui.click(609, 529)
        #     time.sleep(1)

        self.GongXunRenWuComplete = True

    def JingYingRenWu(self):
        self.GuaJiFlag = False
        self.CurStatus = 'TianFu'
        self.EventTime += 1

        # time.sleep(1)
        # # da kai jie mian
        # pyautogui.press('j')
        #
        # # ri chang ren wu
        # time.sleep(1)
        # pyautogui.moveTo(285, 225, duration=0.5)
        time.sleep(1)
        pyautogui.click(943, 347)
        # time.sleep(1)
        pyautogui.click(509, 567)
        time.sleep(1)
        pyautogui.click(509, 567)
        time.sleep(JinYinTime)

        # jie qu ren wu
        # time.sleep(1)
        # pyautogui.moveTo(518, 636, duration=0.5)
        time.sleep(1)
        pyautogui.click(901, 346)

        time.sleep(1)
        pyautogui.click(613, 510)
        time.sleep(1)

        for j in range(9):
            pyautogui.click(509, 567)
            time.sleep(1)
            pyautogui.click(509, 567)
            time.sleep(JinYinTime)

            # jie qu ren wu
            # time.sleep(1)
            # pyautogui.moveTo(518, 636, duration=0.5)
            time.sleep(1)
            pyautogui.click(901, 346)

            time.sleep(1)
            pyautogui.click(613, 510)
            time.sleep(1)

        self.JingYingRenWuComplete = True

    # def TaFangFengMo(self):
    #     self.GuaJiFlag = False
    #     self.CurStatus = 'TaFangFengMo'
    #     self.EventTime += 1
    #
    #     # self._BaoWuShenDunJieMian()
    #
    #     for jj in range(3):
    #         time.sleep(1)
    #         # da kai jie mian
    #         # pyautogui.press('j')
    #
    #         # ri chang ren wu
    #         # time.sleep(1)
    #         # pyautogui.moveTo(281, 227, duration=0.5)
    #         time.sleep(1)
    #         pyautogui.click(931, 385)
    #
    #         # jie qu ren wu
    #         time.sleep(1)
    #         pyautogui.moveTo(278, 635, duration=0.5)
    #         time.sleep(1)
    #         pyautogui.click()
    #
    #         # jin ru feng mo gu
    #         pyautogui.moveTo(505, 611, duration=0.5)
    #         pyautogui.click()
    #
    #         # kai shi shua guai
    #         pyautogui.moveTo(700, 414)
    #         pyautogui.click()
    #
    #         for ii in range(2):
    #             # dian
    #             pyautogui.moveTo(320, 415)
    #             pyautogui.click()
    #
    #             # dao lu dian ji dian, ren wu qian jin
    #             pyautogui.moveTo(754, 349)
    #             # pyautogui.rightClick(clicks=3, interval=0.5)
    #             pyautogui.click(button='right', clicks=1)
    #
    #             # du
    #             pyautogui.moveTo(415, 416)
    #             pyautogui.click()
    #
    #
    #             # dao lu dian ji dian, ren wu qian jin
    #             pyautogui.moveTo(754, 349)
    #             pyautogui.click(button='right', clicks=1)
    #
    #             # bin
    #             pyautogui.moveTo(509, 413)
    #             pyautogui.click()
    #
    #             # dao lu dian ji dian, ren wu qian jin
    #             pyautogui.moveTo(754, 349)
    #             pyautogui.click(button='right', clicks=1)
    #
    #             # bao
    #             pyautogui.moveTo(606, 415)
    #             pyautogui.click()
    #
    #             # dao lu dian ji dian, ren wu qian jin
    #             pyautogui.moveTo(754, 349)
    #             pyautogui.click(button='right', clicks=1)
    #
    #         # deng dai jie shu
    #         time.sleep(420)
    #
    #         # lin qu jiang li
    #         pyautogui.moveTo(604, 398, duration=0.5)
    #         pyautogui.click()
    #
    #     self.TaFangFengMoComplete = True


    # Todo
    def ChuangTianGuan(self):
        self.GuaJiFlag = False
        self.CurStatus = 'ChuangTianGuan'
        self.EventTime += 1

        # time.sleep(1)
        # # da kai jie mian
        # pyautogui.press('c')

        # # wo yao bian qiang
        # time.sleep(1)
        # pyautogui.moveTo(576, 616, duration=0.5)
        time.sleep(1)
        pyautogui.click(911, 503)

        time.sleep(1)
        pyautogui.click(507, 600)
        time.sleep(2000)
        time.sleep(1)
        pyautogui.click(511, 514)
        # # feng mo gu NPC
        # time.sleep(1)
        # pyautogui.moveTo(945, 238, duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        #
        # # xiao chu wu yong dui hua kuang
        # time.sleep(1)
        # pyautogui.press('esc')
        # pyautogui.click()
        # time.sleep(1)
        #
        # # click NPC
        # pyautogui.moveTo(316, 133, duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        #
        # # jin ru chuang tian guan
        # pyautogui.moveTo(507, 618, duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        # time.sleep(900)
        # time.sleep(1)
        # pyautogui.moveTo(511, 533, duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        # time.sleep(1800)

        self.ChuangTianGuanComplete = True

    def CaiLiaoFuBen(self):
        self.GuaJiFlag = False
        self.CurStatus = 'CaiLiaoFuBen'

        self.EventTime += 1
        time.sleep(1)
        # self.InIt()
        # # da kai jie mian
        # pyautogui.press('j')
        #
        # # ri chang ren wu
        # time.sleep(1)
        # pyautogui.moveTo(359, 225, duration=0.5)
        # time.sleep(1)
        # pyautogui.click()
        #
        # # jie qu ren wu
        # time.sleep(1)
        # pyautogui.moveTo(281, 470, duration=0.5)
        # time.sleep(1)
        # pyautogui.click()

        for i in range(2):
            for iii in range(0, 7):
                moveValue = 30;

                # xiao chu dui hua kuang
                time.sleep(1)
                pyautogui.press('esc')
                time.sleep(1)

                # click NPC
                # pyautogui.moveTo(605, 370,duration=0.5)
                # pyautogui.click()
                # time.sleep(1)
                pyautogui.click(939, 425)
                time.sleep(1)

                # fu ben ming zi
                # 514, 413
                # pyautogui.moveTo(514, (398 + (iii * moveValue)),duration=0.5)
                # time.sleep(1)
                pyautogui.click(514, (398 + (iii * moveValue)))

                # jin ru fu ben
                # time.sleep(1)
                # pyautogui.moveTo(498, 600,duration=0.5)
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
                    time.sleep(300)
                elif iii == 5:
                    time.sleep(75)
                elif iii == 6:
                    time.sleep(130)
                else:
                    time.sleep(130)

                # li kai fu ben / mian fei lin qu jiang li
                # time.sleep(1)
                # pyautogui.moveTo(859, 604,duration=0.5)
                time.sleep(1)
                pyautogui.click(860, 528)

        self.CaiLiaoFuBenComplete = True