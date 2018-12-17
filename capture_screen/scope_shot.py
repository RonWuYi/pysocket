import win32gui
import ctypes
import threading
import time

from PIL import ImageGrab
# from time import time, localtime, strftime


class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_int), ('top', ctypes.c_int), ('right', ctypes.c_int), ('bottom', ctypes.c_int)]

# rect = RECT()

class c(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # self.weekday = weekday

    def run(self):
        rect = RECT()
        HWND = win32gui.GetForegroundWindow()
        ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))

        time.sleep(2)
        coordinate = (rect.left + 319, rect.top + 201, rect.right - 319, rect.bottom - 179)
        pic = ImageGrab.grab(coordinate)
        pic.save("C:\\Work\\pysocket\\pic\\active\\{}_{}_{}.png".format(time.strftime("%A"), str(time.localtime()[3]), str(time.localtime()[4])), quality=100)
        time.sleep(100)


if __name__ == '__main__':
    run = c()
    run.start()