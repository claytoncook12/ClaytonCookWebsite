from django.urls import path
from tunes import views

app_name = 'tunes'
urlpatterns = [
    path('list/', views.tunes_list, name='tunes_list'),
    path('<int:pk>/', views.detail, name='detail'),
]
