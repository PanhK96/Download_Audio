from moviepy.editor import *
from pytube import YouTube,Playlist
from youtubesearchpython import Search,PlaylistsSearch
import webbrowser
import os
import time
import pathlib
import shutil

def main(PATH):
    while True: 
        in_lua_chon()
        ans1 = input("Câu trả lời: ")
        print("")
        if ans1 == "1":
            search_with_name(PATH)
        elif ans1 == "2":
            search_with_url(PATH)
        elif ans1 == "3":
            download_playlist(PATH)
        elif ans1 == "4":
            play_on_youtube()
        elif ans1 == "5":
            print("Cảm ơn bạn đã sử dụng chương trình.")
            quit()
        else:
            print("Vui lòng nhập số.\n")
            continue
        

def search_with_url(PATH):
    urls = input("Nhập đường dẫn url tại đây: ")
    yt =YouTube(urls)
    yd = yt.streams.filter(only_audio=True).first()
    video = AudioFileClip(yd.url)
    new_title = xóa_kí_tựa_đặc_biệt(yt.title)
    video.write_audiofile(f'{PATH}'+"\\"+ new_title +".mp3")
    print("Đã hoàn tất tải bài hát \"" + yt.title +"\" của tác giả " + yt.author+"\n")
    time.sleep(10)
    os.system('cls')


def search_with_name(PATH):
        song_name = input("Nhập tên bài hát bạn muốn tải xuống: ")
        n=1
        while True:
            allSearch = Search(song_name, limit=n)
            search_result = allSearch.result()
            urls = search_result['result'][n-1]['link']
            
            yt = YouTube(urls)
            print("Tiêu đề:", yt.title)
            print("Tác giả:", yt.author)
            ans = input("Đây có phải bài hát bạn đang tìm ?(y/n) ")            
            print("")
            #kiểm tra có đúng bài hát người dùng muốn.    
            if ans == 'y':
                yd = yt.streams.filter(only_audio=True).first()
                video = AudioFileClip(yd.url)
                new_title = xóa_kí_tựa_đặc_biệt(yt.title)
                video.write_audiofile(f'{PATH}'+"\\"+ new_title +".mp3")
                print("Đã hoàn tất tải bài hát \"" + yt.title +"\" của tác giả " + yt.author+"\n")
                time.sleep(10)
                os.system('cls')
                return main(PATH)
            else:
                n += 1
                continue 
             
            
def download_playlist(PATH):
    playlist_name = input("Nhập playlist mà bạn muốn tải xuống (nhập chính xác càng tốt): ")
    n = 1
    while True:
        playlistsSearch = PlaylistsSearch(playlist_name, limit=n)
        search_result = playlistsSearch.result()
        title_playlist = search_result['result'][n-1]['title']
        author_playlist = search_result['result'][n-1]['channel']['name']
        
        print("")
        print("Tiêu đề playlist: ",title_playlist)
        print("Tác giả: ",author_playlist)
        ans = input("Đây có phải playlist bạn đang tìm ?(y/n) ")
        if ans == 'y':
            new_title_playlist = xóa_kí_tựa_đặc_biệt(title_playlist)
            os.makedirs(new_title_playlist)
            now_location = str(pathlib.Path(new_title_playlist).parent.resolve())
            full_now_location = now_location+"\\"+ new_title_playlist
            new_location =str( PATH +"\\"+ new_title_playlist)
            shutil.move(full_now_location, new_location)
            urls = search_result['result'][n-1]['link']
            video_links = Playlist(urls).video_urls
            
            for video_link in video_links:
                yt =YouTube(video_link)
                yd = yt.streams.filter(only_audio=True).first()
                video = AudioFileClip(yd.url)
                new_title = xóa_kí_tựa_đặc_biệt(yt.title)
                video.write_audiofile(f'{PATH}'+"\\"+new_title_playlist+"\\"+ new_title +".mp3")
                
            print("Đã hoàn tất tải playlist "+title_playlist+" của tác giả "+yt.author)
            time.sleep(10)
            os.system('cls')
            return main(PATH)
            
        else:
            n += 1
            continue 
        
def play_on_youtube():
    song_name = input("Nhập tên bài hát bạn muốn chơi: ")
    n=1
    while True:
        allSearch = Search(song_name, limit=n)
        search_result = allSearch.result()
        urls = search_result['result'][n-1]['link']
        yt = YouTube(urls)
        print("Tiêu đề:", yt.title)
        print("Tác giả:", yt.author)
        ans = input("Đây có phải bài hát bạn đang tìm ?(y/n) ")            
        print("") 
        if ans == 'y':
            print("playing " + yt.title + " on Youtube")
            webbrowser.open(urls)
            time.sleep(10)
            os.system('cls')
            break
        else:
            n += 1
            continue 

                       
def in_lua_chon():
    print("Hãy chọn chức năng mà bạn muốn sử dụng: ")
    print("1.Tải bài hát theo tên bài hát.")
    print("2.Tải bài hát theo đường dẫn url.")
    print("3.Tải cả playlist.")
    print("4.Chơi nhạc trên Youtube.")
    print("5.Thoát")
    print("")
 
 
def xóa_kí_tựa_đặc_biệt(new_title):
   return new_title.replace("|","-").replace("*","").replace("/","-").replace("\\","-").replace("?","").replace(">","'").replace("<","'").replace("\"","'")       
