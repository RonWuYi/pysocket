
# CT = 120

VALUE = raw_input('please in put VALUE: ')


# while True:
while True:
    for i in range(10):
        if i > 3 and i < 5:
            if int(VALUE) < 10:
                print 'i = ', repr(i)
                print "xiao yu 10"
            elif int(VALUE) < 100 and int(VALUE) > 10:
                print 'i = ', repr(i)
                print "100~10"
            else:
                print "other value"
                break
            continue
    continue