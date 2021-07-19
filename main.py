# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PyQt6 import QtGui, uic, QtWidgets
from PySide6 import QtWidgets
from gui import form
import functional
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QUrl, SIGNAL, Signal
from PySide6.QtUiTools import QUiLoader


class ToxicMusicPlayer(QMainWindow):
    def __init__(self):
        super(ToxicMusicPlayer, self).__init__()
        uic.loadUi("form.ui", self)


if __name__ == "__main__":
    ui = form.Ui_ToxicMusicPlayer()
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui.setupUi(main_window)
    main_window.show()   
    #functional------------------------------------------------------------------------------------------------------
    #ui.pushButton.clicked.connect(functional.PlayMusic.Music)
    

    #----------------------------------------------------------------------------------------------------------------
    RetCode = app.exec()
    sys.exit(RetCode)
