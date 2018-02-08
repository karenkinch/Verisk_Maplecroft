from django.db import models

# Create your models here.


class Countries(models.Model):
    country = models.CharField(max_length=100, blank=False)
    country_abbreviation = models.CharField(max_length=100, blank=False)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
