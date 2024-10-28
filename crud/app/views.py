from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import usercollection
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>App is running...</h1>")

def add_user(request):
    records = {
        "firstname":"remy",
        "lastname":"gitoli"
    }
    usercollection.insert_one(records)
    return HttpResponse("New user is added")

def getusers(request):
    users= usercollection.find()
    return HttpResponse(users)

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')