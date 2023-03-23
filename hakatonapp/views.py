from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

def home(request):
    return render(request, "hakatonapp/home.html")

def about(request):
    return render(request, "hakatonapp/about.html")

def contact(request):
    return render(request, "hakatonapp/contact.html")

def contact(request):
    return render(request, "hakatonapp/login.html")

def hello_there(request, name):
    return render(
        request,
        'hakatonapp/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

