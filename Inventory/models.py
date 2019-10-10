
from django.db import models

# Create your models here.


class ModelType(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self):
        return str(self.type)

class AirconType(models.Model):
    aircon_type = models.CharField(max_length=25)


    def __str__(self):
        return str(self.aircon_type)

class Aircon(models.Model):
    model_type = models.ForeignKey(ModelType, on_delete=models.DO_NOTHING)
    aircon_type = models.ForeignKey(AirconType, on_delete=models.DO_NOTHING)
    stocks = models.IntegerField()
    model_number = models.CharField(max_length=255)
