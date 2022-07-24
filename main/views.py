from django.http import JsonResponse
from django.shortcuts import render

#api_endpoints
api_endpoints = {
    "videos list": "/api/videos",
    "video": "/api/videos/<id>",
    "upload video": "/api/upload",
    "calculate cost": "/api/<id>/calculate_cost",
    "being uploaded": "/api/being_uploaded",
    "media URL": "/videos/<filename>"
}

def main_view(request):
    """
    view of main page that lists api endpoints`
    """
    return JsonResponse(api_endpoints)