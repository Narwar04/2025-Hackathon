#!/usr/bin/env python3

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class ChatWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.text = QtWidgets.QTextEdit("")
        self.layout.addWidget(self.text)

class Gui():
    def __init__(self):
        self.app = QtWidgets.QApplication()

        self.widget = ChatWidget()
        self.widget.resize(400, 600)
        self.widget.setStyleSheet("background: transparent;")
        #self.widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.widget.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.widget.show()

    def qtprint(self, str):
        self.widget.text.append(str)