from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def login(request):
    return render(request, 'login.html', {"current_user":request.user})

def register(request):
    return render(request, 'register.html')