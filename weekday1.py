from datetime import datetime
import time


print(type(datetime.now()))
print str(datetime.now())[11:13]


print(time.localtime())
# for x in time.localtime():
#     print(x)
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print(time.localtime()[3])
print(time.localtime()[4])