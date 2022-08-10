from distutils.command.upload import upload
from email.policy import default
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Database, Profile


# first app
class AppForms(forms.Form):
    Name = forms.CharField()
    Phone = forms.CharField()

# Olier@1234887
class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields ='__all__'
# database
class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields ='__all__'
        #('video', 'title', 'release_date', 'main_actors', 'genre', 'description', 'movie_poster', 'movie_trailer_link')


class registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']