import os
import time
import win32gui

from PIL import ImageGrab, Image, ImageChops, ImageStat


class HST_MOTION():
    """
    based on python3
    """
    def __init__(self, savetime):
        self.file_path = "C:\\test"
        # self.PictureList = []
        # please assgin a odd number there and bigger than 5
        self.savetime = savetime
        self.y = []
        self.z = []

    def callback(self, hwnd, picturelist):
        if win32gui.GetClassName(hwnd) == "#32770":
            picturelist.append(hwnd)
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            coordinate = (x, y, w, h)

            for i in range(self.savetime):
                pic = ImageGrab.grab(coordinate)
                if os.path.isdir(self.file_path):
                    pic.save((self.file_path + "\\picture_{}.jpg").format(
                        str(time.localtime(time.time())[4]) + str(time.localtime(time.time())[5]) + str(
                            time.localtime(time.time())[6])))
                    time.sleep(10)
                else:
                    os.mkdir(self.file_path)
                    pic.save((self.file_path + "\\picture_{}.jpg").format(
                        str(time.localtime(time.time())[4]) + str(time.localtime(time.time())[5]) + str(
                            time.localtime(time.time())[6])))
                    time.sleep(10)
            print("Window finded")
        else:
            print("Find a window, but not the target window")

    def diff(self, im1_file, im2_file):
        im1 = Image.open(im1_file)
        im2 = Image.open(im2_file)
        diff_img = ImageChops.difference(im1, im2)
        stat = ImageStat.Stat(diff_img)
        sum_channel_values = sum(stat.mean)
        max_all_channels = len(stat.mean) * 100
        diff_ratio = sum_channel_values / max_all_channels
        return diff_ratio

    def cleanup(self, new_file_path):
        if os.path.exists(new_file_path):
            for the_file in os.listdir(new_file_path):
                filepath = os.path.join(new_file_path, the_file)
                try:
                    if os.path.isfile(filepath):
                        os.unlink(filepath)
                    # print("Clean up complete!")
                except Exception as e:
                    print(e)
        else:
            print("Target folder does not exist")

    def get_motion_state(self):
        self.cleanup(self.file_path)
        time.sleep(3)
        mainHwnd = win32gui.GetForegroundWindow()
        picturelist = []
        win32gui.EnumChildWindows(mainHwnd, self.callback, picturelist)
        list_dirs = os.walk(self.file_path)
        for root, dirs, files in list_dirs:
            for f in files:
                self.y.append(os.path.join(root, f))
        for i in range(len(self.y)-1):
            self.z.append(self.diff(self.y[i], self.y[i + 1]))
        self.z.sort()
        if sum(self.z[1:-1])/(len(self.z)-2) > 0.2:
            # self.cleanup(self.file_path)
            return True
        else:
            # self.cleanup(self.file_path)
            return False
