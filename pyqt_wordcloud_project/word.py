import sys
from tkinter import dialog
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import uic
from collections import Counter
import numpy as np
import pandas as pd 
import seaborn as sns
import re
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud




path = "./search_file/"


############### 전처리 함수 #########################

# 전체 텍스트 특수문자 제거 
def clean_text(inputString):
    text_rmv = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’\'·]', ' ', inputString)
    return text_rmv


# 키워드와 비슷한 단어 정규 표준화로 제거    
def clean_key(inputString):
    text_rmv = re.sub('인공지능?', ' ', inputString)
    text_rmv = re.sub('[AI]', ' ', inputString)
    text_rmv = re.sub('챗GPT?', ' ', inputString)
    text_rmv = re.sub('Chat?', ' ', inputString)
    text_rmv = re.sub('GPT?', ' ', inputString)
    return text_rmv

#이 부분은 KoNLPy를 사용하면 더 정확한 값을 얻을 수 있기에 추후에 반영해보면 좋을 것 같다. 
# 한국어 특성상 1자 단어들은 주로 제거하는 특성이 있긴 함. ('에','의','을','수','가', 등등)ㅈ

#####################################################




############### 워드 클라우드 실행 함수 #########################
def wordCloudView(seperateList):
    file_list = os.listdir(path)
    fileList1 = [] 
    for file in file_list:
        if file in seperateList:
            fileList1.append(file)
    
    dfCSV = pd.DataFrame()

    for i in fileList1:
        data = pd.read_csv(path + i, encoding ='utf-8')
        dfCSV = pd.concat([dfCSV,data])

        dfCSV = dfCSV.reset_index(drop = True)

    dfCSV = dfCSV.drop(['링크'], axis = 'columns')

    listCsv = dfCSV['제목'].astype(str).tolist()

    oneWord = (' ').join(listCsv)

    oneWord = clean_text(oneWord)
    oneWord = clean_key(oneWord)

    stopList1 = ["인공지능","챗GPT","챗 GPT","챗", "어떻게", "질문","AI","인공지능이", "AI가","관련","이","의","학과","과"] 
    stopList2 = ["비트코인","코인","Bitcoin","암호화폐","가격","왜","의","학과","과","질문","거래소","업비트","관련"]
    wc1 = WordCloud(
    font_path = "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    stopwords = stopList2, 
    background_color = "white",
    width = 451, height = 271,
    random_state = 40)

    cloud = wc1.generate(oneWord)
    
    cloud.to_file("search_file/word.png")

#####################################################




wordMain = uic.loadUiType("ui/ui_wordcloud.ui")[0]

class WordWin(QDialog,wordMain):
    searchText = ''
    aiList = ['인공지능.csv', 'AI.csv','챗gpt.csv']
    btcList = ['코인.csv','비트코인.csv', '비트코인 가격.csv']

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnClose.clicked.connect(self.btn_close_click)
        self.btnWordCloud.clicked.connect(self.btnWordCloud_click)
    

    def btn_close_click(self):
        self.close()
    
    def btnWordCloud_click(self):
        wordCloudView(['코인.csv','비트코인.csv', '비트코인 가격.csv'])
        self.lbImage.setPixmap(QPixmap("./search_file/word.png"))
        QMessageBox.about(self,"워드클라우드 분석","워드클라우드 분석 완료")

        
    def showModal(self):
        return super().exec_()
