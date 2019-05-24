import pymysql


conn =pymysql.Connect(host='127.0.0.1',user='root',password='961109',db='bbs',port=3306,charset='utf8')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql ='select username,usertype,password,regtime,email from user'

res=cursor.execute(sql)
# print(res,type(res))
#
if res:
    # print("用户名   用户类型    密码  注册时间    email")
    # for i in range(res):
    # str=''
    li=['用户名','用户类型','密码','注册时间','email']
    print('{:^4}''{:^4}''{:^30}''{:^45}''{:^1}'.format(*li))
    record = cursor.fetchall()
    for dict in record:
        for key in dict:
            print(dict[key],end='\t')
        print()
        # print("username:{:^5},usertype:{:^5},password:{:^5},regtime:{:^5},email:{:^5}".format(**dict))
        # str1=str.format(**dict)
        # print(str1)
        # for key in dict:
        #     print(dict[key], end='\t')
        # # print()

        # print(records)
    # for key in records:
    #
    #     print(records[key])
        # for key in records:
            # str += records[key]
            # print(str)

cursor.close()
conn.close()