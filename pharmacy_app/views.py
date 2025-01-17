from django.shortcuts import render,HttpResponse , HttpResponseRedirect , get_object_or_404
from . import models
from . import forms
import datetime  


def index(request) : 
    return render(request , "index.html")
# Create your views here.
def indexMedicine(request) : 
    medicines = models.Medicine.objects.all() 
    return render(request , "indexMedicines.html" , {"medicines" : medicines , "message" : request.GET.get("message")}) 


def addMedicine(request) : 
    form =   forms.MedicineForm(request.POST)
    if request.method == "POST" :
        form = forms.MedicineForm(request.POST) 
        if form.is_valid() : 
            form.save() 
            return HttpResponseRedirect("/medicines" , {"message success"})
        else : 
            return HttpResponseRedirect("/medicines/add/" , {"error" : "not valid information" , "form" : form })
    else : 
        return render(request , "addMedicine.html" , { "form" : form })

def deleteMedicine(request) : 
    if(request.method == "POST") :
        if request.POST.get("id") : 
            medicine = models.Medicine.objects.get(id = request.POST.get("id")) 
            medicine.delete() 
            return HttpResponseRedirect("/medicines")


def updateMedicine(request) : 
    medicine = get_object_or_404(models.Medicine , id=request.GET.get("id")) 
    if request.method == "POST" :
        form = forms.MedicineForm(request.POST , instance=medicine ) 
        if form.is_valid() : 
            form.save() 
            return HttpResponseRedirect("/medicines")
    else : 
        return render(request , "updateMedicine.html" , {"form" :forms.MedicineForm(instance=medicine)}) 


def indexClient(request):
    clients = models.Client.objects.all()
    return render(request, "indexClients.html", {"clients": clients, "message": request.GET.get("message")})

def addTemplate(request):
    form = forms.ClientForm()
    error = request.GET.get("error")
    return render(request, "addClient.html", {"form": form, "error": error})

def addClient(request):
    if request.method == "POST":
        form = forms.ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/clients?message=Client added successfully")
        else:
            return HttpResponseRedirect("/clients/add/?error=Invalid information")
    else:
        form = forms.ClientForm()
        return render(request, "addClient.html", {"form": form})

def deleteClient(request):
    if request.method == "POST" and request.POST.get("id"):
        client = get_object_or_404(models.Client, id=request.POST.get("id"))
        client.delete()
        return HttpResponseRedirect("/clients?message=Client deleted successfully")

def updateClient(request):
    client = get_object_or_404(models.Client, id=request.GET.get("id"))
    if request.method == "POST":
        form = forms.ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/clients?message=Client updated successfully")
    else:
        form = forms.ClientForm(instance=client)
    return render(request, "updateClient.html", {"form": form})

def indexSale(request) : 
    sales = models.Sale.objects.all()
    return render(request , "indexSales.html" , { "sales" : sales }) 

def addSale(request) : 
    if request.method == "POST" :
        form = forms.SaleForm(request.POST) 
        if form.is_valid() : 
            sale_instance = form.save(commit=False)
            sale_instance.date = datetime.datetime.now().date()
            sale_instance.save()
            return HttpResponseRedirect("/sales")
        else :
            print("not valid")
            return render(request , "addSale.html" , {'form' : form })
    else : 
        return render(request , "addSale.html" , {"form" : forms.SaleForm()})

def deleteSale(request) : 
        if(request.method == "POST") :
            if request.POST.get("id") : 
                sale = models.Sale.objects.get(id = request.POST.get("id")) 
                sale.delete() 
                return HttpResponseRedirect("/sales")

def updateSale(request) : 
    sale = get_object_or_404(models.Sale , id=request.GET.get("id")) 
    if request.method == "POST" :
        form = forms.SaleForm(request.POST , instance=sale ) 
        if form.is_valid() : 
            form.save()
            return HttpResponseRedirect("/sales")
        else : 
            return render(request , "updateSale.html" , {"form" : forms.SaleForm(instance=sale)}) 
    else : 
        return render(request , "updateSale.html" , {"form" : forms.SaleForm(instance=sale)}) 