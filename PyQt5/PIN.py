# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIN.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#pyuic5 -x PIN.ui -o PIN.py

import sys
<<<<<<< HEAD
import mouse
=======
import pyautogui as gui
import cv2
import numpy as np
>>>>>>> f06f3551ef48ddf65599937915ee452b781d9a30
from PyQt5 import QtCore, QtGui, QtWidgets
from Access import Ui_MainWindow

def rescale_frame(frame, wpercent=130, hpercent=130):
    width = int(frame.shape[1] * wpercent / 100)
    height = int(frame.shape[0] * hpercent / 100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


def contours(hist_mask_image):
    gray_hist_mask_image = cv2.cvtColor(hist_mask_image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_hist_mask_image, 0, 255, 0)
    cont, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return cont

def draw_rect(frame):
    rows, cols, _ = frame.shape
    global total_rectangle, hand_rect_one_x, hand_rect_one_y, hand_rect_two_x, hand_rect_two_y

    hand_rect_one_x = np.array(
        [6 * rows / 20, 6 * rows / 20, 6 * rows / 20, 9 * rows / 20, 9 * rows / 20, 9 * rows / 20, 12 * rows / 20,
         12 * rows / 20, 12 * rows / 20], dtype=np.uint32)

    hand_rect_one_y = np.array(
        [9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20,
         10 * cols / 20, 11 * cols / 20], dtype=np.uint32)

    hand_rect_two_x = hand_rect_one_x + 10
    hand_rect_two_y = hand_rect_one_y + 10

    for i in range(total_rectangle):
        cv2.rectangle(frame, (hand_rect_one_y[i], hand_rect_one_x[i]),
                      (hand_rect_two_y[i], hand_rect_two_x[i]),
                      (0, 255, 0), 1)

    return frame


def hand_histogram(frame):
    global hand_rect_one_x, hand_rect_one_y

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    roi = np.zeros([90, 10, 3], dtype=hsv_frame.dtype)

    for i in range(total_rectangle):
        roi[i * 10: i * 10 + 10, 0: 10] = hsv_frame[hand_rect_one_x[i]:hand_rect_one_x[i] + 10,
                                          hand_rect_one_y[i]:hand_rect_one_y[i] + 10]

    hand_hist = cv2.calcHist([roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
    return cv2.normalize(hand_hist, hand_hist, 0, 255, cv2.NORM_MINMAX)


def hist_masking(frame, hist):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    dst = cv2.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)

    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31))
    cv2.filter2D(dst, -1, disc, dst)

    ret, thresh = cv2.threshold(dst, 150, 255, cv2.THRESH_BINARY) #ret, thresh = cv2.threshold(dst, 150, 255, cv2.THRESH_BINARY)

    #thresh = cv2.dilate(thresh, None, iterations=5)

    thresh = cv2.merge((thresh, thresh, thresh))

    return cv2.bitwise_and(frame, thresh)


def centroid(max_contour):
    moment = cv2.moments(max_contour)
    if moment['m00'] != 0:
        cx = int(moment['m10'] / moment['m00'])
        cy = int(moment['m01'] / moment['m00'])
        return cx, cy
    else:
        return None

def draw_circles(frame, traverse_point):
    if traverse_point is not None:
        for i in range(len(traverse_point)):
            cv2.circle(frame, traverse_point[i], 5, [0, 255, 255], -1)

def manage_image_opr(frame, hand_hist):
    hist_mask_image = hist_masking(frame, hand_hist)

    hist_mask_image = cv2.erode(hist_mask_image, None, iterations=2)
    hist_mask_image = cv2.dilate(hist_mask_image, None, iterations=2)

    contour_list = contours(hist_mask_image)
    max_cont = max(contour_list, key=cv2.contourArea)

    cnt_centroid = centroid(max_cont)
    cv2.circle(frame, cnt_centroid, 5, [255, 0, 255], -1)

    if max_cont is not None:
        hull = cv2.convexHull(max_cont, returnPoints=False)
        defects = cv2.convexityDefects(max_cont, hull)
        #far_point = farthest_point(defects, max_cont, cnt_centroid)
        print("Centroid : " + str(cnt_centroid))

def tracking(hand_hist):

    capture = cv2.VideoCapture(0)

    pressed_key = cv2.waitKey(42)
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)

    manage_image_opr(frame, hand_hist)

    capture.release()

def cal():

    hand_hist = None
    traverse_point = []
    total_rectangle = 9
    hand_rect_one_x = None
    hand_rect_one_y = None

    hand_rect_two_x = None
    hand_rect_two_y = None

    global hand_hist
    capture = cv2.VideoCapture(0)

    while capture.isOpened():
        pressed_key = cv2.waitKey(42)
        _, frame = capture.read()
        frame = cv2.flip(frame, 1)

        if pressed_key & 0xFF == ord('z'):
            hand_hist = hand_histogram(frame)
            cv2.destroyAllWindows()
            capture.release()
            return hand_hist
        else:
            frame = draw_rect(frame)
        imagen1=rescale_frame(frame)
        cv2.imshow("Live Feed", imagen1)
        #cv2.imwrite("imagen.jpg", imagen1)

class Welcome(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window, self.MainWindow)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        width = 1300
        height = 768
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
    cal()
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Welcome()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
