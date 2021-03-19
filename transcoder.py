from os import walk
from pymediainfo import MediaInfo
from pprint import pprint
import glob

# some random libraries that are used I don't know why
def main():
    file_directory = (r"")
    print(video_search(file_directory))
# searches recursivly for all file extensions in variable 'extensions'
    
def video_search(file_direct):
    files = []
    extensions = ["mp4"]
    for x in range(len(extensions)):
        temp = glob.glob(file_direct + f"/**/*.{extensions[x]}", recursive = True)
        files.extend(temp)
    return files
                
main()
