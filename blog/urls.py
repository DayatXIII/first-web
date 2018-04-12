from django.conf.urls import url
from .import views


app_name = "blog"
urlpatterns = [
    url(r'^$', views.blog_lists, name='lists'),
    url(r'^create/$', views.blog_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.blog_content, name='contents'),
]