from django import forms
from .import models

class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['blog_title', 'blog_message', 'blog_slug', 'blog_thumb']
        widgets = {
            'blog_title' : forms.TextInput(attrs={'placeholder' : 'Title', 'class' : 'form-control'}),
            'blog_message' : forms.Textarea(attrs={'placeholder' : 'Message', 'class' : 'form-control'}),
            'blog_slug' : forms.TextInput(attrs={'placeholder' : 'Slug', 'class' : 'form-control'}),
            'blog_thumb' : forms.FileInput(attrs={'class' : 'btn btn-default'}),
        }