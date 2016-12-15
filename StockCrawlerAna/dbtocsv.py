import psycopg2
# 注册字符串缺省类型为unicode
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import psycopg2.pool
import dtime
import csv
# 获取表名称
##day = dtime.get_now()['date']
##tb_pre = "stock_"
##tb_name = tb_pre+day.replace('-','_')
##### 2015_05_14
##test_tbname = tb_pre+"2015_05_18"


def writeDbCsv(tb_name,pool):
    conn = pool.getconn()
    sql = "select name from stock_tbname order by id desc limit 1;"
    cur = conn.cursor()
    cur.execute(sql)
    pre_tbname = cur.fetchone()[0]
    cur.close()
    # 将表名称插入数据表中
    insertTbName(tb_name,pool)
    # 将每条记录逐条写入数据库中
    try:
        with conn.cursor() as cur:
            with open(tb_name+'.csv','w',newline='') as csvfile:
                writer = csv.writer(csvfile,delimiter=',',quotechar='|', quoting = csv.QUOTE_MINIMAL)
                #设置间隔符为','
                sql = '''select b.*,c.* from stock_inf as a
                            left join ''' +pre_tbname+''' as b on a.no = b.no
                            left join '''+tb_name+''' as c on a.no = c.no
                            where a.remark = '1' and b.nomean = '00' and c.nomean = '00'
                        '''
##                sql = "select * from "+pre_tbname+" where nomean = '00';"
                cur.execute(sql)
                for row in cur:
##                    # print(type(row))-> tuple
##                    no = row[0]
##                    icur = conn.cursor()
##                    isql = "select * from "+tb_name+" where no ='"+no+"';"
##                    icur.execute(isql)
##                    row = row +icur.fetchone()
##                    icur.close()
                    writer.writerow(row)
                cur.close()
                # writer.writerows(cur)
                #打开CSV文件，并写入数据库读取的信息。
                        # for row in cur:
                        # 	writer.writerow(row)
    finally:
        # 将连接返回池子
        pool.putconn(conn)

def insertTbName(vtn,vpool):
    #定义sql语句
    iconn = vpool.getconn()
    try:
        with iconn.cursor() as cur:
            isql = "insert into stock_tbname(name) values(%s);"
            cur.execute(isql,(str(vtn),))			
            cur.close()
            iconn.commit()
    finally:
        vpool.putconn(iconn)


##dsn = "host=localhost dbname=dstock user=postgres password=postgres"
##pool = psycopg2.pool.ThreadedConnectionPool( minconn=2,maxconn=10, dsn=dsn)
##writeDbCsv("stock_2015_05_28",pool)

##select b.*,c.* from stock_inf as a
##left join stock_2015_05_27 as b on a.no = b.no
##left join stock_2015_05_28 as c on a.no = c.no
##where a.remark = '1' and b.nomean = '00' and c.nomean = '00'


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

# sql = '''SELECT tablename FROM   pg_tables 
# 		where tablename like 'stock%' 
# 		order by tablename desc limit '''+tb_i+''' offset 2;'''

