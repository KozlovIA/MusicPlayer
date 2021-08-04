from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PySide6.QtCore import QUrl
import time
import vlc
import pafy
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
from gui import form
# v1.5(alpha)   добавление next/previous и корректирка выводимых данных, большое обновление
class PlayMusic():
    def __init__(self) -> None:
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_list_player_new()
        self.mediaList = self.Instance.media_list_new()
        self.volume = 100       # текущее значение звука
        self.url = [""]*1000    # list для ссылок на песни
        self.songName = [""]*1000 # list названий песен
        self.numberSongName = 0 # номер играющей песни для вывода информации
        self.numberSong = 0     # Номер имени песни для записи в переменную self.url и mediaList
        self.firstPlay = True      # Переменная служит для использования вне класса, для проверки 1-го нажатия на Play/Pause
        
        

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def set_volume(self, vol):
        self.volume = vol
        self.player.audio_set_volume(self.volume)

    def addNext(self, URL, name, video = True):
        self.url[self.numberSong] = URL
        self.songName[self.numberSong] = name 

        video_audio = pafy.new(self.url[self.numberSong])         # https://coderoad.ru/49354232/%D0%9A%D0%B0%D0%BA-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D1%82%D1%8C-%D0%B0%D1%83%D0%B4%D0%B8%D0%BE-%D0%B8%D0%B7-Youtube-URL-%D0%B2-Python-%D0%B1%D0%B5%D0%B7-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8
        if video:
            best = video_audio.getbest()
        else:
            best = video_audio.getbestaudio()
        playurl = best.url
        Media = self.Instance.media_new(playurl)
        self.mediaList.add_media(Media.get_mrl())
        if self.numberSong == 0:
            self.player.set_media_list(self.mediaList)
        self.numberSong = self.numberSong + 1


    def playNext(self):
        self.player.next()
        self.numberSongName = self.numberSongName + 1
    def playPrevious(self):
        self.player.previous()
        self.numberSongName = self.numberSongName - 1
        

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
        self.addNext(clip2, concatMusic1['content'])

        return clip2, concatMusic1['content']                


    def test(self, vol):
        print("volume: ")
        self.MediaPlayer.audio_set_volume(vol)
        print(self.MediaPlayer.audio_get_volume())
    

if __name__ == "__main__":
    test = PlayMusic()
    song = test.addNext("https://www.youtube.com/watch?v=0kJdWJXxF3Y", "Reason to Believe")
    song = test.addNext("https://www.youtube.com/watch?v=zsCD5XCu6CM", "Somewhere I Belong")
    test.play()
    time.sleep(5)
    test.playNext()


    a = input()
