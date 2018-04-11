from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=255, verbose_name = 'Title')
    blog_message = models.TextField(verbose_name = 'Message')
    blog_date_created = models.DateTimeField(auto_now_add=True)
    blog_thumb = models.ImageField(default='default.png', blank=True, verbose_name = 'Upload Image')
    blog_slug = models.SlugField(verbose_name = 'Slug')
    blog_author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name = 'Author')

    #Return object title according to the blog's title name
    def __str__(self):
        return self.blog_title

    def blog_message_snippet(self):
        return self.blog_message[:400] + '...'
