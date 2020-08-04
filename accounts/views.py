from django.shortcuts import render,redirect
from .forms import CreateUserForm
from videos.forms import VideoForm
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required 

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('login')
    context ={'registration_form':form}
    return render(request,'register.html',context )

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
             auth_login(request,user)
             return redirect('index')
    return render(request,'login.html')

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def profile(request):
    context ={
        "video_form":VideoForm
    }
    return render(request,"profile.html",context)    