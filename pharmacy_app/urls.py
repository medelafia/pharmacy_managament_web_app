from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index , name="index"),
    path('medicines/', views.indexMedicine , name="indexMedicine"),
    path("medicines/add/" , views.addMedicine , name="addMedicine") , 
    path("medicines/delete/", views.deleteMedicine , name="deleteMedicine"), 
    path("medicines/update/" , views.updateMedicine , name="updateMedicine") , 
    path('clients/', views.indexClient , name="indexClient"),
    path("clients/add/" , views.addClient , name="addClient") , 
    path("clients/delete/", views.deleteClient , name="deleteClient"), 
    path("clients/update/" , views.updateClient , name="updateClient") , 
    path('sales/', views.indexSale , name="indexSale"),
    path("sales/add/" , views.addSale , name="addSale") , 
    path("sales/delete/", views.deleteSale , name="deleteSale"), 
    path("sales/update/" , views.updateSale , name="updateSale") , 
] 