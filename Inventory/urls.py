from django.urls import path

from Inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name="index"),
    path('logging_in/', views.logging_in, name='logging_in'),
    path('logging_out/', views.logging_out, name="logging_out"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/summary/', views.summary_tables, name='summary'),
    path('dashboard/summary/export_csv', views.export_csv, name="export_to_csv"),
    path('dashboard/inventory/', views.inventory, name='inventory'),
    path('dashboard/inventory/condura', views.inventory_condura, name="inventory_condura"),
    path('dashboard/inventory/carrier', views.inventory_carrier, name="inventory_carrier"),
    path('dashboard/inventory/kelvinator', views.inventory_kelvinator, name="inventory_kelvinator"),
    path('dashboard/inventory/edit_stocks', views.stocks, name="edit_stocks"),
    path('dashboard/inventory/edit_stocks/search_item', views.search_item, name="search_item"),
    path('dashboard/inventory/edit_stocks/get_stock', views.get_stock, name="get_stock"),
    path('dashboard/inventory/edit_stocks/update', views.update, name="update"),
]

