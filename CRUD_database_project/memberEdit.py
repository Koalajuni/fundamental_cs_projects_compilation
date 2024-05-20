import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from datetime import datetime
from db_functions import * 

memberEditMain = uic.loadUiType("ui/ui_memberEdit.ui")[0]


class MemberWinEdit(QDialog,memberEditMain):
    edit_idx = ''
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_edit.clicked.connect(self.btn_edit_clicked)
        self.btn_exit.clicked.connect(self.btn_exit_clicked)

    def loadData(self,idx,mails,names, telnos, addrs, sns):
        self.edit_idx = idx
        self.le_email.setText(mails)
        self.le_name.setText(names) 
        self.le_telnos.setText(telnos) 
        self.le_addrs.setText(addrs)
        self.le_sns.setText(sns)   
        #main에서 데이터를 받아서 로드 데이터 함수로 변수를 설정해주는 코드 
    
    def btn_exit_clicked(self):
        self.close()


    def btn_edit_clicked(self):

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
            memberInfoEdit(self.edit_idx, names, mails,addrs,telnos,sns)
            QMessageBox.about(self, "Success Save", "모두 저장했습니다!")
            #database에 추가
            self.close()



    def showModal(self):
        return super().exec_()
    
