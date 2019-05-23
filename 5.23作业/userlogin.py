import pymysql
import hashlib

conn =pymysql.Connect(host='127.0.0.1',user='root',password='961109',db='bbs',port=3306,charset='utf8')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


while 1:
    intusername = input("请输入用户名：")
    intpassword = input("请输入密码：")
    intpassword = hashlib.sha1(intpassword.encode('utf8')).hexdigest()
    # print(intpassword)
    sql = "select username,password from user where username='%s' and password=sha1('%s')" % (intusername,intpassword)
    res = cursor.execute(sql)

    if res:
        print("登陆成功")
        break
    else:
        print("登陆失败，请重新登陆")

cursor.close()
conn.close()

