from django.db import models

# Create your models here.
class Medicine(models.Model) : 
    name = models.CharField("name" , max_length=150)
    category = models.CharField("category" ,max_length=100) 
    price = models.FloatField("price") 
    stock = models.IntegerField("stock") 
    requires_prescription = models.BooleanField("requires prescription") 

