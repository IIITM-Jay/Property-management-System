from django.shortcuts import render,redirect

# Create your views here.

from .forms import AssetForm,AssetSearchForm
from .models import Asset
from django.shortcuts import get_object_or_404
from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponse
import csv
import zerosms

# Create your views here.
def home(request):
    title=''
    context = {
    "title":title,
    }
    return render(request, "home.html",context)
def base(request):
    title=''
    context = {
    "title":title,
    }
    return render(request, "base.html",context)
def Property_entry(request):
    title = 'Add Property'
    form = AssetForm(request.POST or None) 
    if form.is_valid():
        form.save()
        form.save(commit=False)
        form.save_m2m()
        messages.success(request, 'Your details have been "Successfully Saved" into the database.')
        return redirect('Property_entry')
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "Property_entry.html",context)
def Property_list(request):
     title = 'List of all Properties'
     queryset = Property.objects.all()
     context = {
         "title": title,
         "queryset": queryset,
     }
     return render(request, "Property_list.html",context)
def Property_edit(request, id=None):    
    instance = get_object_or_404(Asset, id=id)
    form = AssetForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save()
        form.save_m2m()
        messages.success(request,'Your details have been "Successfully Saved" into the database.')
        return redirect('Property_list')
    context = {
            "title": 'Edit ' + str(instance.Property_type),
            "instance": instance,
            "form": form,
        }
    return render(request, "Property_entry.html", context)
def Property_list(request):
    title = 'List of all Properties'
    form = AssetSearchForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
        }
    if request.method == 'POST':
            queryset = Asset.objects.all().filter(Property_type__icontains=form['Property_type'].value(),location__icontains=form['location'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    if form['export_to_CSV'].value()==True:
         response = HttpResponse(content_type='text/csv')
         response['Content-Disposition'] = 'attachment; filename="Property list.csv"'
         writer = csv.writer(response)
         writer.writerow(["Property_type", "Property_name","location"])   
         instance = queryset
         for row in instance:
             writer.writerow([row.Property_type,row.Property_name,row.location])
         return response
    return render(request, "Property_list.html",context)

def sms(request):
	if "username" in request.POST and "password" in request.POST and "sendto" in request.POST and "message" in request.POST:
		username = request.POST["username"]
		password = request.POST["password"]
		sendto = request.POST["sendto"]
		msg = request.POST["message"]
		zerosms.sms(phno=username,passwd=password, receivernum=sendto,message=msg)
		return HttpResponse("Send")
	return HttpResponse(render(request,"sms.html",{}))












