DROP DATABASE IF EXISTS dstock;

DROP ROLE IF EXISTS admin; 

-- CREATE ROLE admin LOGIN
--   ENCRYPTED PASSWORD 'md545be9a63258b20d15415f90d1162a696' -- password: hh   
--   NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE;
CREATE USER admin WITH PASSWORD 'hh';

CREATE DATABASE dstock WITH OWNER = admin ENCODING = 'UTF8';


DROP TABLE IF EXISTS stock_inf;
CREATE SEQUENCE stock_inf_id_seq ;
CREATE TABLE IF NOT EXISTS stock_inf  (
  	  id 		Integer DEFAULT nextval('stock_inf_id_seq') PRIMARY KEY, 	--ID
	  no 		VARCHAR(10),		--编码
	  name 		TEXT, 				--名称
	  info 		TEXT,				--信息
	  remark 	TEXT				--关键词

);


-- -- 给id创建一个自增序号
-- CREATE SEQUENCE seq_stock_inf_id 
--     START 1 INCREMENT 1 OWNED BY stock_inf.id;
-- ALTER TABLE stock_inf ALTER id 
--     SET DEFAULT nextval('seq_stock_inf_id');
-- ID唯一
 CREATE UNIQUE INDEX idx_stock_inf_no ON stock_inf(no);

--------------------------
CREATE SEQUENCE stock_id_seq ;

-- stock_realtime_templete
DROP TABLE IF EXISTS stock_time_templete;
CREATE TABLE IF NOT EXISTS stock_time_templete  (
    ID 				Integer DEFAULT nextval('stock_id_seq') PRIMARY KEY,     -- ID
    no 				VARCHAR(10), -- 编码外键
    todStarPri 		VARCHAR(20),     -- 当天开盘价
    yesEndPri		VARCHAR(20),	--昨天收盘价
    nowPri 			VARCHAR(20),	--当前价格
    todMaxPri		VARCHAR(20),	--最高价
	todMinPri		VARCHAR(20),	--最低价
	nowBuyPri		VARCHAR(20),	--当前买价
	nowSelPri		VARCHAR(20),	--当前卖价
	dealNum			VARCHAR(20),	--成交量
	dealMoney		VARCHAR(20),	--成交金额
	buyOneNum		VARCHAR(20),	--买一量
	buyOnePri		VARCHAR(20),	--买一价
	buyTwoNum		VARCHAR(20),	--买二量
	buyTwoPri		VARCHAR(20),	--买二价
	buyThrNum		VARCHAR(20),	--买三量
	buyThrPri		VARCHAR(20),	--买三价
	buyForNum		VARCHAR(20),	--买四量
	buyForPri		VARCHAR(20),	--买四价
	buyFivNum		VARCHAR(20),	--买五量
	buyFivPri		VARCHAR(20),	--买五价
	selOneNum		VARCHAR(20),	--卖一量
	selOnePri		VARCHAR(20),	--卖一价
	selTwoNum		VARCHAR(20),	--卖二量
	selTwoPri		VARCHAR(20),	--卖二价
	selThrNum		VARCHAR(20),	--卖三量
	selThrPri		VARCHAR(20),	--卖三价
	selForNum		VARCHAR(20),	--卖四量
	selForPri		VARCHAR(20),	--卖四价
	selFivNum		VARCHAR(20),	--卖五量
	selFivPri		VARCHAR(20),	--卖五价
	date 			date,		--当前日期
	time			time,		--当前时间
	noMean			TEXT		--备注
);

ALTER TABLE stock_time_templete 
    ADD CONSTRAINT stock_time_templete_fk FOREIGN KEY (no) REFERENCES stock_inf(no);


--{'buyForNum': '2700', 'selThrPri': '18.92', 'dealMoney': '690096983.14', 'todMaxPri': '19.15', 'selThrNum': '201500', 'nowSelPri': '18.90', 'buyTwoNum': '22600', 'todStarPri': '18.62', 'buyOneNum': '7200', 'nowBuyPri': '18.89', 'buyForPri': '18.86', 'buyFivNum': '8100', 'buyFivPri': '18.85', 'noMean': '00', 'yesEndPri': '18.44', 'selOneNum': '56116', 'time': '15:05:57', 'selForNum': '5600', 'buyThrNum': '3400', 'todMinPri': '18.40', 'selForPri': '18.93', 'buyOnePri': '18.89', 'selTwoPri': '18.91', 'selTwoNum': '41200', 'nowPri': '18.90', 'date': '2015-04-30', 'buyTwoPri': '18.88', 'selFivPri': '18.94', 'selFivNum': '8100', 'name': '天音控股', 'buyThrPri': '18.87', 'dealNum': '36554372', 'selOnePri': '18.90'}



DROP TABLE IF EXISTS stock_tbname;
CREATE SEQUENCE stock_tbname_id_seq ;
CREATE TABLE IF NOT EXISTS stock_tbname  (
  	  id 		Integer DEFAULT nextval('stock_tbname_id_seq') PRIMARY KEY, 	--ID
	  name 		TEXT				--名称

);