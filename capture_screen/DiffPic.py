from PIL import ImageGrab
import time
from PIL import Image, ImageChops, ImageStat
from os import remove
import os

# diff_img_file = 'diff_img_{}.jpg'

# def diff(im1_file, im2_file, delete_diff_file=False, diff_image_file=diff_img_file):
def diff(im1_file, im2_file):
    im1 = Image.open(im1_file)
    im2 = Image.open(im2_file)
    diff_img = ImageChops.difference(im1, im2)
    # diff_img.convert('RGB').save(diff_image_file)
    stat = ImageStat.Stat(diff_img)

    # can be [r,g,b] or [r,g,b,a]
    sum_channel_values = sum(stat.mean)
    max_all_channels = len(stat.mean) * 100
    diff_ratio =sum_channel_values/max_all_channels

    # if delete_diff_file:
    #     remove(diff_image_file)
    return diff_ratio
#
time.sleep(10)
# # x = ['1', '2', '3', '4', '5']
for i in range(12):
    # time.sleep(2)
    pic = ImageGrab.grab()
    pic.save("D:\\test\\picture_{}.jpg".format(str(i)))
    time.sleep(8)

y = []
z = []
list_dirs =os.walk("D:\\test")
for root, dirs, files in list_dirs:
    for f in files:
        # print os.path.join(root, f)
        y.append(os.path.join(root, f))

print y
for i in range(len(y)-1):
    z.append(diff(y[i], y[i+1]))

z.sort()

print sum(z)/len(z)

print sum(z[1:-1])/(len(z)-2)
