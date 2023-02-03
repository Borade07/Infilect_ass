from django.db import models

# Create your models here.
from django.db import models

class WeatherInformation(models.Model):
    city_name = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    description = models.TextField()
