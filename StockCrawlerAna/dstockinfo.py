# coding: utf-8
import csv
# 根据csv列表，读取信息并写入数组中。


def getCsv():
    stocks_ls = []
# 打开csv文件，定义打开编码格式，定义分隔符
# 将每条记录写入dictionary，并添加入数组
    with open('selStock.csv' ,encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
        for row in readCSV:
            stock_unit = {'no':row[0],'name':row[1],'remark':row[2]}
            stocks_ls.append(stock_unit)                           
    return stocks_ls

# print(getCsv())
