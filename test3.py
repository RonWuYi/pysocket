import urllib2
req = urllib2.Request("http://wan.douyu.com/game_frame/play_5003.php?sid=1017")
response = urllib2.urlopen(req)
the_page = response.read()

print the_page