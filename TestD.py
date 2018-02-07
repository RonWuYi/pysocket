from time import gmtime, strftime
from datetime import datetime as sm
# print strftime("%a, %d %b %Y %H:%M:%S +0000", sm.now())


print sm.now()

print "Start BangHui at {}".format(sm.now().strftime('%b-%d-%y %H:%M:%S'))


x = sm.now()

print str(x)[0:19]