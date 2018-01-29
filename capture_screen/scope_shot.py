import win32gui
import ctypes
from PIL import ImageGrab


class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_int), ('top', ctypes.c_int), ('right', ctypes.c_int), ('bottom', ctypes.c_int)]

rect = RECT()
HWND = win32gui.GetForegroundWindow()
ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))

coordinate = (rect.left+622, rect.top+2, rect.right-2, rect.bottom-2)
pic = ImageGrab.grab(coordinate)
pic.save("D:\\test\\xixi.png")
