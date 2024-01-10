from .views import *
from django.contrib import admin
from django.urls import path,include

urlpatterns=[
    path('game/',main,name="game"),
    path('about/',about,name='about'),
    path('contact/',contact,name="contact"),
    path('product/',product,name="product"),
    path('remot/',remot,name="remot"),
    path('video/',video,name="video")

]