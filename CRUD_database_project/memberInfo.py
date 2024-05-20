import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from datetime import datetime
from db_functions import * 

memberMain = uic.loadUiType("ui/ui_memberInfo.ui")[0]


class MemberWin(QDialog,memberMain):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_exit.clicked.connect(self.btn_exit_clicked)


    
    def btn_exit_clicked(self):
        self.close()


    def btn_save_clicked(self):

        checkInfoList = [('이름',self.le_name),
                         ('이메일',self.le_email),
                         ('전화번호',self.le_telnos),
                         ]
        state = True 
        for name,val in checkInfoList:
            if val.text() == "":
                state = False
        
        if state == False:
            QMessageBox.about(self, "Error Save", f"'{name}'을 입력하지 않았습니다")
            return
        else: 
            names = self.le_name.text()
            mails = self.le_email.text()
            telnos = self.le_telnos.text()
            addrs = self.le_addrs.text()
            sns = self.le_sns.text()
            memberInfoAdd(names, mails,addrs,telnos,sns)
            QMessageBox.about(self, "Success Save", "모두 저장했습니다!")
            #database에 추가
            self.close()



    def showModal(self):
        return super().exec_()
    
