import os
import eyed3 as e3
from tinytag import TinyTag
from folder_funcs import *
import io
# import savify as sv
from savify import Savify
from savify.types import Type, Format, Quality
# import pytube
# from moviepy.editor import VideoFileClip
# import shutil

# def download_MP3(link:str,id:str):
#     video = pytube.YouTube(link)
#     stream = video.streams.get_by_itag(18)
#     stream.download()
#     filename = stream.default_filename
#     clip = VideoFileClip(filename)
#     mp3_file = filename[:-4] + ".mp3"
#     clip.audio.write_audiofile(mp3_file)
#     clip.close()
#     if os.path.exists(filename):
#         os.remove(filename)
#     os.system("cls")
#     cur_path = os.getcwd() + "/" + mp3_file
#     dest_path = make_new_song_file(id)
#     shutil.move(cur_path,dest_path)
#     rename_folder_contents()

# download_MP3("https://www.youtube.com/watch?v=jQPmPlz2dig","https://www.youtube.com/watch?v=jQPmPlz2dig")

def func1():
    x = 1
    if x == 1:
        print("yes")
        # continue