from django.contrib import admin
from .models import Video, TemproraryFile

# Register your models here.
admin.site.register(Video)
admin.site.register(TemproraryFile)