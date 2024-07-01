import sys
from tkinter import dialog
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import uic
from search_naver import *
import random 

searchMain = uic.loadUiType("ui/ui_crawling.ui")[0]

class SearchWin(QDialog,searchMain):

    searchText = ''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnClose.clicked.connect(self.btn_close_click)
        self.btnSearch.clicked.connect(self.btn_search_click)
        self.btnSave.clicked.connect(self.btn_save_click)
    

    def btn_close_click(self):
        self.close()
    
    def btn_search_click(self):
        if self.leSearch.text() == '':
            QMessageBox.about(self,"Error search","입력값이 존재하지 않습니다")
            return  #좋은 프로그램,, 여기서 끝내야 혹여나 뒤에 코드가 있더라도 종료된다.

        naverClear()  #전에 있던 값을 지워준다 
        self.searchText = self.leSearch.text()
        
        for i in range(100):
            page = i + 1
            sList = naverKin(self.searchText,page)
            print('#'*20 + ' ' + str(page) + ' ' +'#'*20)

            model = QStandardItemModel()
            for data in sList:
                model.appendRow(QStandardItem(data[0]))
            self.lvSearch.setModel(model)

            time.sleep(random.uniform(1.1, 2.3)) #정말 많이 crawling하면, random 함수를 돌려서 제한이 안되게끔
        QMessageBox.about(self,"Crawling Success","크롤링 완료했습니다")
        # naverKin(searchText,3)

    def btn_save_click(self):
        if self.searchText == '':
            QMessageBox.about(self,"Error search","검색어를 입력해 주세요")
            return

        saveKin(f"search_file/{self.searchText}")
        
    
    def showModal(self):
        return super().exec_()

