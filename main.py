# This Python file uses the following encoding: utf-8
from os import read
import sys, time
import numpy as np
from PyQt6 import QtGui, uic, QtWidgets, QtCore
from PySide6 import QtWidgets
from gui import form
import functional
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractButton
import requests
from bs4 import BeautifulSoup
import threading

class ToxicMusicPlayer(QMainWindow):
    def __init__(self):
        super(ToxicMusicPlayer, self).__init__()
        uic.loadUi("form.ui", self)



def test():
    print(ToxicFunctional.player.play_item_at_index(1))

ToxicFunctional = functional.PlayMusic()
def searchUrl():
    music_name = ui.AddMusic.text()
    ui.AddMusic.setText("Loading...")
    if len(music_name) > 5:
        if music_name[0]+music_name[1]+music_name[2]+music_name[3]+music_name[4]+music_name[5] == "https:":
            clip = requests.get(music_name)     # частично копия из searchUrl, для вывода названия песни
            inspect = BeautifulSoup(clip.content, "html.parser")
            yt_title = inspect.find_all("meta", property="og:title")
            for concatMusic1 in yt_title:
                pass
            ToxicFunctional.addNext(music_name, concatMusic1['content'])
        else:
            ToxicFunctional.searchUrl(music_name=music_name)
    else:
        if len(music_name) > 1:
            ToxicFunctional.searchUrl(music_name=music_name)
    ui.AddMusic.clear()

def play_pause():
    if ToxicFunctional.firstPlay:
        ToxicFunctional.play()
        ToxicFunctional.firstPlay = False
        ui.songName.setText(ToxicFunctional.songName[ToxicFunctional.numberSongName_Play])
        ui.Play_Pause.setText("Pause/Play")
    else:
        ToxicFunctional.player.pause()
    time.sleep(0.5)
    set_time_for_ui()
    set_time_song_for_ui()

def playNext():
    ToxicFunctional.playNext()
    ui.songName.setText(ToxicFunctional.songName[ToxicFunctional.numberSongName_Play])
    time.sleep(0.5)
    set_time_song_for_ui()
    set_time_for_ui()
def playPrevious():
    ToxicFunctional.playPrevious()
    ui.songName.setText(ToxicFunctional.songName[ToxicFunctional.numberSongName_Play])
    time.sleep(0.5)
    set_time_song_for_ui()
    set_time_for_ui()

def stop():
    ToxicFunctional.stop()
    ToxicFunctional.firstPlay = True
    ui.Play_Pause.setText("Play")
    ui.songName.setText("Playlist is empty")
    
def volumeChange():
    ToxicFunctional.set_volume(ui.volumeSlider.value())

def set_time_song_for_ui():
    # set time song in ui
    songTime = ToxicFunctional.get_length()
    minutes = int(songTime/(1000*60))
    seconds = str((songTime/(1000*60) - minutes) / 10 * 6)
    seconds = seconds[2] + seconds[3]
    ui.songTime.setText(str(minutes) + ":" + str(seconds))
    ui.timeSlider.setMaximum(songTime)

def set_time_for_ui(Timer = True):
    currentTime = ToxicFunctional.get_time()
    minutes = int(currentTime/(1000*60))
    seconds = str((currentTime/(1000*60) - minutes) / 10 * 6)
    if len(str(currentTime)) > 3:
        seconds = seconds[2] + seconds[3]
        ui.currentTime.setText(str(minutes) + ":" + str(seconds))
    ui.timeSlider.setValue(currentTime)
    thread = threading.Timer(1, set_time_for_ui)
    thread.start()
    if ToxicFunctional.player.is_playing() == 0 or Timer == False:
        thread.cancel()

def stop_time_ui():
    set_time_for_ui(Timer=False)

def set_time():
    print(ui.timeSlider.value())
    ToxicFunctional.set_time(ui.timeSlider.value())
    set_time_for_ui()
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
ui.playNext.clicked.connect(playNext)
ui.playPrevious.clicked.connect(playPrevious)
ui.volumeSlider.valueChanged.connect(volumeChange)
ui.timeSlider.sliderPressed.connect(stop_time_ui)
ui.timeSlider.sliderReleased.connect(set_time)
#ui.testButton.clicked.connect(test)
#----------------------------------------------------------------------------------------------------------------
RetCode = app.exec()
stop()
sys.exit(RetCode)

