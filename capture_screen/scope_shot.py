import win32gui
import ctypes
import time

from PIL import ImageGrab


class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_int), ('top', ctypes.c_int), ('right', ctypes.c_int), ('bottom', ctypes.c_int)]

rect = RECT()
HWND = win32gui.GetForegroundWindow()
ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))

time.sleep(2)
coordinate = (rect.left+319, rect.top+201, rect.right-319, rect.bottom-179)
pic = ImageGrab.grab(coordinate)
pic.save("C:\\Work\\pysocket\\capture_screen\\xixi55.png", quality = 100)
