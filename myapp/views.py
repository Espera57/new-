from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.csrf import csrf_protect

from myapp.models import Database, Profile

from .forms import AppForms, DatabaseForm, registration,profileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout


def search_venue(request):
    return render(request, 'search_venue.html',{})

def loginsite(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'incorrect user')
            return redirect('signin')
    return render(request, 'login.html')


def logoutsite(request):
    logout(request)
    messages.success(request, " You logout success")
    return redirect('signin')


#@login_required(login_url='signin')
# registration in default
def register(request):
    form = registration()
    if request.method == 'POST':
        form = registration(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'thank for create account success \t' + user)
            return redirect('signin')
    context = {'form': form}
    return render(request, 'register.html', context)


# used to user database without save data
def new(request):
    if request.method == 'POST':
        form = AppForms(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Phone = form.cleaned_data['Phone']
            print(Name, Phone)
    form = AppForms()
    return render(request, 'form.html', {'forms': form})

def profiledata(request):
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.owner=request.user.id
            profile.save()
            return HttpResponseRedirect('home')

    form = profileForm()
    return render(request, 'profile.html', {'forms': form})

# save data in database Datab 
def datab_data(request):
    if request.method == 'POST':
        form = DatabaseForm(request.POST, request.FILES)
        if form.is_valid():
            videos=form.save(commit=False)
            videos.owner=request.user.id
            videos.save()
            return HttpResponseRedirect('home')

    form = DatabaseForm()
    return render(request, 'form.html', {'forms': form})

@login_required(login_url='signin')
def home(request):
    #video={Database.objects.all()}
    context = {
       'video':Database.objects.all(),
       'profile':Profile.objects.all()
       }
    return render(request, 'home.html', context)

@login_required(login_url='signin')
def single(request,movie_id):
    #video={Database.objects.all()}
    context = {
       'movie':Database.objects.get(id=movie_id),
       'profile':Profile.objects.all()
       }
    return render(request, 'single.html', context)


# Create your views here.
def home1(request):
    context = {}
    return render(request, 'home1.html', context)


def signup(request):
    form = registration()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        myuser = User.objects.create_user(username, email, password1)
        myuser.Username = username
        myuser.Email = email
        myuser.save()

        messages.success(request, 'account created success' + username)

        return redirect('signin')
    return render(request, 'signup.html', {'form': form})


def signin(request):
    form = registration()
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'incorrect user')

    return render(request, 'signin.html', {'form': form})


def signUp1(request):
    form = registration()
    if request.method == 'POST':
        form = registration(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request, 'thank for create account success \t' + user)
            return redirect('signin')
    return render(request, 'signUp1.html', {'form': form})


def movies(request):
    context = {}
    return render(request, 'Movies.html', context)
