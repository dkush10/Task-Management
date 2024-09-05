from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout

# Create your views here.

def login_(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # user=authenticate(username=username,password=password)
        
        try:
            user=User.objects.get(username=username)
        except:
            return HttpResponse("Username does not exist!")
        if user.password==password:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password!")
    return render(request,'login_form.html')

def register_(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        print(username,email,password)
        user=User.objects.create(username=username,email=email, password=password)
        # user.set_password(password)
        # user.save()
        return redirect('login_')
    return render(request,'register.html')

def logout_(request):
    logout(request)
    return redirect('login_')
     
