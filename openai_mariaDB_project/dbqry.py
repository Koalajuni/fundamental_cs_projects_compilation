#데이터베이스에서 데이터 조회 

import pymysql

#데이터베이스 세팅
conn = pymysql.connect(
    host= '127.0.0.1',
    user='chat',
    password='@1234@',
    database='chatdb', 
    port = 3306,
    charset='utf8',
)

try:
    cursor = conn.cursor()
    sql = "select * from chat"
    cursor.execute(sql)
    rst = cursor.fetchall()
    for data in rst:
        print(data)

except:
    print("조회 에러입니다.")

conn.close()