import pymysql

conn =pymysql.Connect(host='127.0.0.1',user='root',password='961109',db='bbs',port=3306,charset='utf8')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql1 = "create table if not exists user(uid int primary key auto_increment,username varchar(30) unique,usertype enum('0','1') default '0',password varchar(48),regtime datetime,email varchar(30))"

cursor.execute(sql1)
cursor.close()
conn.close()