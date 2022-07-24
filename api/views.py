
import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest
from main.models import Video, TemproraryFile
from django.core.exceptions import PermissionDenied, ValidationError
from django.views.decorators.csrf import csrf_exempt

from main.utils import validators, get_size, get_duration
from django.conf import settings
from django.core.files.base import File, ContentFile


# Create your views here.
def videos_api(request):

    dict1={
        'videos':list(Video.objects.all().values('id','file','duration','type','size'))
    }
    if request.method == "GET":
        return JsonResponse(dict1)
    else:
        raise PermissionDenied

def videos_api_id(request,id):
    
    dict1={
        'videos':list(Video.objects.filter(id=id).values('id','file','duration','type','size'))
    }

    if request.method == 'GET':
        return JsonResponse(dict1)
    else:    
        raise PermissionDenied

@csrf_exempt
def upload_video(request):
    if request.method == "POST":
        if 'file' not in request.POST:
            return JsonResponse('Bad POST Parameters. Please use "file" key')
        file = request.FILES['file']
        if not file:
            return HttpResponse('file field cannot be empty value')

        temp_file = TemproraryFile()
        temp_file.file.save(file.name, File(file))

        duration = get_duration(temp_file.file.name)
        size = get_size(temp_file.file) 
        extension = temp_file.file.name.split('.')[-1]

        if validators(file.name,duration,size,extension):
            video = Video()

            video.file.save(file.name, File(temp_file.file))
            video.duration = duration
            video.size = size
            video.type = extension

            video.save()
            temp_file.delete()
            return HttpResponse('Video uploaded successfully')
        else:
            temp_file.delete()
            os.remove(f'{settings.MEDIA_ROOT}\{file.name}')
            return HttpResponse('Validation Error')
        
    else:
        raise PermissionDenied

def cost_calculator(request, id):

    if request.method == "GET":
        video = Video.objects.filter(id=id)

        size = video[0].size
        duration = video[0].duration

        if size < 524288000:
            cost = 5
        else:
            cost = 12
            
        if duration < 378:
            cost += 12.5
        else:
            cost += 20
    else:
        raise PermissionDenied

    return JsonResponse({'cost':f'{cost}$'})

def being_uploaded(request):
    dict1={
        'uploading':list(TemproraryFile.objects.all().values('id','file'))
    }

    if request.method == 'GET':
        return JsonResponse(dict1)
    else:    
        raise PermissionDenied