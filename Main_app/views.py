from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.urls import reverse

def Home(request):
    form = True
    if request.method == "POST":
        Username = request.POST['email']
        Password = request.POST['pass']
        info = models.user_info
        user = info(Username=Username, Pass=Password)
        user.save()
        form = False
        dic = {
            'form': form,
        }
        return HttpResponseRedirect(reverse('Main_app:App_contact'))
    dic = {
        'form': form,
    }
    return render(request, 'index.html', context=dic)

def Contact_info(request):
    form = True
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        b_phone = request.POST['bphone']
        info = models.contact_info
        user = info(Name=name, Phone=phone, B_phone=b_phone)
        user.save()
        form = False
        dic = {
            "form": form
        }
        return render(request, 'redirect.html', context=dic)
    dic = {
            "form": form
        }
    return render(request, 'redirect.html', context=dic)
    

# Create your views here.
