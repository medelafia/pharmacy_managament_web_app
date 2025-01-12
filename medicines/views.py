from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from . import models

# Create your views here.
def index(request) : 
    medicines = models.Medicine.objects.all() 
    return render(request , "medicines/index.html" , {"medicines" : medicines }) 

def addTemplate(request) :
    return render(request , "medicines/addMedicine.html") 

def add(request) : 
    if request["name"] and request["category"] and request["price"] and request["stock"] and request["requires_prescription"] : 
        return HttpResponseRedirect("/medicines")
    else : 
        return HttpResponseRedirect("/medicines/add/")