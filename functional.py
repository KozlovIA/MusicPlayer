from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PySide6.QtCore import QUrl
import time
import vlc
import pafy
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
from gui import form

class PlayMusic():
    def __init__(self) -> None:
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()
        self.MediaPlayer = vlc.MediaPlayer()
        self.volume = 100
        self.url = [""]*1000
        self.songName = [""]*1000
        self.numberName = 0     # Номер имени песни для записи в переменную self.url
        self.numberSong = 0     # Номер песни для вопроизведения
        self.firstPlay = True      # Переменная служит для использования вне класса, для проверки 1-го нажатия на Play/Pause
        
        

    def play(self):
        print("URL = ", self.url[self.numberSong])
        video = pafy.new(self.url[self.numberSong])         # https://coderoad.ru/49354232/%D0%9A%D0%B0%D0%BA-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D1%82%D1%8C-%D0%B0%D1%83%D0%B4%D0%B8%D0%BE-%D0%B8%D0%B7-Youtube-URL-%D0%B2-Python-%D0%B1%D0%B5%D0%B7-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8
        best = video.getbest()
        playurl = best.url
        #Instance = vlc.Instance()
        #player = self.Instance.media_player_new()
        Media = self.Instance.media_new(playurl)
        Media.get_mrl()
        self.player.set_media(Media)
        self.player.play()
        self.numberSong = self.numberSong + 1
        #player.set_pause(1)


    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def set_volume(self, vol):
        self.volume = vol
        self.MediaPlayer.audio_set_volume(self.volume)


    def searchUrl(self, music_name):
        query_string = urllib.parse.urlencode({"search_query": music_name})

        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())

        clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

        #print(clip2)

        inspect = BeautifulSoup(clip.content, "html.parser")
        yt_title = inspect.find_all("meta", property="og:title")

        for concatMusic1 in yt_title:
            pass
        #print(concatMusic1['content'])
        self.url[self.numberName] = clip2
        self.songName[self.numberName] = concatMusic1['content']
        self.numberName = self.numberName + 1
        return clip2, concatMusic1['content']                


    def test(self, vol):
        print("volume: ")
        self.MediaPlayer.audio_set_volume(vol)
        print(self.MediaPlayer.audio_get_volume())
    

if __name__ == "__main__":
    test = PlayMusic()
    song = test.searchUrl("Faint")
    test.play()
    test.test(20)

    a = input()