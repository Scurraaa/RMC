from .models import Aircon
from import_export import resources
class AirconResource(resources.ModelResource):
    class Meta:
        model = Aircon