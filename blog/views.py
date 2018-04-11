from django.shortcuts import render
from .models import *

# Create your views here.

def blog_lists(request):
    blogLists = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogLists' : blogLists})

def blog_content(request, slug):
    blogContent = Blog.objects.get(blog_slug = slug)
    return render(request, 'blog/blog_content.html', {'blogContent':blogContent})