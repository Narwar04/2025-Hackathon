#!/usr/bin/env python3

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class Chat(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        text = QtWidgets.QLabel("Hello World")
        self.layout.addWidget(text)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = Chat()
    widget.resize(800, 600)
    widget.setStyleSheet("background: transparent;")
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    widget.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    widget.show()

    sys.exit(app.exec())