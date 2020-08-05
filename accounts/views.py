from django.shortcuts import render,redirect
from .forms import CreateUserForm
from videos.forms import VideoForm
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required 
from videos.models import Video

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
    if request.method == 'POST':
        video_form = VideoForm(request.POST or None,request.FILES or None )
        if video_form.is_valid():
            aux = video_form(commit=False)
            aux.save()
    my_video = Video.objects.filter(owner=request.user)
    context ={
        "video_form":VideoForm,
        "my_video" : my_video
    }
    return render(request,"profile.html",context)    