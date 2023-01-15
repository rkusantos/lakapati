from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


# Create your models here.
class Farm(models.Model):
    user = models.CharField(max_length=100)
    farm_name = models.CharField(max_length=100)
    longitude = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)


class FarmDetails(models.Model):
    user = models.CharField(max_length=100)
    farm_name = models.CharField(max_length=100)
    date = models.DateField()
    percentage_crop = models.CharField(max_length=5)
    image_link = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000, default='')