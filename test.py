import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import time

""" music_name = "Linkin Park Numb"
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

a = input("a = ")
subprocess.Popen("start /b " + "C:\PyProject\playMusicPython\MPVplayer\mpv.exe " + clip2 + "--no-video", shell=True)
b = input("b = ") """

import vlc, pafy
from PySide6.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

""" p = vlc.MediaPlayer(('https://www.youtube.com/watch?v=K3a-Q2wUsbs'))
p.play() """

""" player = QMediaPlayer()
player.setMedia(QMediaContent(('https://www.youtube.com/watch?v=K3a-Q2wUsbs')))
player.play() """

""" import vlc
p = vlc.MediaPlayer("https://www.youtube.com/watch?v=qrWPKu37H1E5")
p.play()
 """


""" 
import ffmpeg
input = ffmpeg.input("C:\PyProject\playMusicPython\ToxicMusicPlayer\source\music\Life Eternal.mp3")
audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
video = input.video.hflip()
out = ffmpeg.output(audio, video, 'out.mp3') """


""" import pafy
import vlc

url = "https://www.youtube.com/watch?v=LYU-8IFcDPw"# Работает!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
video = pafy.new(url)                           # https://coderoad.ru/49354232/%D0%9A%D0%B0%D0%BA-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D1%82%D1%8C-%D0%B0%D1%83%D0%B4%D0%B8%D0%BE-%D0%B8%D0%B7-Youtube-URL-%D0%B2-Python-%D0%B1%D0%B5%D0%B7-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8
best = video.getbest()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()                   # Работает!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 """


# TEST MediaList(Player)
""" url = "https://www.youtube.com/watch?v=LYU-8IFcDPw"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
Instance = vlc.Instance()
player = Instance.media_list_player_new()
Media = Instance.media_new(playurl)
MediaTest = Instance.media_list_new()
print("MediaTest.media()", MediaTest.media())
MediaTest.add_media(Media.get_mrl())
player.set_media_list(MediaTest)
url = "https://www.youtube.com/watch?v=lvs68OKOquM"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
Media = Instance.media_new(playurl)
MediaTest.add_media(Media.get_mrl())

player.play()
print("get_media_player", player.get_media_player)
time.sleep(3)
print("MediaTest.media()", MediaTest.media()) """


url = "https://www.youtube.com/watch?v=LYU-8IFcDPw"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
Instance = vlc.Instance() 
Media = Instance.media_new(playurl)
# creating vlc media player object

  
# media object
#media = vlc.Media("source\music\Life Eternal.mp3")

url = "https://www.youtube.com/watch?v=LYU-8IFcDPw"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
Instance = vlc.Instance()
Media = Instance.media_new(playurl)
MediaTest = Instance.media_list_new()
MediaTest.add_media(Media.get_mrl())
url = "https://www.youtube.com/watch?v=lvs68OKOquM"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
Media = Instance.media_new(playurl)
MediaTest.add_media(Media.get_mrl())


player = Instance.media_list_player_new()
player.set_media_list(MediaTest)
# setting media to the media player
media_player = vlc.MediaPlayer()
media_player.set_media(Media)

  
# start playing video
media_player.play()
print(media_player.is_playing())  
# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(0.01)
print(media_player.get_length())  
print(media_player.is_playing())

c = input("c = ")