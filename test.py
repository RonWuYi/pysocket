import time

# CT = (time.localtime()[3]*100) + (time.localtime()[4])
# print CT
from AllWay import AW
SPlay = AW()

time.sleep(2)
SPlay.TabQieHuan()
SPlay.InIt()
SPlay.CaiLiaoFuBen()
SPlay.HuiShou()
SPlay.InIt()
SPlay.TaFangFengMo()
SPlay.HuiShou()
SPlay.InIt()
SPlay.JingYingRenWu()
SPlay.HuiShou()
SPlay.InIt()
SPlay.GongXunRenWu()
SPlay.HuiShou()
SPlay.InIt()
SPlay.ChuMoRenWu()
while True:
    SPlay.InIt()
    SPlay.GuaJi()
    time.sleep(3600)
    SPlay.HuiShou()