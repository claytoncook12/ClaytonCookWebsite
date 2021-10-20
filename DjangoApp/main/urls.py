from django.urls import path
from main import views

app_name = 'tunes'
urlpatterns = [
    path('', views.home, name='home'),
    path('music/', views.music_home, name='music_home'),
]