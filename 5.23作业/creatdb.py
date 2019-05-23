import pymysql

conn =pymysql.Connect(host='127.0.0.1',user='root',password='961109',db='homework',port=3306,charset='utf8')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql="create database bbs default charset=utf8;"
cursor.execute(sql)

cursor.close()
conn.close()