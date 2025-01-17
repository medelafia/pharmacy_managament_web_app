from django.contrib import admin
from django.urls import path , include 
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , include("pharmacy_app.urls"))
    ]
