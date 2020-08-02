#pip3 install PyQt5 PyQt5-tools

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
        self.setGeometry(500, 200, 300, 100)
        self.setWindowTitle("My Awesome window")

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Here's a label")
        self.label.move(150, 50)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Click me")
        self.button.clicked.connect(self.Click)
        
        self.i = 0

    def Click(self):
        self.i += 1
        self.label.setText("Clicks: " + str(self.i))

def Click():
    print("Clicky")

def window():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

window()
