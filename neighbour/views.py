from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as log_in
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django_registration.forms import RegistrationForm
import cloudinary, cloudinary.api,cloudinary.uploader
from .models import Users, Contact, Business, Neighbourhood, Post


def register(request):
    form = UserCreationForm()#RegistrationForm(data=request.POST)
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            new_user = Users(name = user.username)
            new_user.save()
            return redirect('login')
    return render(request, 'auth/register.html', {"form": form})
def login(request):
    form = AuthenticationForm(data=request.POST)
    context = {"form":form}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            log_in(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect")
            context.update({"messages": messages})
            return redirect('login')
    else: 
        return render(request, 'auth/login.html', context)   

def logout_me(request):
    logout(request)
    messages.info(request, "You have logged out successfully!")
    return redirect("login")

def home(request):
    # project = [project for project in Project.objects.all()]
    # projects = [(project, [project.ratings]) for project in project] 
    return render(request, 'home/base.html', {'projects': ""})

def business(request):
    businesses = Business.objects.all()
    return render(request, 'home/business.html', {'businesses': businesses})
def neighbourhood(request):
    current_user = request.user
    neighbourhood = current_user.neighbourhood
    return render(request, 'home/neighbor_hood.html', {'neighbourhood': neighbourhood})
def post(request):
    posts = Post.objects.all()
    return render(request, 'home/posts.html', {'posts': posts})

