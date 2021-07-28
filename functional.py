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
        #self.Instance = vlc.Instance()
        #self.player = self.Instance.media_player_new()
        pass
        

    def play(url):
        video = pafy.new(url)         # https://coderoad.ru/49354232/%D0%9A%D0%B0%D0%BA-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D1%82%D1%8C-%D0%B0%D1%83%D0%B4%D0%B8%D0%BE-%D0%B8%D0%B7-Youtube-URL-%D0%B2-Python-%D0%B1%D0%B5%D0%B7-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8
        best = video.getbest()
        playurl = best.url
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        #player.set_pause(1)


    def pause(self):
        self.player.set_pause(1)
    def unpause(self):
        self.player.set_pause(0)
    
    def searchUrl(self, music_name):
        query_string = urllib.parse.urlencode({"search_query": music_name})

        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())

        clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

        print(clip2)

        inspect = BeautifulSoup(clip.content, "html.parser")
        yt_title = inspect.find_all("meta", property="og:title")

        for concatMusic1 in yt_title:
            pass

        print(concatMusic1['content'])
        return clip2                

    def GetNameOrUrl():
        ui = form.Ui_ToxicMusicPlayer()
        ui.AddMusic.setText("Hello shit")


if __name__ == "__main__":
    test = PlayMusic()

    song = test.searchUrl("Faint")
    test.play(song)


    a = input()