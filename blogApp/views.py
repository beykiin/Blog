from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import authenticate, login as lgn, logout as lgt
import datetime
from .models import *
# Create your views here.

def index(request):
    posts=Posts.objects.all()
    context={
         "posts":posts
    }
    return render(request,"index.html",context)
def register(request):
    form=UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("index")
    context={
        "form":form
    }
    return render(request,"register.html",context)

def login(request):
    if request.method=="POST":
        userName=request.POST["username"]
        userpass=request.POST["userpass"]
        user=authenticate(username=userName,password=userpass)
        if user is not None:
                lgn(request,user)
                return redirect("login")
        else:
             return render(request,"login.html")
    return render(request,"login.html")

def logout(request):
     lgt(request)
     return redirect('index')

def newPost(request):
     form=NewPost()
     if request.method=="POST":
          form=NewPost(request.POST,request.FILES)
          if form.is_valid:
               post=form.save(commit=False)
               post.postOwner=request.user
               post.published=datetime.datetime.now()
               post.save()
               return redirect("index")
     context={
          "form":form
     }
     return render(request,"posts.html",context)
def postDetail(request,id):
    post=Posts.objects.filter(id=id)
    comments=Comment.objects.filter(commentPost=id)
    form=NewComment()
    context={
        "post":post,
        "comments":comments,
        "form":form
    }
    print(post)
    if request.method=="POST":
        form=NewComment(request.POST)
        if form.is_valid:
            comment=form.save(commit=False)
            comment.published=datetime.datetime.now()
            comment.commentPost=id
            comment.commentOwner=request.user
            comment.save()
        return render(request,"postdetails.html",context)
             

    return render(request,"postdetails.html",context)