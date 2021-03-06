# Generated by Django 4.0.4 on 2022-05-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passangers', '0004_reservation_air_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='flight_class',
            field=models.CharField(blank=True, max_length=125),
        ),
        migrations.AddField(
            model_name='reservation',
            name='flight_no',
            field=models.CharField(blank=True, max_length=125),
        ),
        migrations.AddField(
            model_name='reservation',
            name='pnr_code',
            field=models.CharField(blank=True, max_length=125, verbose_name='شناسه رزرو'),
        ),
    ]
