from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Aircon
from .resources import AirconResource

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
        'users': auth
    }

    if user is not None:
        login(request, user)
        if auth.is_superuser:
            return HttpResponseRedirect(reverse('inventory:dashboard'))
        else:
            return HttpResponseRedirect(reverse('inventory:index'))
    else:
        return render(request, 'Inventory/index.html', {})


def summary_tables(request):
    username = request.session['user']
    user = User.objects.get(username=username)
    aircon = Aircon.objects.all()
    context = {
        'users': user,
        'aircon': aircon
    }
    return render(request, 'Inventory/tables.html', context)


def dashboard(request):
    username = request.session['user']
    user = User.objects.get(username=username)
    context = {
        'users': user
    }
    return render(request, 'Inventory/dashboard.html', context)


def inventory(request):

    username = request.session['user']
    user = User.objects.get(username=username)
    condura_stock_wrac = Aircon.objects.get(model_number = 'WCONX008EA2')
    condura_stock_hw = Aircon.objects.get(model_number = '13-42KCR018')
    condura_stock_pe = Aircon.objects.get(model_number = 'FP-53CCA024313')
    carrier_stock_wrac = Aircon.objects.get(model_number = 'WCARG006EE')
    carrier_stock_hw = Aircon.objects.get(model_number = 'FP-42CVUR016-703')
    carrier_stock_pe = Aircon.objects.get(model_number = 'FB-53CCF-LDS024308')
    kelvinator_stock_wrac = Aircon.objects.get(model_number = 'WKELW010EC')
    context = {
        'users': user,
        'condura_wrac': condura_stock_wrac,
        'condura_hw': condura_stock_hw,
        'condura_pe':condura_stock_pe,
        'carrier_wrac': carrier_stock_wrac,
        'carrier_hw': carrier_stock_hw,
        'carrier_pe': carrier_stock_pe,
        'kelvinator_wrac': kelvinator_stock_wrac
    }
    return render(request, 'Inventory/inventory.html', context)

def inventory_carrier(request):

    username = request.session['user']
    user = User.objects.get(username=username)
    carrier_stock_wrac = Aircon.objects.get(model_number = 'WCARG006EE')
    carrier_stock_hw = Aircon.objects.get(model_number = 'FP-42CVUR016-703')
    carrier_stock_pe = Aircon.objects.get(model_number = 'FB-53CCF-LDS024308')
    context = {
        'users': user,
        'carrier_wrac': carrier_stock_wrac,
        'carrier_hw': carrier_stock_hw,
        'carrier_pe': carrier_stock_pe
    }
    return render(request, 'Inventory/inventory_carrier.html', context)

def inventory_condura(request):

    username = request.session['user']
    user = User.objects.get(username=username)
    condura_stock_wrac = Aircon.objects.get(model_number = 'WCONX008EA2')
    condura_stock_hw = Aircon.objects.get(model_number = '13-42KCR018')
    condura_stock_pe = Aircon.objects.get(model_number = 'FP-53CCA024313')
    context = {
        'users': user,
        'condura_wrac': condura_stock_wrac,
        'condura_hw': condura_stock_hw,
        'condura_pe':condura_stock_pe,
    }
    return render(request, 'Inventory/inventory_condura.html', context)

def inventory_kelvinator(request):

    username = request.session['user']
    user = User.objects.get(username=username)
    kelvinator_stock_wrac = Aircon.objects.get(model_number = 'WKELW010EC')
    context = {
        'users': user,
        'kelvinator_wrac': kelvinator_stock_wrac
    }
    return render(request, 'Inventory/inventory_kelvinator.html', context)


def stocks(request):
    username = request.session['user']
    user = User.objects.get(username=username)
    aircon = Aircon.objects.all()
    condura_stock_wrac = Aircon.objects.get(model_number = 'WCONX008EA2')
    condura_stock_hw = Aircon.objects.get(model_number = '13-42KCR018')
    condura_stock_pe = Aircon.objects.get(model_number = 'FP-53CCA024313')
    carrier_stock_wrac = Aircon.objects.get(model_number = 'WCARG006EE')
    carrier_stock_hw = Aircon.objects.get(model_number = 'FP-42CVUR016-703')
    carrier_stock_pe = Aircon.objects.get(model_number = 'FB-53CCF-LDS024308')
    kelvinator_stock_wrac = Aircon.objects.get(model_number = 'WKELW010EC')
    context = {
        'users': user,
        'aircon': aircon,
        'condura_wrac': condura_stock_wrac,
        'condura_hw': condura_stock_hw,
        'condura_pe':condura_stock_pe,
        'carrier_wrac': carrier_stock_wrac,
        'carrier_hw': carrier_stock_hw,
        'carrier_pe': carrier_stock_pe,
        'kelvinator_wrac': kelvinator_stock_wrac
    }
    return render(request, 'Inventory/edit_stocks.html', context)


def search_item(request):
    model_number = request.POST.get('select_model_number')
    print(model_number)

    return render(request, 'Inventory/edit_stocks.html')


def get_stock(request):
    model_number = request.POST.get('model_number')
    print(model_number)
    aircon = Aircon.objects.get(model_number=model_number)
    stocks = aircon.stocks
    data = {
        "stocks": stocks
    }
    return JsonResponse(data)


def update(request):
    model_number = request.POST.get('model_number')
    stock = request.POST.get('stock')
    aircon = Aircon.objects.get(model_number=model_number)
    aircon.stocks = stock
    aircon.save()
    data = {
        "status": "success"
    }
    return JsonResponse(data)

def export_csv(request):
    aircon_resources = AirconResource()
    dataset = aircon_resources.export()
    response = HttpResponse(dataset.csv, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="Aircon_Inventory.csv"'
    return response


def logging_out(request):
    del request.session['user']
    logout(request)
    return HttpResponseRedirect(reverse('inventory:index'))

