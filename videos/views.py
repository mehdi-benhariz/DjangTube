from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required 
from .forms import CommentForm,VideoForm
from django.db.models import Q

# Create your views here.
def index(request):
    return redirect() 

@login_required
def show(request):
    video_list=Video.objects.all()
    all_comments=Comment.objects.all()
    query = request.GET.get("q")
    if(query):
        video_list = video_list.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)
            ).distinct()

    context={
        'video_list':video_list,
        'all_comments':all_comments,
    }
    return render(request,'index.html',context)


def detail(request,id):
    instance = get_object_or_404(Video,id=id)
    comment_list = Comment.objects.filter(writer=instance.owner).order_by('-date')
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            aux = comment_form.save(commit=False)
            aux.writer = request.user
            aux.save()
            return redirect('detail')
    context={
        "instance":instance,
        "comment_list":comment_list,
        "comment_form" :comment_form
    }
    return render(request,"detail.html",context)

def like(request,id):
    instance = get_object_or_404(Video,id=id)
    instance.likes = instance.likes +1
    instance.save()
    return redirect ('videos:detail',id=id)

def update(request,id):
    video_form = VideoForm()
    instance = get_object_or_404(Video,id=id)
    if request.method == 'POST':
        video_form = VideoForm(request.POST or None,request.FILES or None,instance=instance )
        if video_form.is_valid():
            aux = video_form(commit=False)
            aux.save()
            return redirect("accounts:profile")
    context ={
        "video_form":VideoForm,
    }

    return render(request,"profile.html",context)

def delete(request,id):
    instance= get_object_or_404(Video,id=id)
    instance.delete()
    return redirect("accounts:profile")
