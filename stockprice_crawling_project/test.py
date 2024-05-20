import FinanceDataReader as fdr
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import os
from PyQt5 import uic


form_main = uic.loadUiType("main.ui")[0]

class MyWindow(QMainWindow,form_main):
    def __init__(self):
        super().__init__()  #QMainWindow를 무조건 먼저 실행하는 코드 
        self.setupUi(self)
        self.searchBtn.clicked.connect(self.searchBtn_click)
        self.lbSearch.setPlaceholderText("Search Stock Name") 

    def searchBtn_click(self):
        name = self.lbSearch.text()
        try:
            df = fdr.DataReader(name)
            QMessageBox.about(self,"찾기",f"{name} 찾겠습니다")
            print(df.head())
        except:
            QMessageBox.about(self,"에러",f"{name} 잘못 된 이름입니다")



app = QApplication(sys.argv)
path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon.png')
app.setWindowIcon(QIcon(path))
windowMain = MyWindow()
windowMain.show() 
app.exec_()


# Finance Reader 
df = fdr.DataReader("090430")