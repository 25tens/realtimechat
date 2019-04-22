"""justchat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from chat import views
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('chat.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
#   path('add/post/', views.add-post,name='add_post'),
#    path('edit/post/<int:post_id>/', views.edit-post,name='edit_post'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
