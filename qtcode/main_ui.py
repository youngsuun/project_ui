# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\PycharmProjects\pythonProject\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 753)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/로고_아이콘.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 620, 331, 51))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.maintxt_4 = QtWidgets.QLabel(Form)
        self.maintxt_4.setGeometry(QtCore.QRect(70, 450, 251, 16))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        font.setPointSize(8)
        self.maintxt_4.setFont(font)
        self.maintxt_4.setObjectName("maintxt_4")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(150, 170, 101, 91))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/background/로고_연한거 (1).png"))
        self.logo.setObjectName("logo")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(40, 560, 331, 51))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(10)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_1.setAutoFillBackground(False)
        self.pushButton_1.setAutoDefault(False)
        self.pushButton_1.setDefault(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.maintxt_1 = QtWidgets.QLabel(Form)
        self.maintxt_1.setGeometry(QtCore.QRect(50, 370, 291, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        self.maintxt_1.setFont(font)
        self.maintxt_1.setObjectName("maintxt_1")
        self.maintxt_2 = QtWidgets.QLabel(Form)
        self.maintxt_2.setGeometry(QtCore.QRect(70, 410, 251, 21))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        font.setPointSize(8)
        self.maintxt_2.setFont(font)
        self.maintxt_2.setObjectName("maintxt_2")
        self.bg_2 = QtWidgets.QLabel(Form)
        self.bg_2.setGeometry(QtCore.QRect(40, -20, 411, 611))
        self.bg_2.setText("")
        self.bg_2.setPixmap(QtGui.QPixmap(":/background/bg.png"))
        self.bg_2.setObjectName("bg_2")
        self.bg_1 = QtWidgets.QLabel(Form)
        self.bg_1.setGeometry(QtCore.QRect(0, 0, 501, 611))
        self.bg_1.setText("")
        self.bg_1.setPixmap(QtGui.QPixmap(":/background/bg-Light Gray.png"))
        self.bg_1.setObjectName("bg_1")
        self.maintxt_3 = QtWidgets.QLabel(Form)
        self.maintxt_3.setGeometry(QtCore.QRect(70, 430, 251, 21))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        font.setPointSize(8)
        self.maintxt_3.setFont(font)
        self.maintxt_3.setObjectName("maintxt_3")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 680, 331, 51))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.bg_3 = QtWidgets.QLabel(Form)
        self.bg_3.setGeometry(QtCore.QRect(80, 50, 241, 331))
        self.bg_3.setText("")
        self.bg_3.setPixmap(QtGui.QPixmap(":/background/bg_2.png"))
        self.bg_3.setObjectName("bg_3")
        self.bg_1.raise_()
        self.pushButton_2.raise_()
        self.pushButton_1.raise_()
        self.bg_2.raise_()
        self.pushButton_3.raise_()
        self.bg_3.raise_()
        self.logo.raise_()
        self.maintxt_1.raise_()
        self.maintxt_2.raise_()
        self.maintxt_3.raise_()
        self.maintxt_4.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "당신 곁의 잔여백신_백발백신"))
        self.pushButton_2.setText(_translate("Form", "데이터 수집하기"))
        self.maintxt_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">확인해보세요</p></body></html>"))
        self.pushButton_1.setText(_translate("Form", "사용 전 필독 사항"))
        self.maintxt_1.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">우리동네 잔여백신 발생 현황</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.maintxt_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">데이터 수집을 통해</p><p align=\"center\"><br/></p></body></html>"))
        self.maintxt_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">신청 성공 확률이 높은 병원과 시간대를</p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "수집 결과 확인 "))
import testResource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
