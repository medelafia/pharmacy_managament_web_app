from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index , name="index"),
    path('addMedicine/' , views.addTemplate , name="addMedicine") , 
    path("add/" , views.add , name="add")
]