from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from BackendApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import MenuItemForm
from .serializers import MenuItemSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

@login_required
def dashboard(request):
    return render(request,"index.html")
@login_required
def table(request):
    # user = User.objects.filter(is_staff=False)
    user = User.objects.order_by('-id')
    context ={ 
        'user':user
    }
    return render(request,"table.html",context)


# Create and Read Menu
def create_menu_item(request):
    form = MenuItemForm()
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        form.save()
        form = MenuItemForm()
        return redirect('form')
    data = MenuItem.objects.all()

    context={
        'form': form,
        'data': data,
    }

    return render(request, 'form.html', context)




# Delete Menu
def delete(request, id):
    a= MenuItem.objects.get(pk=id)
    a.delete()
    return redirect('form')

# Update Menu
def update(request, id):
    if request.method == 'POST':
        data = MenuItem.objects.get(pk=id)
        form = MenuItemForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('form')
    else:
        data = MenuItem.objects.get(pk=id)
        form = MenuItemForm(instance=data)
    context={
        'form': form,
    }
    return render(request, 'update.html', context)





@login_required
def charts(request):
    return render(request,"chart.html")
@login_required
def widgets(request):
    return render(request,"widget.html")


# Display Menu Data in React

class MenuItemDisplay(APIView):
    def get(self, request):
        menuitem = MenuItem.objects.all()
        menuserializer = MenuItemSerializer(menuitem, many=True)
        return JsonResponse(menuserializer.data, safe=False)






