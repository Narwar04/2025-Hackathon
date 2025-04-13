from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PySide6 import QtCore, QtWidgets
import sys


class donationAlert():
    name: str

    def __init__(self, username:str):
        print("AAAAAH")
        self.app = QtWidgets.QApplication()
        screenRect = self.app.primaryScreen().geometry()
        self.name = username
        self.label = QLabel()
        self.label2 = QLabel(self.name +"has gifted 40 fenwicks!")
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



        self.movie = QMovie("./gifs/rainbowgangdamn.gif")
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

        sys.exit(self.app.exec())


if __name__ == "__main__":
    guiObj = donationAlert("bob")


    # app = QApplication([])
    # window = QMainWindow()
    # ui = popup()
    # ui.setup(window)
    # window.show()
    # sys.exit(app.exec_())

