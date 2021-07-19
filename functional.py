from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PySide6.QtCore import QUrl
from pygame import mixer
import pygame
import time
import vlc

class PlayMusic():
    def __init__(self) -> None:
        pass

    def Music(self):
        #pygame.mixer.init()
        #pygame.mixer.music.load("source/music/Life Eternal.mp3")
        #pygame.mixer.music.play()
        player = QMediaPlayer()
        player.setMedia(QMediaContent(QUrl("https://www.youtube.com/watch?v=MAiV8RpqzME")))
        player.play()
        




if __name__ == "__main__":
    test = PlayMusic()
    test.Music()

    a = input()