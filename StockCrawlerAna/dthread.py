import time
import threading
import dstock
import dtime
import psycopg2
# 注册字符串缺省类型为unicode
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import psycopg2.pool

import dbtocsv
#定义线程
def timeThread(stime,etime,itime): 
    # 获取当前线程的名称
    name=threading.current_thread().getName()
    print(name+":线程启动......")
    # 定义数据库连接池的线程库以及相关配置
    # 地址，数据库名称，用户名，密码
    dsn = "host=localhost dbname=dstock user=postgres password=postgres"
    pool = psycopg2.pool.ThreadedConnectionPool( minconn=2,maxconn=10, dsn=dsn)
    #根据表模板建立新表。
    # 根据日期创建表名称
    day = dtime.get_now()['date']
    tablename = "stock_"+day.replace('-','_')
    # 从连接池获取连接-数据库
    conn = pool.getconn()
    try:
        # 尝试首次建立当日数据表，根据模板字段进行表新建。
         with conn.cursor() as cur:                
                sql = "drop table if exists "+tablename+"; create table "+tablename+" as select no, todStarPri, yesEndPri, nowPri, todMaxPri, todMinPri, nowBuyPri, nowSelPri, dealNum, dealMoney, buyOneNum, buyOnePri, buyTwoNum, buyTwoPri, buyThrNum, buyThrPri, buyForNum, buyForPri, buyFivNum, buyFivPri, selOneNum, selOnePri, selTwoNum, selTwoPri, selThrNum, selThrPri, selForNum, selForPri, selFivNum, selFivPri, date, time, noMean from stock_time_templete;"
                cur.execute(sql)
                conn.commit()
    finally:
        #无论任何情况，将连接放回数据池。
        pool.putconn(conn)
    # 获取当前时间，并进行判断，判断是否超出了预定义时间。
    a=dtime.get_now()['time']
    c = dtime.compareTime(a,etime)
    while c:        
        # 开启新的线程，定义线程名称。
        # 该线程去完成读取数据并写入数据库的操作
        p = threading.Thread(target = co,args=(pool,),name=tablename)
        p.start()
        # 休眠5分钟
        time.sleep(itime)
        # 比较时间
        t = dtime.get_now()['time']
        c = dtime.compareTime(t,etime)
    dbtocsv.writeDbCsv(tablename,pool)
    input("press return to exit  ^_^")

# 获取结构数据库表以及根据api获取信息并写入数据库的线程。
def co(pool): 
    # 获取线程名称
    name=threading.current_thread().getName()
    print('{'+name+"}线程启动......")
    # 提取连接
    conn = pool.getconn()
    try:
         with conn.cursor() as cur:                
                # 获取股票信息
                sql = "select no,name from stock_inf where remark = '1';"
                cur.execute(sql)
                # 对每个股票进行当前数据获取并写入数据库
                for row in cur:
                    key = str(row[0])
                    # 根据编码，通过api获取股票当前交易详细信息
                    stock_info_key = dstock.get_stock(key)
                    # 节点输出
                    print(dtime.get_now()['time'])
                    # 将获取的数据插入数据库
                    cur_in = conn.cursor()
                    sql = '''insert into '''+name+''' (no,todstarpri,yesEndPri,nowPri ,todMaxPri,todMinPri,nowBuyPri,
                                nowSelPri,dealNum,dealMoney,buyOneNum,buyOnePri,buyTwoNum,buyTwoPri,buyThrNum,
                                 buyThrPri,buyForNum,buyForPri,buyFivNum,buyFivPri,selOneNum,selOnePri,selTwoNum,
                                 selTwoPri,selThrNum,selThrPri,selForNum,selForPri,selFivNum,selFivPri,date ,time,noMean) values (
                                 %(no)s,%(todStarPri)s, %(yesEndPri)s, %(nowPri)s, %(todMaxPri)s, %(todMinPri)s, %(nowBuyPri)s,
                                 %(nowSelPri)s, %(dealNum)s, %(dealMoney)s, %(buyOneNum)s, %(buyOnePri)s, %(buyTwoNum)s,
                                 %(buyTwoPri)s, %(buyThrNum)s, %(buyThrPri)s, %(buyForNum)s, %(buyForPri)s, %(buyFivNum)s,
                                 %(buyFivPri)s, %(selOneNum)s, %(selOnePri)s, %(selTwoNum)s, %(selTwoPri)s, %(selThrNum)s,
                                 %(selThrPri)s, %(selForNum)s, %(selForPri)s, %(selFivNum)s, %(selFivPri)s, %(date)s, %(time)s,
                                 %(noMean)s);'''
                    try:
                        cur_in.execute(sql,stock_info_key)
                        cur_in.close()
                        conn.commit()
                    except:
                        # 如果存在异常，进行回滚，同时继续读取插入下一条
                        conn.rollback()
                        continue
    finally:
        #建立完新表，将连接放回数据池。
        pool.putconn(conn)
    print('{'+name+'} 数据获取完成 !')
