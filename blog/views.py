from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .import forms

# Create your views here.

def blog_lists(request):
    blogLists = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogLists' : blogLists})

def blog_content(request, slug):
    blogContent = Blog.objects.get(blog_slug = slug)
    return render(request, 'blog/blog_content.html', {'blogContent':blogContent})

@login_required(login_url='/')
def blog_create(request):
    if request.method == "POST":
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.blog_author = request.user
            instance.save()
            return redirect('blog:lists')
    else:
        form = forms.CreateBlog()
    return render(request, 'blog/blog_create.html', {'form':form})