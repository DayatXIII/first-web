from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.accounts_views, name='lists'),
    url(r'^login/$', views.login_views, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
