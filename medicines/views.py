from django.shortcuts import render , HttpResponse , HttpResponseRedirect , get_object_or_404 
from . import models
from .forms import MedicineForm 

# Create your views here.
def index(request) : 
    medicines = models.Medicine.objects.all() 
    return render(request , "medicines/index.html" , {"medicines" : medicines , "message" : request.GET.get("message")}) 

def addTemplate(request) :
    form = MedicineForm() 
    error = request.GET.get("error")

    return render(request , "medicines/addMedicine.html" , {"form" : form , "error" : error}) 

def add(request) : 
    form = MedicineForm(request.POST)
    if request.method == "POST" :
        form = MedicineForm(request.POST) 
        if form.is_valid() : 
            form.save() 
            return HttpResponseRedirect("/medicines" , {"message success"})
        else : 
            return HttpResponseRedirect("/medicines/add/" , {"error" : "not valid information" , "form" : form })
    else : 
        return render(request , "medicines/addMedicine.html" , { "form" : form })

def delete(request) : 
    if(request.method == "POST") :
        if request.POST.get("id") : 
            medicine = models.Medicine.objects.get(id = request.POST.get("id")) 
            medicine.delete() 
            return HttpResponseRedirect("/medicines")


def update(request) : 
    medicine = get_object_or_404(models.Medicine , id=request.GET.get("id")) 
    if request.method == "POST" :
        form = MedicineForm(request.POST , instance=medicine ) 
        if form.is_valid() : 
            form.save() 
            return HttpResponseRedirect("/medicines")
    else : 
        return render(request , "medicines/updateMedicine.html" , {"form" : MedicineForm(instance=medicine)}) 