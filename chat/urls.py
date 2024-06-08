from django.urls import path
from . import views


urlpatterns = [
    path('userlogin', views.userlogin, name='userlogin'),
    path('', views.home, name='home'),
     path('<str:room>/', views.room, name='room'),
     path('checkview' , views.checkview, name='checkview'),
     path('send', views.send, name='send'),
     path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]






