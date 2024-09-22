from django.urls import path
from posts import views

urlpatterns = [
    path('', views.home, name='index'),
    path('posts/', views.posts, name='posts'),
    path('about/', views.about, name='about')
]