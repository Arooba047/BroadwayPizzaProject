from django.shortcuts import render
from django.http import HttpResponse
from BackendApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def dashboard(request):
    return render(request,"index.html")

def table(request):
    # user = User.objects.filter(is_staff=False)
    user = User.objects.order_by('-id')
    context ={ 
        'user':user
    }
    return render(request,"table.html",context)

def forms(request):
    return render(request,"form.html")


def charts(request):
    return render(request,"chart.html")

def widgets(request):
    return render(request,"widget.html")