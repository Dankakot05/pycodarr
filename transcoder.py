from os import walk
from pymediainfo import MediaInfo
from pprint import pprint

# some random libraries that are used I don't know why

file_direct = (r"")

def video_search(file_direct):
    video_file_list = []
    _, _, filenames = next(walk(file_direct))
    for x in range(len(filenames)):
        fileInfo = MediaInfo.parse(fr"{file_direct}\{filenames[x]}")
        for track in fileInfo.tracks:
            if track.track_type == "Video":
                video_file_list.append(filenames[x])
    return video_file_list
                
    