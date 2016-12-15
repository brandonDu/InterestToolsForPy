# -*- coding: UTF-8 -*-
'''
Created on 2015/4/23
Author: duwb
Email: wenbindu@yeah.net
'''
import datetime
import time
import urllib.request, urllib.error, urllib.parse
import math
def main():
	#根据编码实例化获取实时数据
	stockData = GetData("sz131810")
	price = stockData.getRealTimeData()
	#计算10万盈利以及5万盈利，扣除手续费，最低1元，十万分之一
	benefitTen = round(100000*price/100/360-1,2)
	benefitFiv = round(50000*price/100/360-1,2)
	#获取当前时间
	vdate,vtime = getNow.getNowTime()
	#初始化建议措施
	advice = "No"
	if benefitFiv > 5:
		advice = "Yes"
	else:
		advice = "No"
	#输出格式化的时间，当前利率，五万盈利，十万盈利，和购买建议
	print("{:>10} {:>10} {:>10} {:>10} {:>10}".format(*[vtime,price,benefitFiv,benefitTen,advice]))
	#每10s进行数据获取计算
	#休眠
	time.sleep(10)
	#继续运行
	main()


#http://hq.sinajs.cn/list=sz131810
#object = "sz131810"
class GetData:
	"""从网站获取R-001的实时数据"""
	def __init__(self,stockcode):
		self.nums = set()
		self.code = stockcode
	#获取当前时间的代码对应的信息
	def getRealTimeData(self):
		url="http://hq.sinajs.cn/list="+str(self.code)
		res = urllib.request.urlopen(url).read()
		resdata = str(res.decode("GBK"))
		self.nums = resdata.split(",")
		#获取当前利率值
		nowPrice = float(self.nums[3])
		return nowPrice
#获取当前时间类
class getNow:
	"""docstring for getNow"""
	def getNowTime():
		now = datetime.datetime.now()
		vdate = now.strftime('%Y-%m-%d')
		vtime =  now.strftime('%H:%M:%S')
		return vdate,vtime
		

if __name__ == '__main__':
	#获取当前日期，时间
	nowDate,nowTime = getNow.getNowTime()
	print("Date:"+nowDate)	#输出当前时日
	print("{:>10} {:>10} {:>10} {:>10} {:>10}".format(*["Now-Time","Now-Rate","benefit-5","benefit-10","Advice"]))
	
	main()
