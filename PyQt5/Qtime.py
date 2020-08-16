from PyQt5 import QtCore, QtGui, QtWidgets


class Welcome(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window, self.MainWindow)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 700)
        MainWindow.move(0, 0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(10, 50, 250, 150))
        self.Button_1.setObjectName("Button")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 1000, 31))
        self.textEdit.setObjectName("textEdit")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(260, 50, 250, 150))
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(510, 50, 250, 150))
        self.Button_3.setObjectName("Button_3")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(10, 200, 250, 150))
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(260, 200, 250, 150))
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(510, 200, 250, 150))
        self.Button_6.setObjectName("Button_6")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(10, 350, 250, 150))
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(260, 350, 250, 150))
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(510, 350, 250, 150))
        self.Button_9.setObjectName("Button_9")
        self.Button_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_10.setGeometry(QtCore.QRect(760, 50, 250, 150))
        self.Button_10.setObjectName("Button_10")
        self.Button_11 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_11.setGeometry(QtCore.QRect(260, 500, 500, 150))
        self.Button_11.setObjectName("Button_11")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(10, 500, 250, 150))
        self.Button_0.setObjectName("Button_0")
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

#        self.capture = cv2.VideoCapture(0)
#        self.hand_hist=cal(self.capture)
#        self.timer = QtCore.QTimer(self.centralwidget)
#        self.timer.timeout.connect(self.update)
#        self.timer.start(42)

    def update(self):
        tracking(self.hand_hist, self.capture)

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

def Format():
    print("Traceback (most recent call last):\n  File \"Access.py\", line 20, in <module>\nProtectedCodeError: mismatched signature")
