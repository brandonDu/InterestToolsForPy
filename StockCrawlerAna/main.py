# -*- coding: UTF-8 -*-
###
# Created on 2015/4/23
# Author: duwb
# Email: wenbindu@yeah.net
###
import time
import dthread
import dstock
import threading
import dtime
import datetime
from datetime import datetime as dt

# 主函数 根据时间定义进行启动判断 如果小于开始时间，则进行sleep，如果大于开始时间，则进行sleep。 如果在工作时间内，则直接开始运行
def main():
   # 定义开始时间和结束时间,以及间隔时间。
   interval = 300
   startTime = '14:50:01'
   endTime = '14:54:59'
   nowTime = dtime.get_now()['time']
   timeS= dt.strptime(startTime,'%H:%M:%S')
   timeE= dt.strptime(endTime,'%H:%M:%S')
   timeN=datetime.datetime.strptime(nowTime,'%H:%M:%S')
   timeY = datetime.datetime.strptime('23:59:59','%H:%M:%S')
   timeD = datetime.datetime.strptime('0:00:00','%H:%M:%S')
   if dtime.compareTime(nowTime,startTime):
            t = (timeS-timeN).seconds
   elif dtime.compareTime(endTime,nowTime):
            t = (timeY-timeN).seconds+(timeS-timeD).seconds
   else:
            t=0
   print(t)
   time.sleep(t)
   # 启动主线程，开始执行数据读取和写入。
   p=threading.Thread(target=dthread.timeThread,args=(startTime,endTime,interval,), name="计时线程")
   p.start()



if __name__ == '__main__':
   main()

