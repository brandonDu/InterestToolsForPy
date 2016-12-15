#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#每月还本付息金额=（本金/还款月数）+（本金-累计已还本金）×月利率
#每月本金=总本金/还款月数
#每月利息=（本金-累计已还本金）×月利率
#还款总利息=（还款月数+1）×贷款额×月利率/2
#还款总额=（还款月数+1）×贷款额×月利率/2+ 贷款额
# 2750+11253 
# 2745.49+11231.11 
# 2740.98+11209.23 
# 2736.46+10943.92 = 13680.38
# 2731.95+10750.88 =  13482.83
def main():
	months = 240
	businessloan = 1440000
	wagesloan = 400000
	discount = 0.85
	_stage = []
	_stage.append([3,5.15*0.85,3.25])
	_stage.append([237,4.9*0.85,3.25])
	infList = []
	lastms = int(months)

	for stage in _stage:
		ms = stage[0]
		rateBusi = stage[1]/100
		rateWage = stage[2]/100
		#计算本息信息
		for x in range(0,ms,1):
			reMBusiness = repayPrincipalAndInterest(months,businessloan,lastms-x,rateBusi)
			reMWages = repayPrincipalAndInterest(months,wagesloan,lastms-x,rateWage)
			reAll = reMBusiness+reMWages			
			reM = str("%.2f"%round(reMBusiness,2))+" | "+str("%.2f"%round(reMWages,2))+" | "+str("%.2f"%round(reAll,2)) 
			infList.append(reM)
		lastms = lastms-ms
		infList.append('-----------------------------')
	print("\n".join(infList[0:10]))
#获取还款本金和利息和。
def repayPrincipalAndInterest(ms,prin,lastms,rate):
	reMoney = (prin/ms) + prin/ms*lastms*rate/12
	return reMoney
def everyMonthPrin(ms,prin):
	everyMonthPrin = prin / ms
	return everyMonthPrin
if __name__ == '__main__':
	main()