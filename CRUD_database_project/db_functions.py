from PyQt5 import uic
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import requests 
import pymysql
from datetime import datetime


########### 데이터베이스 추가 함수 #############

def memberInfoAdd(names, mails,addrs,telnos,sns):
    conn = pymysql.connect(
        host= '127.0.0.1',
        user='newMember',
        password='@1234@',
        database='memberdb', 
        port = 3306,
        charset='utf8',
    )
    # try:
    #오늘 날짜
    currentTime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    #아이피 주소 확인 
    userIP = requests.get('http://ip.jsontest.com').json()['ip']

    cursor = conn.cursor()
    sql = "INSERT INTO members (mails,names,telnos,addrs,sns,ips,date_created) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (mails,names,telnos,addrs,sns,userIP,currentTime)
    cursor.execute(sql,val)
    conn.commit()
    print('데이터 입력 완료')

    conn.close()
    # except:
    #     print("데이터베이스 추가 오류")


######## 데이터베이스 불러오기 함수 ##########

def memberInfoLoad(qry):
    conn = pymysql.connect(
        host= '127.0.0.1',
        user='newMember',
        password='@1234@',
        database='memberdb', 
        port = 3306,
        charset='utf8',
    )
    try:
        cursor = conn.cursor()
        dataset = ''
        if qry == "":
            sql = "SELECT id,mails,names,telnos,addrs,sns FROM members"
        else:
            sql = f"""
            SELECT id,mails,names,telnos,addrs,sns FROM members 
            WHERE 
            (mails like '%{qry}%' or
            names like '%{qry}%' or
            telnos like '%{qry}%' or 
            addrs like '%{qry}%' or 
            sns like '%{qry}%')
            """
        cursor.execute(sql)
        dataset = cursor.fetchall()
        conn.commit()
        print('데이터 조회 완료')
    except:
        print("데이터베이스 불러오기 오류")
        conn.close()
    finally:
        conn.close()
        return dataset
    


######## 데이터베이스 제거 함수 ##########

def memberDelete(idx):

    if idx == '':
        return False
    #실제 프로젝트에서 삭제 전에 데이터베이스에 있는지 확인 필요
    conn = pymysql.connect(
        host= '127.0.0.1',
        user='newMember',
        password='@1234@',
        database='memberdb', 
        port = 3306,
        charset='utf8',
    )
    try:
        cursor = conn.cursor()
        sql = f"DELETE FROM members WHERE id='{idx}'"
        cursor.execute(sql)
        conn.commit()
        print('데이터 제거 완료')
    except:
        conn.close()
        print("데이터베이스 제거 오류")
        return False
    finally:
        conn.close()
        return True
    

    ######## 데이터베이스 제거 함수 ##########

def memberInfoEdit(idx,mails,names,telnos,addrs,sns):

    conn = pymysql.connect(
        host= '127.0.0.1',
        user='newMember',
        password='@1234@',
        database='memberdb', 
        port = 3306,
        charset='utf8',
    )
    # try:
    cursor = conn.cursor()
    sql = """
        UPDATE members 
        set mails = %s,
            names = %s,
            telnos = %s,
            addrs = %s,
            sns = %s
        WHERE id = %s
    """
    val = (mails,names,telnos,addrs,sns,idx)
    cursor.execute(sql,val)
    conn.commit()
    print('데이터 수정 완료')
    # except:
    #     print("데이터베이스 수정 오류")
    #     return False
    # finally:
    #     conn.close()
    #     return True