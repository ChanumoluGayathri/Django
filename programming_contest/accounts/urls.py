from django.contrib import admin
from django.urls import path, include
from accounts.views import *
from accounts import views

urlpatterns = [
    path('main', views.greetings),
    path('main/run', views.runcode),
]
