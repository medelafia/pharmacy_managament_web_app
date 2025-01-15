from django.db import models

# Create your models here.
class Client(models.Model) : 
    name = models.CharField("name" , max_length=150)
    email= models.CharField("email" ,max_length=100) 
    phone = models.IntegerField("phone") 