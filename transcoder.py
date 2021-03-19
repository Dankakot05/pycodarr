from os import walk
from pymediainfo import MediaInfo
from pprint import pprint

# some random libraries that are used I don't know why

file_direct = (r"")

# sets the file directory to be used to make changing directories easier

_, _, filenames = next(walk(file_direct))

# saves a list of all files in the directory specified

for x in range(len(filenames)):
    fileInfo = MediaInfo.parse(fr"{file_direct}\{filenames[x]}")
    
    # checks if any files in the directory are video files
    
    for track in fileInfo.tracks:
        if track.track_type == "Video":
            extension = ((filenames[x])[len(filenames[x])-4:len(filenames[x])])
            print(extension)
            
