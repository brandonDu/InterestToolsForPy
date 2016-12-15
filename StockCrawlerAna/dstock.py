# -*- coding: UTF-8 -*-
'''
Created on 2015/04/23
Author:duwb
Email: wenbindu@yeah.net
'''
#根据stock key获取当前的stock info。
#input: key -> str
#output: stock_information -> dict
import urllib.request
#get the string from api of sina for stock.
#input: key of the stock ->str
#return: string of the stock information ->str
def http_get(key):
  try:
      #key is the id of the stock
      #fe: sh600241
      url = 'http://hq.sinajs.cn/list='+key
      response = urllib.request.urlopen(url).read()
      text = response.decode('GBK').encode('utf-8').decode('utf-8')
      return text
  except Exception as e:
      return str(e)
#analyse the string of the return data from the api of the sina with the key.
#input:data -> str
#output:stock information -> list
def get_list(data,key):
  arr = data.split('"')
  #get the information in the complex string.
  stock_info = arr[1].split(',')
  stock_info[0]=key    
  return stock_info
#map the values to the keys.
#input:arr of values ->list
#output:dict
def map_str(arr):
  arr_cn = ('no','todStarPri','yesEndPri','nowPri','todMaxPri','todMinPri',
            'nowBuyPri','nowSelPri','dealNum','dealMoney','buyOneNum','buyOnePri',
            'buyTwoNum','buyTwoPri','buyThrNum','buyThrPri','buyForNum',
            'buyForPri','buyFivNum','buyFivPri',
            'selOneNum','selOnePri','selTwoNum','selTwoPri','selThrNum',
            'selThrPri','selForNum','selForPri','selFivNum','selFivPri',
            'date','time','noMean')
  dictionary = dict(zip(arr_cn, arr))
  return dictionary
##def format_dic(dic):
##    dic['todStarPri'] = round(float(dic['todStarPri']),2)
##    dic['nowPri'] = round(float(dic['nowPri']),2)
##    dic['yesEndPri'] = round(float(dic['yesEndPri']),2)
##    dic['todMaxPri'] = round(float(dic['todMaxPri']),2)
##    dic['todMinPri'] = round(float(dic['todMinPri']),2)
##    dic['nowBuyPri'] = round(float(dic['nowBuyPri']),2)
##    dic['nowSelPri'] = round(float(dic['nowSelPri']),2)
##
##    dic['dealNum'] = int(dic['dealNum'])/100
##    dic['dealMoney'] = round(float(dic['dealMoney'])/10000 ,2)
##
##    dic['buyOneNum'] = int(dic['buyOneNum'])/100
##    dic['buyOnePri'] = round(float(dic['buyOnePri']),2)
##    dic['buyTwoNum'] = int(dic['buyTwoNum'])/100
##    dic['buyTwoPri'] = round(float(dic['buyTwoPri']),2)
##    dic['buyThrNum'] = int(dic['buyThrNum'])/100
##    dic['buyThrPri'] = round(float(dic['buyThrPri']),2)
##    dic['buyForNum'] = int(dic['buyForNum'])/100
##    dic['buyForPri'] = round(float(dic['buyForPri']),2)
##    dic['buyFivNum'] = int(dic['buyFivNum'])/100
##    dic['buyFivPri'] = round(float(dic['buyFivPri']),2)
##
##    dic['selOneNum'] = int(dic['selOneNum'])/100
##    dic['selOnePri'] = round(float(dic['selOnePri']),2)
##    dic['selTwoNum'] = int(dic['selTwoNum'])/100
##    dic['selTwoPri'] = round(float(dic['selTwoPri']),2)
##    dic['selThrNum'] = int(dic['selThrNum'])/100
##    dic['selThrPri'] = round(float(dic['selThrPri']),2)
##    dic['selForNum'] = int(dic['selForNum'])/100
##    dic['selForPri'] = round(float(dic['selForPri']),2)
##    dic['selFivNum'] = int(dic['selFivNum'])/100
##    dic['selFivPri'] = round(float(dic['selFivPri']),2)
##    return dic
#the main function to line the functions.
#input: key of the stock -> str
#output: information ot the stock with sina api -> dict
def get_stock(key):
  data = http_get(key)
  text = get_list(data,key)
  dict_stock = map_str(text)
  return dict_stock
# print(get_stock('sh600006'))
