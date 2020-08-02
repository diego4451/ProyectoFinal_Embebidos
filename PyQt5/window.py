from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 200, 300, 100)
    win.setWindowTitle("My Awesome window")

    label = QtWidgets.QLabel(win)
    label.setText("Here's a label")
    label.move(150, 50)

    win.show()
    sys.exit(app.exec_())

window()
