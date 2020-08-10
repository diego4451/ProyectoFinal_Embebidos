# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIN.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#pyuic5 -x PIN.ui -o PIN.py

import sys
import pyautogui as gui
from PyQt5 import QtCore, QtGui, QtWidgets
from Access import Ui_MainWindow

class Welcome(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window, self.MainWindow)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        width, height = gui.size()
        winW = 500
        winH = 500
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(winW, winH)
        MainWindow.move((width-winW)//2, (height-winH)//2)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, winW, winH))
        self.label.setPixmap(QtGui.QPixmap("Images/Green.png"))
        self.label.setScaledContents(True)

        winW = winW//2 - 90
        winH = winH//2 - 110
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(winW+20, winH+70, 41, 41))
        self.Button_1.setObjectName("Button")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(winW+20, winH+40, 161, 31))
        self.textEdit.setObjectName("textEdit")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(winW+60, winH+70, 41, 41))
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(winW+100, winH+70, 41, 41))
        self.Button_3.setObjectName("Button_3")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(winW+20, winH+110, 41, 41))
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(winW+60, winH+110, 41, 41))
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(winW+100, winH+110, 41, 41))
        self.Button_6.setObjectName("Button_6")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(winW+20, winH+150, 41, 41))
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(winW+60, winH+150, 41, 41))
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(winW+100, winH+150, 41, 41))
        self.Button_9.setObjectName("Button_9")
        self.Button_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_10.setGeometry(QtCore.QRect(winW+140, winH+70, 41, 41))
        self.Button_10.setObjectName("Button_10")
        self.Button_11 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_11.setGeometry(QtCore.QRect(winW+60, winH+190, 81, 41))
        self.Button_11.setObjectName("Button_11")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(winW+20, winH+190, 41, 41))
        self.Button_0.setObjectName("Button_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 207, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.string = ""
        self.MainWindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Awesome Window"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter Pin here</p></body></html>"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_1.clicked.connect(lambda: self.Click(1))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_2.clicked.connect(lambda: self.Click(2))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_3.clicked.connect(lambda: self.Click(3))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_4.clicked.connect(lambda: self.Click(4))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_5.clicked.connect(lambda: self.Click(5))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_6.clicked.connect(lambda: self.Click(6))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_7.clicked.connect(lambda: self.Click(7))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_8.clicked.connect(lambda: self.Click(8))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_9.clicked.connect(lambda: self.Click(9))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_0.clicked.connect(lambda: self.Click(0))
        self.Button_10.setText(_translate("MainWindow", "←"))
        self.Button_10.clicked.connect(self.Backspace)
        self.Button_11.setText(_translate("MainWindow", "Enter"))
        self.Button_11.clicked.connect(self.Enter)

    def Click(self, x):
        self.string += str(x)
        self.textEdit.setPlainText(self.string)

    def Backspace(self):
        self.string = self.string[0:-1]
        self.textEdit.setPlainText(self.string)

    def Enter(self):
        self.string  = "Enter PIN here"
        self.textEdit.setPlainText(self.string)
        self.openWindow()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Welcome()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
