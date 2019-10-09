from django.urls import path

from Inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.logging_in, name='logging_in'),
    path('dashboard/summary/', views.summary_tables, name='summary'),
    path('dashboard/inventory/', views.inventory, name='invetory'),
]

