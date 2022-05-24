from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

user = settings.AUTH_USER_MODEL


# Create your models here.
class Passenger(TimeStampedModel):
    GENDER = (
        ("مرد", "مرد"),
        ("زن", "زن"),
    )
    en_name = models.CharField(max_length=125)
    en_family = models.CharField(max_length=125)
    gender = models.CharField(max_length=12, choices=GENDER)
    national_code = models.CharField(max_length=10)
    ir_name = models.CharField(max_length=125)
    ir_family = models.CharField(max_length=125)
    day = models.PositiveSmallIntegerField()
    month = models.CharField(max_length=25)
    year = models.PositiveSmallIntegerField()
    reserver = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True)
    fly_code = models.CharField(max_length=125)

    def __str__(self):
        pass
