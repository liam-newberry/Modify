# File created by: Liam Newberry
from eyed3 import load as e3_load
import io
import os
from screeninfo import get_monitors
from tinytag import TinyTag

def make_songs_file():
    main_folder = os.getcwd()
    song_folder = os.path.join(main_folder, "songs")
    file_name = "songs"
    current_path = os.getcwd()
    current_path += "/"
    new_path = current_path + file_name
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return main_folder, song_folder

main_folder, song_folder = make_songs_file()

def get_monitor_resolution():
    data = str(get_monitors()[0])
    width = data.index("width=") + len("width=")
    w = data[width:]
    width = data[width:width + w.index(",")]
    width = int(width)
    height = data.index("height=") + len("height=")
    h = data[height:]
    height = data[height:height + h.index(",")]
    height = int(height)
    return width, height

def get_song_id(link:str):
    start_pos = link.index("=")
    return link[start_pos+1:]

def get_song_image(folder_id:str):
    for folder in os.scandir(song_folder):
        if folder.name == folder_id:
            for doc in os.scandir(folder):
                if doc.name.endswith(".mp3"):
                    audio_file = e3_load(doc)
                    for image in audio_file.tag.images:
                        return io.BytesIO(image.image_data)

def get_song_info(folder_id:str):
    for folder in os.scandir(song_folder):
        if folder.name == folder_id:
            for entry in os.scandir(folder):
                if entry.name.endswith(".mp3"):
                    tag = TinyTag.get(entry)
                    stats = {"album":tag.album,
                            "artist":tag.artist,
                            "duration":tag.duration,
                            "genre":tag.genre,
                            "image":get_song_image(folder_id),
                            "sample rate":tag.samplerate,
                            "title":tag.title,
                            "track":tag.track,
                            "track total":tag.track_total,
                            "year":tag.year}
                    return stats

def make_new_song_file(id:str):
    make_songs_file()
    id = get_song_id(id)
    file_name = id
    current_path = os.getcwd()
    current_path += "/songs/"
    new_path = current_path + file_name
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path

def rename_folder_contents():
    for folder in os.scandir(song_folder):
        song_id = folder.name
        for entry in os.scandir(folder):
            if entry.name.endswith(".mp3"):
                if song_id not in entry.name:
                    temp_path = (entry.path[:-len(entry.name)])
                    os.rename(entry.path, temp_path + song_id + ".mp3")