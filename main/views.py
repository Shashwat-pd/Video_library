from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests

#api_endpoints
api_endpoints = {
    "videos list": "/api/videos",
    "video": "/api/videos/<id>",
    "upload video": "/api/upload",
    "calculate cost": "/api/<id>/calculate_cost",
    "media URL": "/videos/<filename>"
}

def main_view(request):
    return JsonResponse(api_endpoints)