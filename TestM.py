class BASICA(object):
    def __init__(self, test):
        self.test = test
        self.opena()
        self.BFUCN()
        self.closea()
        print self.test + ' this is test'


    def opena(self):
        print "opena"

    def BFUCN(self):
        pass

    def closea(self):
        print "closea"


# class BASICB(object):
#     def __init__(self):
#         self.openb()
#         self.BFUCN()
#         self.closeb()
#
#
#     def openb(self):
#         print "openb"
#
#     def BFUCN(self):
#         pass
#
#     def closeb(self):
#         print "closeb"



class TESTA(BASICA):
    # super def __init__(self):
    #     self.func()


    def __init__(self, childtest, hardcode):
        super(TESTA, self).__init__(hardcode)
        # self.hardcode = hardcode
        self.childtest = childtest
        print "from child class TESTA"
        print self.childtest

    def BFUCN(self):
        print "func"


# class TESTB(BASICB):
#     # super def __init__(self):
#     #     self.func()
#     def BFUCN(self):
#         print "func"

x = TESTA('childtestinput', 'fathertestinput')

# y = TESTB()