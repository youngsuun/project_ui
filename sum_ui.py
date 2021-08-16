import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_ui.ui", self)
        self.pushButton_1.clicked.connect(self.openM_Button_1)

    def openM_Button_1(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class M_Button_1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/로고_아이콘.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 310, 281, 71))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(90, 230, 31, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setText("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.txt_1 = QtWidgets.QLabel(Dialog)
        self.txt_1.setGeometry(QtCore.QRect(60, 110, 311, 101))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_1.setFont(font)
        self.txt_1.setObjectName("txt_1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 220, 231, 61))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "사용 전 필독사항"))
        self.pushButton.setText(_translate("Dialog", "설치 완료 !"))
        self.txt_1.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">프로그램 실행을 위해 </p><p align=\"center\">Chrome Driver 설치가 필요합니다.</p></body></html>"))
        self.label.setText('<a href="https://beaded-jaborosa-fdf.notion.site/Chrome-Driver-3e707acbdea44cd28af991708097e938">Chrome Driver 설치 가이드</a>')
        self.label.setOpenExternalLinks(True)
import testResource_rc


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()

    #레이아웃 인스턴스 생성
    mainWindow = MainWindow()
    Button1Window = M_Button_1()

    #Widget 추가
    widget.addWidget(mainWindow)
    widget.addWidget(Button1Window)

    #프로그램 화면을 보여주는 코드
    widget.setFixedHeight(275)
    widget.setFixedWidth(390)
    widget.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()