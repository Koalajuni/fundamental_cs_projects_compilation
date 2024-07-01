#데이터베이스에서 데이터 조회 

import pymysql

#데이터베이스 세팅
conn = pymysql.connect(
    host= '127.0.0.1',
    user='chat',
    password=,
    database=, 
    port = 3306,
    charset='utf8',
)

try:
    cursor = conn.cursor()
    sql ="""
        UPDATE chat 
        set human_chat = %s, 
            ai_chat = %s, 
        WHERE id = %s
    """
    val = [("다시 바꿈","답변을 이렇게 바꾸었다",1),
           ("또 바꿈","답변을 이렇게 바꾸었다",6)]
    cursor.executemany(sql,val)
    conn.commit()
    print("업데이트 완료")
except:
    print("업데이트 에러입니다.")

conn.close()
