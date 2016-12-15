import psycopg2
# 注册字符串缺省类型为unicode
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import psycopg2.pool
import dstockinfo
# 获取股票信息列表，包括编码，名称
stocks = dstockinfo.getCsv()
# 定义数据库连接配置项，并定义连接池的最少数量和最大数量
dsn = "host=localhost dbname=dstock user=postgres password=postgres"
pool = psycopg2.pool.ThreadedConnectionPool(minconn=2, maxconn=10, dsn=dsn)
# 将每条记录逐条写入数据库中
for stocks_unit in stocks:
    conn = pool.getconn()
    try:
    	with conn.cursor() as cur:
	               sql = "insert into stock_inf (no,name,remark) values (%(no)s,%(name)s,%(remark)s);"
	               cur.execute(sql,stocks_unit)
	               conn.commit()
    finally:
         # 将连接返回池子
         pool.putconn(conn)


#cur.execute('''
#INSERT INTO test_tbl1 (sn, name) VALUES (%(sn)s, %(name)s)
#''', {'sn':sn, 'name':name} )
#sql = '''
#		SELECT s.name, c.name, g.grade 
#	    FROM course_grade as g
#	        LEFT OUTER JOIN student as s ON g.stu_sn = s.sn
#	        LEFT OUTER JOIN course as c  ON g.cou_sn = c.sn ;
#		'''
#		cur.execute(sql)
#		for row in cur:
#			print '%s, %s, %f' % (row[0], row[1], row[2])
