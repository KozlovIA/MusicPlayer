# This Python file uses the following encoding: utf-8
from os import read
import sys
import numpy as np
from PyQt6 import QtGui, uic, QtWidgets, QtCore
from PySide6 import QtWidgets
from gui import form
import functional
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractButton



class ToxicMusicPlayer(QMainWindow):
    def __init__(self):
        super(ToxicMusicPlayer, self).__init__()
        uic.loadUi("form.ui", self)



def test():
    print("Lalala all")

ToxicFunctional = functional.PlayMusic()
firstPush = True
def searchUrl():
    music_name = ui.AddMusic.text()
    ui.AddMusic.setText("Loading...")
    ToxicFunctional.searchUrl(music_name=music_name)
    ui.AddMusic.clear()

def play_pause():
    if ToxicFunctional.firstPlay:
        ToxicFunctional.play()
        ToxicFunctional.firstPlay = False
        ui.songName.setText(ToxicFunctional.songName[ToxicFunctional.numberSong-1])
        ui.Play_Pause.setText("Pause/Play")
    else:
        ToxicFunctional.player.pause()

def stop():
    ToxicFunctional.stop()
    firstPush = True
    ui.Play_Pause.setText("Play")
    ui.songName.clear("Playlist is empty")
    
def volumeChange():
    volume = np.interp(ui.volumeSlider.value(), [0, 99], [0, 100])
    ToxicFunctional.set_volume(int(volume))
#---------------------------------------------------------------------------------------------------------
#--------------------- Создание окна ---------------------------------------------------------------------
ui = form.Ui_ToxicMusicPlayer()
app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
ui.setupUi(main_window)
main_window.show()   
#functional------------------------------------------------------------------------------------------------------
ui.Play_Pause.clicked.connect(play_pause)    
ui.AddMusicButton.clicked.connect(searchUrl)
ui.playStop.clicked.connect(stop)
ui.volumeSlider.valueChanged.connect(volumeChange)


#----------------------------------------------------------------------------------------------------------------
RetCode = app.exec()
sys.exit(RetCode)

