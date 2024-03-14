from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        
        if User.objects.filter(username=username).exists():
            print('username is taken!')
        elif User.objects.filter(email=email).exists():
            print('email is taken!')
        else:
            user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname, email=email)
            user.save();
            return redirect('login')
        
        return redirect('/')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def home(request):
    return render(request,'home.html')