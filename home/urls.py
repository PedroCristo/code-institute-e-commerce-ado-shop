from django.contrib import admin
from django.urls import path
from . import views
from django.urls import reverse

urlpatterns = [
    path('', views.index, name='home')
]

