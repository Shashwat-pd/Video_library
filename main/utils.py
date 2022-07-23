import os
from moviepy.editor import VideoFileClip

allowed_extension = ['mp4','mkv']

def validators(file_name,duration,size, extension):
    if extension not in allowed_extension:
        print('Invalid file type')
        return False
    if duration > 10*60:
        print('Duration too long')
        return False
    if size>1:
        print('File too large')
        return False
    return True

def get_size(file):
    size = os.path.getsize(file.name)
    return size

def get_duration(file):
    duration = VideoFileClip(file.name).duration
    return duration
