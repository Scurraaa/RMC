from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from Inventory.models import ModelType, Aircon, AirconType
# Register your models here.

admin.site.register(ModelType)
admin.site.register(AirconType)

@admin.register(Aircon)
class ViewAircon(ImportExportModelAdmin):
    pass