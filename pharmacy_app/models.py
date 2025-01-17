from django.db import models

class Client(models.Model) : 
    name = models.CharField("name" , max_length=150)
    email= models.CharField("email" ,max_length=100) 
    phone = models.IntegerField("phone") 

    def __str__(self):
        return self.name
    
class Medicine(models.Model) : 
    name = models.CharField("name" , max_length=150)
    category = models.CharField("category" ,max_length=100) 
    price = models.FloatField("price") 
    stock = models.IntegerField("stock") 
    requires_prescription = models.BooleanField("requires prescription") 
    def __str__(self) -> str:
        return self.name
        
class Sale(models.Model) : 
    client = models.ForeignKey( 
        Client  ,
        on_delete=models.PROTECT ,
        blank=False  
    )
    medicines = models.ManyToManyField(Medicine  , related_name='sales') 
    date = models.DateField("date") 


