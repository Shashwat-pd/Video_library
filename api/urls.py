from django.urls import path
from main.views import videos_api, upload_video, videos_api_id

urlpatterns = [
    path('videos',videos_api,name='videos'),
    path('upload',upload_video,name='add_videos'),
    path('videos/<int:id>',videos_api_id,name='video'),
]
