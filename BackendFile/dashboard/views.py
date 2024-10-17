from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from BackendApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import MenuItemForm

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
# @login_required
# def forms(request):
#     # menu = MenuItem.objects.order_by('-id')
#     # context = {
#     #     'menu' : menu
#     # }
#     return render(request,"form.html")


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





@login_required
def charts(request):
    return render(request,"chart.html")
@login_required
def widgets(request):
    return render(request,"widget.html")