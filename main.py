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
import requests
from bs4 import BeautifulSoup

class ToxicMusicPlayer(QMainWindow):
    def __init__(self):
        super(ToxicMusicPlayer, self).__init__()
        uic.loadUi("form.ui", self)



def test():
    #print("Lalala all")
    print("All URL: ", ToxicFunctional.url)
    print("All Name: ", ToxicFunctional.songName)
    print("len: ", len(ToxicFunctional.url))


ToxicFunctional = functional.PlayMusic()
firstPush = True
def searchUrl():
    music_name = ui.AddMusic.text()
    ui.AddMusic.setText("Loading...")
    if len(music_name) > 4:
        if music_name[0]+music_name[1]+music_name[2]+music_name[3]+music_name[4]+music_name[5] == "https:":
            clip = requests.get(music_name)
            inspect = BeautifulSoup(clip.content, "html.parser")
            yt_title = inspect.find_all("meta", property="og:title")
            for concatMusic1 in yt_title:
                pass
            ToxicFunctional.addNext(music_name, concatMusic1['content'])
    else:
        if len(music_name) > 1:
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
    ui.songName.setText("Playlist is empty")
    
def volumeChange():
    #volume = np.interp(ui.volumeSlider.value(), [0, 99], [0, 100])
    print(ui.volumeSlider.value())
    ToxicFunctional.set_volume(ui.volumeSlider.value())
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
ui.testButton.clicked.connect(test)

#----------------------------------------------------------------------------------------------------------------
RetCode = app.exec()
sys.exit(RetCode)

