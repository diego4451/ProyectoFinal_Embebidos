import sys
import mouse
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.Qt import Qt
from PyQt5 import QtWidgets, QtCore
from PySide2.QtCore import QTimer

width = 1300
height = 768

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        MainWindow.resize(self, 150, 120)

        self.Button_1 = QtWidgets.QPushButton(self)
        self.Button_1.setGeometry(QtCore.QRect(30, 20, 30, 30))
        self.Button_1.setText("1")
        self.Button_2 = QtWidgets.QPushButton(self)
        self.Button_2.setGeometry(QtCore.QRect(90, 20, 30, 30))
        self.Button_2.setText("2")

        self.Button_3 = QtWidgets.QPushButton(self)
        self.Button_3.setGeometry(QtCore.QRect(60, 70, 30, 30))
        self.Button_3.setText("3")

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.update(self.t))
        self.timer.start(1000)

        self.t1 = 0
        self.t2 = 0

    def keyPressEvent(self, event):
        if(event.key() == 49):
            gui.moveTo(width/2 - 40, height/2 - 10)
        elif(event.key() == 50):
            gui.moveTo(width/2 + 20, height/2 - 10)
        elif(event.key() == 51):
            gui.moveTo(width/2 - 10, height/2 + 40)

    def update():
        self.t1 += 1
        a = self.t1%2 
        if(a == 0):
            self.t2 += 1
        mouse.move(400+800*a, 200+400*(self.t2%2))

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = MainWindow()
	demo.show()

	sys.exit(app.exec_())
