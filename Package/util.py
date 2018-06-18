import time

from datetime import datetime as sm

fang_kuai_move_value = 56


def go_feng_mo_npc():
    time.sleep(1)
    pyautogui.click(337, 674)
    time.sleep(1)
    pyautogui.click(575, 598)
    time.sleep(1)
    pyautogui.click(412, 214)
    time.sleep(1)
    pyautogui.click(892, 220)


def boss_jie_mian():
    # da kai boss jie mian
    time.sleep(1)
    pyautogui.click(715, 188)
    time.sleep(1)


def huo_dong_jie_mian():
    time.sleep(0.5)
    pyautogui.click(951, 714)
    time.sleep(0.5)
    pyautogui.press('j')
    time.sleep(1)
    pyautogui.click(750, 615)
    time.sleep(0.5)


def xiao_chu_jie_mian():
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

    # for i in range(2):
    # hui shou tianfumojin
    pyautogui.doubleClick(587, 728)
    time.sleep(1)
    # hui shou xueyu
    pyautogui.doubleClick(634, 728)
    time.sleep(1)

    _boss_hui_shou()


def go_wei_wang_npc():
    customize_init()
    time.sleep(1)
    pyautogui.click(665, 676)
    time.sleep(1)
    pyautogui.click(877, 539)
    time.sleep(2)


def wo_yao_sheng_ji():
    time.sleep(1)
    pyautogui.click(335, 673)
    time.sleep(1)
    pyautogui.click(199, 212)
    time.sleep(1)
    pyautogui.click(576, 601)
    time.sleep(1)
    pyautogui.click(410, 214)
    time.sleep(1)


def huo_dong_jie_mian_no_click():
    time.sleep(0.5)
    pyautogui.click(951, 714)
    time.sleep(0.5)
    pyautogui.press('j')
    time.sleep(2)


def go_gua_ji_npc():
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


def lin_qu_huo_yue_jiang_li():
    xiao_chu_jie_mian()
    time.sleep(1)
    pyautogui.click(260, 128)
    for i in range(5):
        time.sleep(1)
        pyautogui.click(766, (373+i*57))
        time.sleep(1)


def xing_qi_ji():
    xing_qi = sm.now()
    return xing_qi.weekday()


def bao_wu_shen_dun_jie_mian():
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


def bao_wu_jie_mian(level):
    # da kai bao wu jie mian
    xiao_chu_jie_mian()
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


def go_to(xx, yy):
    xiao_chu_jie_mian()
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
    go_gua_ji_npc()
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
    customize_init()


def go_chu_mo_npc():
    wo_yao_sheng_ji()
    pyautogui.click(893, 413)
    time.sleep(11)


def seconds_change(total_seconds):
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    return "%02d:%02d:%02d:%02d" % (d, h, m, s)


def run_time():
    ss = sm.now()
    # put method below
    dd = sm.now()


def boss_hui_shou():
    time.sleep(1)
    pyautogui.click(714, 119)
    time.sleep(1)
    pyautogui.click(597, 197)
    time.sleep(1)
    pyautogui.click(719, 617)
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)


def yin_xiong_jie_mian(ge_su):
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
    else:
        pyautogui.click(197, (317+fang_kuai_move_value*3))
        time.sleep(1)

    pyautogui.click(628, 206)
    time.sleep(1)


def re_start(sleep_time):
    time.sleep(1)
    pyautogui.click(1008,  13)

    time.sleep(1)
    pyautogui.click(477, 457)

    time.sleep(5)

    time.sleep(1)
    pyautogui.click(366, 288)
    time.sleep(sleep_time)


def cun_ru_cang_ku():
    time.sleep(4)
    pyautogui.click(852, 685)

    time.sleep(2)
    pyautogui.click(309, 204)

    for i in range(7):
        time.sleep(2)
        pyautogui.doubleClick(194, 269)

    boss_hui_shou()


def da_boss():
    pass


def _wo_yao_bian_qiang_jie_mian():
    pass


def di_xia_gong_dian():
    pass


def zu_ma_boss():
    pass


def mi_jin():
    pass


def tab_qie_huan():
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    #self.GuaJiFlag = False