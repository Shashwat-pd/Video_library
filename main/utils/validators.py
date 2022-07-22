def validators(file_name,duration,size, extension):
    if extension != 'mp4' and extension != 'mkv':
        print('Invalid file type')
        return False
    if duration > 10*60:
        print('Duration too long')
        return False
    if size>1:
        print('File too large')
        return False
    return True