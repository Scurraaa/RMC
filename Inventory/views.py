from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'Inventory/index.html')



def logging_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    auth = User.objects.get(username=username)
    user = authenticate(request, username=username, password=password)
    request.session['user'] = username

    context = {
        'users': user
    }

    if user is not None:
        login(request, user)
        if auth.is_superuser:
            return render(request, 'Inventory/dashboard.html', context)
        else:
            return HttpResponseRedirect(reverse('inventory:index'))
    else:
        return render(request, 'Inventory/index.html', {})


def summary_tables(request):
    return render(request, 'Inventory/tables.html')


def inventory(request):
    return render(request, 'Inventory/inventory.html')

