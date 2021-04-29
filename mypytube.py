from pytube import Playlist
from pytube import YouTube
import pytube


def getVideo():
    print('Enter the url')
    url = input() 
    youtube = pytube.YouTube(url)
    yt = pytube.YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print('Download complete')
def getPlayList():
    print('Enter the url')
    url = input() 
    p = Playlist(url)
    print(f'Downloading: {p.title}')
    for video in p.videos:
         print(f'video title: {video.title}')
         video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print('Download complete')

def menuScreen():
    print(" ")
    print("choose the type of download")
    print("0  - Video")
    print("1  - Playlist")
    print("99 - Exit")
def main():
    print("***Welcome to My-Pytube***")

    while True:
       menuScreen()
       choice = input()
       if choice == "0":
          getVideo()
       if choice == "1":
          getPlayList()
       if choice =="99":
           break
 
if __name__ == '__main__':
	main()