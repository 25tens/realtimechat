from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    
   
   
#    path('add/post', views.add_post, name='add_post'),
#    path('edit/blog/^(?P<pk>\d+)/$', views.edit_blog, name='edit_blog'),
]   