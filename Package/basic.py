from datetime import datetime as sm

class BASIC(object):
    def __init__(self, current_level = 80, current_zhuan_shen = 4):
        self.CurrentLevel = current_level
        self.zhuan_shen_level = current_zhuan_shen
        self.GuaJiFlag = True
        self.CurStatus = 'null'
        self.Seconds = 60
        # self.x, self.y = pyautogui.size()
        self.Year = str(sm.now())[0:4]
        self.Month = str(sm.now())[5:7]
        self.Day = str(sm.now())[8:10]

    def _time_diff(self, hh, mm=0, ss=0):
        current_time = sm.now()
        target_times = self.Year+'-'+self.Month+'-'+self.Day+' '+str(hh)+':'+str(mm)+':'+str(ss)+'.0'
        target_time = sm.strptime(target_times, "%Y-%m-%d %H:%M:%S.%f")
        if current_time < target_time:
            return (target_time-current_time).seconds
        else:
            return 0