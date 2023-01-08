
from django.shortcuts import render
from .models import Place
from .models import Client


def demo(request):
    ob = Place.objects.all()
    obj = Client.objects.all()
    return render(request, "index.html", {'result': ob, 'res': obj})
