# pycodarr
python transcoder using FFMPEG

Searches in a specified directory for any video files it finds including subdirectories.
These files will then be checked against a blacklist to see if pycodarr already transcoded them.
If the files are in the blacklist then they are left alone, if they are not they are transcoded using
ffmpeg based on user's settings.
