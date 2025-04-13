#!/usr/bin/env python3

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from time import sleep

class ChatWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.text = QtWidgets.QTextEdit("")
        self.text.setReadOnly(True)
        self.text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text.setFont(QtGui.QFont("Helvetica", 24))
        self.layout.addWidget(self.text)

class donationAlertWindow(QtWidgets.QMainWindow):
    name: str

    def __init__(self, app: QtWidgets.QApplication, username:str):
        super().__init__()
        screenRect = app.primaryScreen().geometry()
        self.name = username
        self.label = QtWidgets.QLabel()
        self.label2 = QtWidgets.QLabel(self.name +"has gifted 40 dollars!")
        self.label2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label2.setStyleSheet("""
                            QLabel {
                                font-size: 24px;
                                color: white;
                                font-weight: 900;
                            }""")
        self.label2.resize(400, 200)
        self.label2.move(screenRect.width()*0.7, screenRect.height()*0.1)
        self.label2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label2.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.label2.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)



        self.movie = QtGui.QMovie("./gifs/rainbowgangdamn.gif")
        self.movie.setScaledSize(QtCore.QSize(200, 200))
        self.label.setMovie(self.movie)
        self.movie.start()

        self.widget = self.label
        self.widget.resize(200, 200)
        self.widget.move(screenRect.width()*0.7, screenRect.height()*0.1)
        #self.widget.setStyleSheet("background: transparent;")
        #self.widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.widget.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.widget.show()
        self.label2.show()

        # super().__init__()
        # print("opening gif")

        # # self.label2 = QtWidgets.QLabel("bob" + "has gifted 40 fenwicks!")
        # # self.label2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        # # self.label2.setStyleSheet("""
        # #                     QLabel {
        # #                         font-size: 24px;
        # #                         color: white;
        # #                         font-weight: 900;
        # #                     }""")
        # # self.label2.resize(400, 200)
        # # self.label2.move(screenRect.width()*0.7, screenRect.height()*0.1)
        # # self.label2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # # self.label2.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # # self.label2.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        # self.setGeometry(200,200,200,200)
        # self.movie = QtGui.QMovie("./../gifs/rainbowgangdamn.gif")
        # self.label = QtWidgets.QLabel(self)
        # self.label.setMovie(self.movie)
        # self.movie.start()

        # # self.movie.setScaledSize(QtCore.QSize(200, 200))

        # # self.label.resize(200, 200)
        # # self.widget.move(screenRect.width()*0.7, screenRect.height()*0.1)
        # # self.widget.setStyleSheet("background: transparent;")
        # # self.widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # # self.widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # # self.widget.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        # # self.setCentralWidget(self.label)

class Gui():
    def __init__(self):
        self.app = QtWidgets.QApplication()

        print("before gif")
        # self.app.window = donationAlertWindow(self.app, "wilson")
        print("start timer")
        self.timer = QtCore.QTimer()
        self.timer.singleShot(5000, lambda: self.donationAlert(self.app))
        # self.timer.singleShot(2500, self.app.window.hide)



        self.widget = ChatWidget()
        self.widget.resize(400, 600)
        self.widget.setStyleSheet("background: transparent;")
        self.widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.widget.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.widget.show()


    def qtprint(self, str):
        self.widget.text.insertHtml(str)
        self.widget.text.ensureCursorVisible()

    def donationAlert(self, app: QtWidgets.QApplication):
        print("donationAlert")
        app.window = donationAlertWindow(self.app, "wilson")
        # print(window.movie.state())
        self.timer.singleShot(400, lambda: app.window.widget.hide())
        self.timer.singleShot(400, lambda: app.window.label2.hide())

        self.timer.singleShot(100000 * (random.random()), lambda: self.donationAlert(app))

    # def turnOff(self,  app: QtWidgets.QApplication):
    #     print("turn off")
    #     self.timer.singleShot(5000, lambda: self.donationAlert(app))