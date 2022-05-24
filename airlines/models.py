from django.db import models
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Airline(TimeStampedModel):
    name = models.CharField(max_length=250)
    symbol = models.CharField(max_length=10)
    logo = models.ImageField(upload_to="")
    base_url = models.URLField()
    username = models.CharField(max_length=125)
    password = models.CharField(max_length=125)

    def __str__(self):
        return self.name
