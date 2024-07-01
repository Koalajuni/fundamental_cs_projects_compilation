import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import os
from PyQt5 import uic
from search import SearchWin
from word import WordWin

form_main = uic.loadUiType("ui/ui_main.ui")[0]

class MyWindow(QMainWindow,form_main):
    def __init__(self):
        super().__init__()  #QMainWindow를 무조건 먼저 실행하는 코드 
        self.setupUi(self)
        self.btn_close.clicked.connect(self.btn_close_click)
        self.btn_search.clicked.connect(self.btn_search_click)
        self.btn_wordcloud.clicked.connect(self.btn_wordcloud_click)


    def btn_close_click(self):
        exit()
    
    def btn_search_click(self):
        searchWin = SearchWin()
        searchWin.showModal()
        # QMessageBox.about(self,"검색","네이버를 검색하겠습니다")
    
    def btn_wordcloud_click(self):
        wordWin = WordWin()
        wordWin.showModal()
    




app = QApplication(sys.argv)
path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'assets/icon.png')
app.setWindowIcon(QIcon(path))
windowMain = MyWindow()
windowMain.show() 
app.exec_()
