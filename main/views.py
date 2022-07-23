import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest
from .models import Video
from django.core.exceptions import PermissionDenied, ValidationError
from django.views.decorators.csrf import csrf_exempt

from moviepy.editor import *
from main.utils import validators, get_size, get_duration


# Create your views here.
def videos_api(request):

    dict1={
        'videos':list(Video.objects.all().values('id','file','duration','type','size'))
    }

    return JsonResponse(dict1)

def videos_api_id(request,id):

    dict1={
        'videos':list(Video.objects.filter(id=id).values('id','file','duration','type','size'))
    }

    return JsonResponse(dict1)


@csrf_exempt
def upload_video(request):

    if request.method == "POST":
        if 'file' not in request.POST:
            return JsonResponse('Bad POST Parameters. Please use "file" key')
        file = request.FILES['file']
        if not file:
            return HttpResponse('file field cannot be empty value')


        duration = get_duration(file)
        size = get_size(file) 
        type = file.name.split('.')[-1]


        if validators(file.name,duration,size,type):
            video = Video(file=file,duration=duration,size=size,type=type)
            video.save()
            return HttpResponse('Video uploaded successfully')
        else:
            return HttpResponse('Validation Error')
    else:
        raise PermissionDenied