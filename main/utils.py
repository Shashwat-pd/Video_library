import os
from moviepy.editor import VideoFileClip
from django.conf import settings

allowed_extension = ['mp4','mkv']

def validators(file_name,duration,size, extension):
    if extension not in allowed_extension:
        print('Invalid file type')
        return False
    if duration > 10*60:
        print('Duration too long')
        return False
    if size>10**9:
        print('File too large')
        return False
    return True

def get_size(file):
    size = os.path.getsize(f'{settings.MEDIA_ROOT}\{file.name}')
    return size

def get_duration(file):
    duration = VideoFileClip(f'{settings.MEDIA_ROOT}\{file}').duration
    return duration
