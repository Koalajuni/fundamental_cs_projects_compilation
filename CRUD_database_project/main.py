import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from memberInfo import MemberWin
from memberEdit import MemberWinEdit
from db_functions import * 


formMain = uic.loadUiType("ui/ui_main.ui")[0]

class MyWindow(QMainWindow,formMain):
    del_idx, edit_idx, edit_email, edit_names, edit_telnos, edit_addrs, edit_sns = '','','','','','','', 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_del.clicked.connect(self.btn_del_clicked)
        self.btn_edit.clicked.connect(self.btn_edit_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_exit.clicked.connect(self.btn_exit_clicked)
        self.btn_search_clicked()
        self.tble_members.cellClicked.connect(self.cellclicked_event)


    def cellclicked_event(self,row,col):
        self.del_idx        = self.tble_members.item(row,0).text()
        self.edit_idx       = self.tble_members.item(row,0).text()
        self.edit_email     = self.tble_members.item(row,1).text()  
        self.edit_names     = self.tble_members.item(row,2).text() 
        self.edit_telnos    = self.tble_members.item(row,3).text() 
        self.edit_addrs     = self.tble_members.item(row,4).text() 
        self.edit_sns       = self.tble_members.item(row,5).text() 

    def btn_add_clicked(self):
        memberWin = MemberWin()
        memberWin.showModal()
        self.btn_search_clicked()  #회원가입 페이지 클로즈 되면 업데이트 (update, repaint)
    
    def btn_del_clicked(self):
        if self.del_idx == '':
            QMessageBox.about(self,"삭제 에러", "선택된 항목이 없습니다")
            return 
        if memberDelete(self.del_idx) == True:
            QMessageBox.about(self,"삭제 완료", "데이터를 삭제했습니다")
        else:
            QMessageBox.about(self,"삭제 실패","삭제를 실패했습니다")
        self.btn_search_clicked() 
        self.del_idx = ''
    
    def btn_edit_clicked(self):
        memberWinEdit = MemberWinEdit()
        memberWinEdit.loadData(self.edit_idx, self.edit_email, self.edit_names, 
                               self.edit_telnos, self.edit_addrs, self.edit_sns)
        memberWinEdit.showModal()
        self.btn_search_clicked()

    def btn_search_clicked(self):
        table = self.tble_members
        dataset = memberInfoLoad(self.le_search.text())
        table.setRowCount(len(dataset))
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(['id','이메일','이름','전화번호','주소','SNS'])
        for i, (idx,email,name,telnos,addrs,sns) in enumerate(dataset):
            table.setItem(i,0,QTableWidgetItem(str(idx)))
            table.setItem(i,1,QTableWidgetItem(email))
            table.setItem(i,2,QTableWidgetItem(name))
            table.setItem(i,3,QTableWidgetItem(telnos))
            table.setItem(i,4,QTableWidgetItem(addrs))
            table.setItem(i,5,QTableWidgetItem(sns))

    def btn_exit_clicked(self):
        exit()


app = QApplication(sys.argv)
path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'assets/icon.png')
app.setWindowIcon(QIcon(path))
windowMain = MyWindow()
windowMain.show()
app.exec()