from django.conf import settings
from django.db import models
from django.db.models import Sum
from django_extensions.db.models import TimeStampedModel

user = settings.AUTH_USER_MODEL


# Create your models here.


class Reservation(TimeStampedModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="reservation", verbose_name='کاربر')
    fly_code = models.CharField(max_length=125, verbose_name='کد پرواز')
    source = models.CharField(max_length=125, verbose_name='مبذا')
    target = models.CharField(max_length=125, verbose_name='مقصد')
    # price = models.IntegerField(verbose_name='')
    date = models.CharField(max_length=125, verbose_name='تاریخ')
    email = models.EmailField()
    phone_number = models.CharField(max_length=125, verbose_name='شماره تماس')
    paid = models.BooleanField(default=False, verbose_name='پرداخت شده؟')

    def get_total_cost(self):
        return self.passengers.filter.aggregate(Sum("price"))

    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزروها'


class Passenger(TimeStampedModel):
    GENDER = (
        ("مرد", "مرد"),
        ("زن", "زن"),
    )
    en_name = models.CharField(max_length=125, )
    en_family = models.CharField(max_length=125, verbose_name='نام لایتن')
    gender = models.CharField(max_length=12, choices=GENDER, verbose_name='جنسیت')
    national_code = models.CharField(max_length=10, verbose_name='کد ملی')
    ir_name = models.CharField(max_length=125, verbose_name='نام')
    ir_family = models.CharField(max_length=125, verbose_name='نام خانوادگی')
    day = models.PositiveSmallIntegerField(verbose_name='ماه')
    month = models.CharField(max_length=25, verbose_name='سال')
    year = models.PositiveSmallIntegerField(verbose_name='روز')
    reserve = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="passengers", verbose_name='رزرو کننده'
    )
    price = models.IntegerField(verbose_name='قیمت')
    age = models.CharField(max_length=125, verbose_name='سن')

    def __str__(self):
        return f"{self.ir_name} {self.ir_family}"

    def en_full_name(self):
        return f"{self.en_name} {self.en_family}"

    class Meta:
        verbose_name = 'مسافر'
        verbose_name_plural = 'مسافر ها'
