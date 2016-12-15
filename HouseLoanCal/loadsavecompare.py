# -*- coding: UTF-8 -*-
'''
本程序主要考虑对于不同还款方式
比较在一定利率下提前还款是否合适
From:wenbindu@yeah.net
'''
import math
from tabulate import tabulate

def main(x,y,z):
	#define the number of the months is 240
	mons = 240
	m_rate = y/100.0/12
	m_s_rate = x/100.0/12
	money_save = round(z)
	_money_save = round(z)
	#headers = ["月份","本金","利息","本息","储蓄","剩余","本金","利息","本息","储蓄","剩余"]
	headers = ["mons","capital","interest","repay","save","last","capital","interest","repay","save","last"]
	table = []
	#等额本息
	# 每月月供额=〔贷款本金×月利率×(1＋月利率)＾还款月数〕÷〔(1＋月利率)＾还款月数-1〕
	# 每月应还利息=贷款本金×月利率×〔(1+月利率)^还款月数-(1+月利率)^(还款月序号-1)〕÷〔(1+月利率)^还款月数-1〕
	# 每月应还本金=贷款本金×月利率×(1+月利率)^(还款月序号-1)÷〔(1+月利率)^还款月数-1〕
	# 总利息=还款月数×每月月供额-贷款本金
	
	for x in range(1,mons+1):
		#等额本息
		last_mon = mons-x
		mon_pay = z*m_rate*math.pow((m_rate+1),mons)/(math.pow((1+m_rate),mons)-1)
		mon_re_interest = z*m_rate*((1+m_rate)**mons-(1+m_rate)**(x-1))/((1+m_rate)**mons-1)
		mon_re_capital = z*m_rate*(1+m_rate)**(x-1)/((1+m_rate)**mons-1)
		money_earn = money_save*(1+m_s_rate)
		money_save = money_earn-(mon_re_interest+mon_re_capital)
		#等额本金
		_mon_re_capital = z/mons*1.0
		_mon_re_interest = z*1.0/mons*(mons-x+1)*m_rate
		_money_earn = _money_save*(1+m_s_rate)
		_money_save = _money_earn-(_mon_re_interest+_mon_re_capital)
		item = [x,round(mon_re_capital),round(mon_re_interest),round(mon_re_capital)+round(mon_re_interest),round(money_earn),round(money_save),round(_mon_re_capital),round(_mon_re_interest),round(_mon_re_capital)+round(_mon_re_interest),round(_money_earn),round(_money_save)]
		table.append(item)
	print(tabulate(table,headers,tablefmt="grid"))	


	#等额本金
	# 每月月供额=(贷款本金÷还款月数)+(贷款本金-已归还本金累计额)×月利率
	# 每月应还本金=贷款本金÷还款月数
	# 每月应还利息=剩余本金×月利率=(贷款本金-已归还本金累计额)×月利率
	# 每月月供递减额=每月应还本金×月利率=贷款本金÷还款月数×月利率
	# 总利息=还款月数×(总贷款额×月利率-月利率×(总贷款额÷还款月数)*(还款月数-1)÷2+总贷款额÷还款月数)


if __name__ == '__main__':
	rate_save = 4 #save rate 
	rate_loan = 4.9*0.85 #85 discount
	dr_money = 1840000 #100w
	main(rate_save,rate_loan,dr_money)
