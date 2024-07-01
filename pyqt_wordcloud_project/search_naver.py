#################################################
# 네이버 지식인 자동 크롤링 프로그램 
# 일자: 2024년 5월 7일 
# lib: requests, beautifulsoup4, selenium
#################################################


#라이브러리 사용
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus #한국어를 영문 변환으로 
import csv 
import selenium 
import requests as req
import codecs
import time 

#CSV로 저장할 배열 
searchList = []

def naverClear():
    global searchList
    searchList = [] 

def naverKin(search,pageNum):
    #입력창
    # search = input("지식인 검색어를 입력하세요:")
    # search = "인공지능"
    #Url에서 정보 가져오기 
    url = f"https://kin.naver.com/search/list.naver?query={quote_plus(search)}&page={pageNum}"


    #인터넷에서 정보 가져오기 
    # html = urlopen(url).read()  #url 정보 가져오기 
    html = req.get(url)  #request을 쓰는 이유는 response을 통해서 에러 처리 할 수 있도록 

    if html.status_code == 200:
        htmlcode = html.text
        
        soup = bs(htmlcode,'html.parser') #html을 사용하겠다 선언 

        #<class basic1> 찾는 과정 
        ul = soup.select_one('ul.basic1')
        titles = ul.select('li>dl>dt>a')  #List 값 구조가 비슷하기 때문에 tag를 파고 들어감 

        #데이터 값 가져오기 
        for title in titles:
            titleText = title.text
            titleLink = title.attrs['href']
            searchList.append([titleText,titleLink])

    return searchList 
    
#파일로 저장  
def saveKin(search):
    f  = codecs.open(f'{search}.csv','w', encoding = 'utf-8')
    csvWriter = csv.writer(f)

    csvWriter.writerow(['제목','링크'])

    for data in searchList:
        csvWriter.writerow(data)

    f.close()

#################################################
#함수 테스트
#################################################
''' 
search = "인공지능"
for i in range(10):
    page = i + 1
    naverKin(search,page)
    print('#'*20 + ' ' + str(page) + ' ' +'#'*20)
    time.sleep(1.5)

'''