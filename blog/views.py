from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})

def post_detail(request, id):
    post = Post.objects.get(id = id)
    return render(request, "detail.html", {"post": post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Veri başarıyla eklendi.")
            return redirect("/")

    else:
        form = PostForm()

    return render(request, "create.html", {"form": form})

def post_update(request, id):
    post = Post.objects.get(id = id)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, f"{post.baslik} adlı veri başarıyla güncellendi.")
            return redirect("/")
    
    else:
        form = PostForm(instance=post)
    
    return render(request, "update.html", {"form": form})

def post_delete(request, id):
    post = Post.objects.get(id = id)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Veri başarıyla silindi.")
        return redirect("/")
    
    return render(request, "delete.html", {"post": post})