from distutils.command.upload import upload
from re import T
from django.db import models
from django.forms import FileField

# Create your models here.
class Video(models.Model):
    file = models.FileField(null=True, blank=True)
    size = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    type = models.CharField(max_length=4, default='')

    def __str__(self):
        return self.file.name

