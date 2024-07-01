#데이터베이스에서 데이터 추가 

import pymysql
from datetime import datetime
import requests


def ChatGPTadd(human_chat,ai_chat):
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
        #오늘 날짜
        currentTime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        #아이피 주소 확인 
        userIP = requests.get('http://ip.jsontest.com').json()['ip']

        cursor = conn.cursor()
        sql = "INSERT INTO chat (human_chat,ai_chat,dates,ips) VALUES (%s,%s,%s,%s)"
        val = (human_chat,ai_chat,currentTime, userIP)
        cursor.execute(sql,val)
        conn.commit()
        print('데이터 입력 완료')
    except:
        print('입력 실패')

    conn.close()
