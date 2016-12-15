# -*- coding: UTF-8 -*-
'''
Created on 2015/4/23
Author: duwb
Email: wenbindu@yeah.net
'''
#run the function every 5 minutes or other time.

import datetime
import threading
# 比较时间，如果前者小于等于后者，返回true.
# 否则返回false
# 输入格式：时间字符串 '10:10:01'，返回类型：true / false
def compareTime(a,b):        
         # 对字符串格式时间进行格式化，转为时间类型。
         time_a = datetime.datetime.strptime(a,'%H:%M:%S')
         time_b = datetime.datetime.strptime(b,'%H:%M:%S')
         return time_a <= time_b
# 获取当前年，日期和时间
# 获取当前第几周，周几信息。
# 返回类型：dictionary {'time':'10:10:01','date':'2015-05-05'}
def get_now():
         now = datetime.datetime.now()
         date = now.strftime('%Y-%m-%d')
         time =  now.strftime('%H:%M:%S')
         week = now.isocalendar()
         year = week[0]
         week_num = week[1]
         week_day = week[2]
         dic = {}
         dic['date']=date
         dic['time']=time
         dic['weekNum']=week_num
         dic['weekDay']=week_day
         dic['year']=year
         return dic


# a=datetime.datetime.strptime('8:15:56','%H:%M:%S')
# b=datetime.datetime.strptime('8:16:56','%H:%M:%S')
# print((b-a).seconds)
