from distutils.command.upload import upload
from multiprocessing import Value
import django
from django.core.validators import FileExtensionValidator
from collections import UserDict
from django.db import models
import datetime as timezone


class Database(models.Model):
    video = models.FileField(upload_to='USER_FAVORITE_VIDEO%Y',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateTimeField(default=django.utils.timezone.now)
    title = models.CharField(max_length=100, blank=True, null=True)
    release_date =models.DateTimeField(auto_now_add=True, null=True)
    main_actors = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    movie_poster = models.FileField(upload_to='MOVIE_POSTER',null=True)
    movie_trailer_link = models.CharField(max_length=100)
   

def __str__(self):
    return self.title

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    profile_image =models.ImageField(null=True, upload_to='photoes')
    registration_date = models.DateTimeField(default=django.utils.timezone.now)

def __str__(self):
    return self.first_name

# Create your models here.
