from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('music/', views.music_home, name='music_home'),
]