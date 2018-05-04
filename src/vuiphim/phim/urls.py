from django.urls import path, re_path
from django.conf.urls import handler404, handler500

from . import views

urlpatterns = [
    # path('', views.list_paste_template, name = 'list_paste_template'),
    path('', views.index, name = 'index_page'),    
    path('video/', views.video, name = 'video_page'),
]