from django.shortcuts import render , HttpResponse , HttpResponseRedirect , get_object_or_404 
from . import models
from .forms import ClientForm

def index(request):
    clients = models.Client.objects.all()
    return render(request, "clients/index.html", {"clients": clients, "message": request.GET.get("message")})

def addTemplate(request):
    form = ClientForm()
    error = request.GET.get("error")
    return render(request, "clients/addClient.html", {"form": form, "error": error})

def add(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/clients?message=Client added successfully")
        else:
            return HttpResponseRedirect("/clients/add/?error=Invalid information")
    else:
        form = ClientForm()
        return render(request, "clients/addClient.html", {"form": form})

def delete(request):
    if request.method == "POST" and request.POST.get("id"):
        client = get_object_or_404(models.Client, id=request.POST.get("id"))
        client.delete()
        return HttpResponseRedirect("/clients?message=Client deleted successfully")

def update(request):
    client = get_object_or_404(models.Client, id=request.GET.get("id"))
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/clients?message=Client updated successfully")
    else:
        form = ClientForm(instance=client)
    return render(request, "clients/updateClient.html", {"form": form})

