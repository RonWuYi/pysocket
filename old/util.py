import time
import pyautogui

from datetime import datetime as sm

pyautogui.PAUSE = 1.5
GongXunTime = 120
JinYinTime = 160
cai_liao_move_value = 30
fang_kuai_move_value = 56
ge_ren_boss_time = 19


def go_feng_mo_npc():
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
    # zhuang bei hui shou jie mian
    pyautogui.click(623, 630)
    time.sleep(0.5)
    pyautogui.click(521, 410)
    time.sleep(1)
    # hui shou kuangshi
    pyautogui.click(427, 558)
    time.sleep(2)
    # hui shou zhuang bei
    pyautogui.click(631, 558)
    time.sleep(2)
    # hui shou zhuang bei
    pyautogui.click(956, 558)
    time.sleep(2)

    # for i in range(2):
    # hui shou tianfumojin
    pyautogui.doubleClick(587, 728)
    time.sleep(1)
    # hui shou xueyu
    pyautogui.doubleClick(634, 728)
    time.sleep(1)
    # for i in range(2):
    # hui shou tianfumojin
    pyautogui.doubleClick(546, 728)
    time.sleep(1)
    # hui shou xueyu
    pyautogui.doubleClick(498, 728)
    time.sleep(1)

    # hui shou tianfumojin
    pyautogui.doubleClick(455, 728)
    time.sleep(1)
    # hui shou xueyu
    pyautogui.doubleClick(407, 728)
    time.sleep(1)

    _boss_hui_shou()


def _go_wei_wang_npc():
    customize_init()
    time.sleep(1)
    pyautogui.click(665, 676)
    time.sleep(1)
    pyautogui.click(877, 539)
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
    pyautogui.click(261, 138)
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
        pyautogui.click(198, 209)
    elif level == 2:
        time.sleep(1)
        pyautogui.click(198, (209+(level-1)*54))
    elif level == 3:
        time.sleep(1)
        pyautogui.click(198, (209+(level-1)*54))
    elif level == 4:
        time.sleep(1)
        pyautogui.click(198, (209+(level-1)*54))
    else:
        time.sleep(1)
        pyautogui.click(198, 433)


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


def tab_qie_huan():
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

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
    # new add after added xin fa
    pyautogui.click(660, 200)
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
        pyautogui.click(197, (317+fang_kuai_move_value))
        time.sleep(1)
    elif ge_su == 5:
        pyautogui.click(197, (317+fang_kuai_move_value*2))
        time.sleep(1)
    elif ge_su == 6:
        pyautogui.click(197, (317+fang_kuai_move_value*3))
        time.sleep(1)
    elif ge_su == 7:
        pyautogui.click(197, (317+fang_kuai_move_value*4))
        time.sleep(1)
    elif ge_su == 8:
        pyautogui.click(197, (317+fang_kuai_move_value*5))
        time.sleep(1)
    else:
        pyautogui.click(197, (317+fang_kuai_move_value*6))
        time.sleep(1)

    pyautogui.click(628, 206)
    time.sleep(1)


def re_start(sleep_time):
    time.sleep(1)
    pyautogui.click(1008,  14)

    time.sleep(3)
    pyautogui.click(481, 454)

    time.sleep(10)

    pyautogui.click(360, 286)
    time.sleep(sleep_time)

    pyautogui.click(798, 236)
    time.sleep(2)



def cun_ru_cang_ku():
    time.sleep(4)
    pyautogui.click(852, 685)

    time.sleep(2)
    pyautogui.click(309, 204)

    for i in range(7):
        time.sleep(2)
        pyautogui.doubleClick(194, 269)

    _boss_hui_shou()


def qi_fu():
    time.sleep(1)
    pyautogui.click(915, 602)

    time.sleep(1)
    pyautogui.click(359, 607)

    time.sleep(1)
    pyautogui.click(665, 609)

    _xiao_chu_jie_mian()


def lan_yue_da_ren():
    time.sleep(1)
    pyautogui.click(508, 140)

    time.sleep(1)
    pyautogui.click(514, 549)

    time.sleep(1)

    _xiao_chu_jie_mian()

def fu_li_da_ting():
    time.sleep(1)
    pyautogui.click(443, 140)
    time.sleep(1)
    pyautogui.click(214, 207)

    time.sleep(1)
    pyautogui.click(810, 556)

    # time.sleep(1)
    # # zuo bian
    # pyautogui.click(212, 208)


    time.sleep(1)
    # zuo bian
    pyautogui.click(212, 254)

    time.sleep(1)
    pyautogui.click(586, 458)

    time.sleep(1)
    pyautogui.click(810, 573)

    time.sleep(1)
    # zuo bian
    pyautogui.click(212, 303)

    # time.sleep(1)
    # pyautogui.click(586, 459)

    time.sleep(1)
    pyautogui.click(819, 444)

    time.sleep(1)
    pyautogui.click(665, 609)

    time.sleep(1)
    pyautogui.click(820, 446)

    _xiao_chu_jie_mian()


# def sui_shi_ya_biao():
#     pass

def sui_shi_ya_biao(run_times=3,
                    wait_time=20, ge_su=3):
    print "Start yabiao at {}"\
        .format(current_date_time())
    # self.GuaJiFlag = False
    # self.CurStatus = 'JinYanGongXun'

    for i in range(run_times):
        _bao_wu_jie_mian(ge_su)

        # NPC
        time.sleep(1)
        pyautogui.click(793, 550)

        # Jie qu
        time.sleep(1)
        pyautogui.click(509, 581)

        # shua chu
        time.sleep(1)
        pyautogui.click(412, 545)

        # shua xin
        time.sleep(1)
        pyautogui.click(650, 551)

        # Hu Song
        time.sleep(wait_time)
        pyautogui.click(936, 549)

        time.sleep(1)
        pyautogui.click(512, 453)

        if i == 0:
            time.sleep(55)
        else:
            time.sleep(160)
    # for i in range(run_times):
    #
    #     time.sleep(1)
    #     pyautogui.click(622, 527)
    #     time.sleep(8)
    #
    #     # jie shou ren wu
    #     pyautogui.click(509, 567)
    #     time.sleep(1)
    #
    #     # qian wang wan cheng ren wu
    #     pyautogui.click(509, 567)
    #
    #     # deng dai wan cheng
    #     time.sleep(wait_time+extra_time)
    #
    #     # dian ji di mian (fang zi wa kuang cuo wo)
    #     # click chuan
    #     time.sleep(1)
    #     pyautogui.click(793, 583)
    #
    #     # wan cheng ren wu - san bei jiang li
    #     time.sleep(2)
    #     pyautogui.click(610, 511)
    #     time.sleep(1)

    # print "GongXunRenWu complete at {}"\
    #     .format(current_date_time())
    # customize_init()
    # self.GongXunRenWuComplete = True

