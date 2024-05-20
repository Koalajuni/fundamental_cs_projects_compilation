
#파일 저장하기 
# save_file = open('save.txt', 'w',encoding='utf8')
# print('test1: test', file = save_file)  # or save_file.write("test1: test" \n)
# print('test1: test2', file = save_file)
# save_file.close()


#불러오기: 
# fileLoad = open('save.txt','r',encoding='utf8')

# lines = fileLoad.readline()

# while True:
#     line = fileLoad.readline()

#     if not line:
#         break 

#     print(line,end = '')

# fileLoad.close()

from json import load
import pickle 

# pFile = open('pFile.pickle','wb')

# saveData = {
#     "name": "홍길동",
#     "age":35,
#     "lang": "Python"
# }

# pickle.dump(saveData,pFile)

# pFile.close()


# loadFile = open('pFile.pickle','rb')
# memData = pickle.load(loadFile)
# print(memData)

# loadFile.close()
# try: 
#     x  = input("숫자를 입력하세요:")
#     y = 10 / int(x)
#     print(y)

# except:
#     print("숫자는 0으로 나눌 수 없습니다")


class Cafe:
    def __init__(self,name, menu):
        self.menu = menu 
        self.cafeName = name

    def ordering(self, cupSize):
        self.cupSize = cupSize
        print(f"카페명: {self.cafeName}, 주문:{self.menu}, 크기: {self.cupSize}")

cafeList = ["Starbucks","Twosome","Ediya"]
menuList = ['카페라떼','아메리카노','바닐라라떼']
sizeList = ["톨","레굴러","빅"]

for i in range(len(cafeList)):
    cafeList[i]  = Cafe(cafeList[i] ,menuList[i])
    cafeList[i].ordering(sizeList[i])

#####
# python translation scraping: 
#  1. Scrape text from google sheets 
#  2. Load text to open API 
#  3. get result to word document (Done)
#####