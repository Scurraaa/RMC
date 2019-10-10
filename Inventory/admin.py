from django.contrib import admin
from Inventory.models import ModelType, Aircon, AirconType
# Register your models here.

admin.site.register(ModelType)
admin.site.register(Aircon)
admin.site.register(AirconType)