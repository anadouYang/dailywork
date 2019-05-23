import pymysql
import hashlib
import datetime

conn =pymysql.Connect(host='127.0.0.1',user='root',password='961109',db='bbs',port=3306,charset='utf8')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# inusername=input("请输入姓名：")
# sql="select username from user where username='%s'"%inusername
#
# res=cursor.execute(sql)
while 1:
    inusername=input("请输入姓名：")
    sql="select username from user where username='%s'"%inusername
    res=cursor.execute(sql)
    if not res and len(inusername.strip())>2:

        password = input("请输入密码：")
        password = hashlib.sha1(password.encode('utf8')).hexdigest()
        print(password)
        usertype = input("输入用户类型，0普通，1 管理员：")
        email = input("请输入邮箱：")
        sql1="insert into user(username,usertype,password,regtime,email) values ('%s','%s',sha1('%s'),'%s','%s')"%(inusername,usertype,password,datetime.datetime.now(),email)
        cursor.execute(sql1)
        conn.commit()
        break
        # cursor.close(sql1)
        # conn.close(sql1)
    else:
        print("有误")
cursor.close()
conn.close()
#
# if len(username.strip())>2 and (username not in namelist):
#     namelist.append(username)
#     break
# password = input("请输入密码：")
# password = hashlib.sha1(password.encode('utf8')).hexdigest()
# usertype = input("输入用户类型，0普通，1 管理员：")
# email = input("请输入邮箱：")
#
# sql="insert into user(username,usertype,password,regtime,email) values ()"
