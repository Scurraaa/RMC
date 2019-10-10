from django.urls import path

from Inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name="index"),
    path('logging_in/', views.logging_in, name='logging_in'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/summary/', views.summary_tables, name='summary'),
    path('dashboard/inventory/', views.inventory, name='inventory'),
    path('dashboard/inventory/condura', views.inventory_condura, name="inventory_condura"),
    path('dashboard/inventory/carrier', views.inventory_carrier, name="inventory_carrier"),
    path('dashboard/inventory/kelvinator', views.inventory_kelvinator, name="inventory_kelvinator")
]

