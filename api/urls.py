from django.urls import path
from .views import videos_api, upload_video, videos_api_id, cost_calculator, being_uploaded

urlpatterns = [
    path('videos',videos_api,name='videos'),
    path('upload',upload_video,name='add_videos'),
    path('videos/<int:id>',videos_api_id,name='video'),
    path('<int:id>/calculate_cost',cost_calculator,name='cost_calculator'),
    path('being_uploaded',being_uploaded),
]
