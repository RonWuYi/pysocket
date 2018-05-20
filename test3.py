import urllib2

import urllib2



# print req
# html = req.read()
# for i in req:
#     print i

# import urllib2
# import cookielib
# req = "http://wan.douyu.com/game_frame/play_5003.php?sid=1017"
# cookie = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# for item in cookie:
#     print 'Name = ' + item.name
#     print 'Value = ' + item.value


import urllib2
req = urllib2.Request("http://wan.douyu.com/game_frame/play_5003.php?sid=1017")
response = urllib2.urlopen(req)
the_page = response.read()

print the_page