
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.core.files.base import File
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.views.decorators.csrf import csrf_exempt

from main.utils import validators, get_size, get_duration
from main.models import Video



uploadings = []


def videos_api(request):
    """
    view of API endpoint to get list of videos in database.
    """
    dict1={
        'videos':list(Video.objects.all().values('id','file','duration','type','size'))
    }
    if request.method == "GET":
        return JsonResponse(dict1)
    else:
        raise PermissionDenied

def videos_api_id(request,id):
    """
    view of API endpoint to get video by id.
    """
    dict1={
        'videos':list(Video.objects.filter(id=id).values('id','file','duration','type','size'))
    }

    if request.method == 'GET':
        return JsonResponse(dict1)
    else:    
        raise PermissionDenied

@csrf_exempt
def upload_video(request):
    """
    view of API endpoint to upload video.
    
    """
    if request.method == "POST":
        if 'file' not in request.POST:
            return JsonResponse({"message":"Bad POST Parameters. Please use file key"})
        file = request.FILES['file']
        if not file:
            return JsonResponse({"message" :"file field cannot be empty value"})

        uploadings.append(file.name) # add file name to list of uploading files for another API endpoint
        
        location = TemporaryUploadedFile.temporary_file_path(file) # get location of file saved by django in temporary folder

        duration = get_duration(location)
        size = get_size(location) 
        extension = file.name.split('.')[-1]
        
        valid, message = validators(file.name,duration,size,extension)
        if valid:
            video = Video()
            
            video.file.save(file.name, File(file)) # save file in database using django File class, conventional way throws an error  
            video.duration = duration 
            video.size = size 
            video.type = extension

            video.save()
            uploadings.remove(file.name) 
            
            return JsonResponse({"message" :message})
        else:
            uploadings.remove(file.name)
            return JsonResponse({"message" : message})
        
    else:
        raise PermissionDenied

def cost_calculator(request, id):
    """
    view of API endpoint to calculate cost of video.
    """
    if request.method == "GET":
        video = Video.objects.filter(id=id)

        size = video[0].size
        duration = video[0].duration

        if size < 524288000: # 500MB
            cost = 5
        else:
            cost = 12
            
        if duration < 378: # 6 minutes 18 seconds
            cost += 12.5
        else:
            cost += 20
    else:
        raise PermissionDenied

    return JsonResponse({'cost':f'{cost}$'})

def being_uploaded(request):
    dict1={
        'uploading': uploadings
    }

    if request.method == 'GET':
        return JsonResponse(dict1)
    else:    
        raise PermissionDenied