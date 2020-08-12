
from PyQt5.QtWidgets import QFileDialog
import sys
from PyQt5.QtGui import QIcon
import subprocess
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop, QTimer
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QTextEdit
from PyQt5.QtGui import QTextCursor, QIntValidator
import os
s = []
p = []
f = open('./list.txt', mode='r')
global pix
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.setGeometry(250,40,900,690)
        MainWindow.setGeometry(0, 0, 1300, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 350, 300, 300))
        self.label1.setObjectName("匹配第一张")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(400, 350, 300, 300))
        self.label2.setObjectName("匹配第二张")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(800, 350, 300, 300))
        self.label3.setObjectName("匹配第三张")

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(450, 50, 300, 300))
        self.label4.setObjectName("原图")

        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(800, 50, 400, 400))
        self.label5.setObjectName("相似度")

        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(450, 50, 300, 300))
        self.label6.setObjectName("本地图片")

        self.label1.setScaledContents(True)  # 让图片自适应label大小
        self.label2.setScaledContents(True)  # 让图片自适应label大小
        self.label3.setScaledContents(True)  # 让图片自适应label大小
        self.label4.setScaledContents(True)  # 让图片自适应label大小
        self.label5.setScaledContents(True)  # 让图片自适应label


        # self.myButton = QtWidgets.QPushButton(self.centralwidget)
        # self.myButton.setObjectName("myButton")
        # self.myButton.setText("选择照片")
        # self.myButton.setGeometry(QtCore.QRect(20,20,60,50))


        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(590, 70, 75, 23))
        self.Button1.setObjectName("拍照")

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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "拍照检索"))
        # self.label1.setText(_translate("MainWindow", "输入下载图片名称："))
        # self.label_2.setText(_translate("MainWindow", "下载张数："))
        self.Button1.setText(_translate("MainWindow", "拍照"))
        #self.myButton.setText(_translate("MainWindow", "选择照片"))

    def control(self):
        self.Button1.clicked.connect(self.Button1_on_click)
        #self.myButton.clicked.connect(self.img)

    def Button1_on_click(self):
        str=("python query_online_gai.py")
        o = os.system(str)
        self.show()

    def show(self):
        for line in f:
            p.append(line[:-1])

        pix = QtGui.QPixmap(p[0])
        pix1 = QtGui.QPixmap(p[1])
        pix2 = QtGui.QPixmap(p[2])
        pix3 = QtGui.QPixmap("./datab/1.jpg")

        self.label1.setPixmap(pix)
        self.label2.setPixmap(pix1)
        self.label3.setPixmap(pix2)
        self.label4.setPixmap(pix3)

        file = open('./fs.txt')
        file_text = file.read()
        self.label5.setText(file_text)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()

    def img(self):
        imgName, imgType = QFileDialog.getOpenFileName(None, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName)
        self.label6.setPixmap(jpg)
        #c = ['python', 'query_online.py', '-query', imgName, '-index' ,'add_after.h5' ,'-result' ,'Download']
        c = ['python query_online.py -query', imgName, '-index add_after.h5 -result Download']
        str = ' '.join(c)
        print(str)
        p = os.system(str)
        for line in f:
            p.append(line[:-1])

        pix = QtGui.QPixmap(p[0])
        pix1 = QtGui.QPixmap(p[1])
        pix2 = QtGui.QPixmap(p[2])
        #pix3 = QtGui.QPixmap(imgName)

        self.label1.setPixmap(pix)
        self.label2.setPixmap(pix1)
        self.label3.setPixmap(pix2)
        #self.label4.setPixmap(pix3)

        file = open('./fs.txt')
        file_text = file.read()
        self.label5.setText(file_text)
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/ahh15.ico'))
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())