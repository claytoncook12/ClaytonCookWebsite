from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('music/', views.music_home, name='music_home'),
    path('adminlinks/', views.admin_links, name="admin_links"),
    path('dbjson/', views.dbjson, name="dbjson"),
]