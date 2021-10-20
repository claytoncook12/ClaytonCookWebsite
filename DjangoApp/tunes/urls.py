from django.urls import path
from tunes import views

app_name = 'tunes'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
]
