# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5.QtGui import QIcon
import sys
import subprocess
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QTextEdit
from PyQt5.QtGui import QTextCursor, QIntValidator
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(250,40,900,690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(80, 70, 111, 16))
        self.label1.setObjectName("label1_name")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit_name")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 70, 54, 12))
        self.label_2.setObjectName("label2_name")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 100, 700, 500))
        self.label_3.setObjectName("label3_text")



        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)

        intValidator = QIntValidator(self.lineEdit2)
        intValidator.setRange(1, 99999)
        self.lineEdit2.setValidator(intValidator)
        self.lineEdit2.setGeometry(QtCore.QRect(450, 65, 61, 21))
        self.lineEdit2.setObjectName("lineEdit_num")
        self.myButton = QtWidgets.QPushButton(self.centralwidget)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("打开文件夹")
        self.myButton.setGeometry(QtCore.QRect(590, 100, 75, 23))
        self.myButton.clicked.connect(self.msg)

        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(590, 70, 75, 23))
        self.Button1.setObjectName("Button1")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.control()

    def msg(self):

        def startfile(filename):
            try:
                os.startfile(filename)
            except:
                subprocess.Popen(['xdg-open', filename])
        start_directory = r'E:\PycharmProjects\doutula\ImageSearchingEngine_gai\add_photo'
        startfile(start_directory)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "下载"))
        self.label1.setText(_translate("MainWindow", "输入下载图片名称："))
        self.label_2.setText(_translate("MainWindow", "下载张数："))
        self.Button1.setText(_translate("MainWindow", "确认下载"))

    def control(self):
        self.Button1.clicked.connect(self.Button1_on_click)

    def Button1_on_click(self):
        PhotoName = self.lineEdit.text()
        PhotoNum = self.lineEdit2.text()
        c = ['python', 'downphoto.py', PhotoName, PhotoNum]
        str=' '.join(c)
        p = os.system(str)

        file = open('./downpic.txt')
        file_text = file.read()
        self.label_3.setText(file_text)
        print(p)  # 打印执行结果 0表示 success ， 1表示 fail
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        #print('下载完成')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/aw9.ico'))
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())