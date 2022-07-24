import os
from moviepy.editor import VideoFileClip
from django.conf import settings

allowed_extension = ['mp4','mkv']

def validators(file_name,duration,size, extension):
    if extension not in allowed_extension:
        return [False, 'Invalid file type']
    if duration > 10*60:
        return [False, 'Duration too long']
    if size>10**9:
        return [False, 'File too large']
    return [True, 'File uploaded sucessfully']

def get_size(location):
    size = os.path.getsize(location)
    return size

def get_duration(location):
    duration = VideoFileClip(location).duration
    return duration
