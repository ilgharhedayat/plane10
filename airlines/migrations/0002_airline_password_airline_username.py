# Generated by Django 4.0.4 on 2022-05-25 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("airlines", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="airline",
            name="password",
            field=models.CharField(blank=True, max_length=125),
        ),
        migrations.AddField(
            model_name="airline",
            name="username",
            field=models.CharField(blank=True, max_length=125),
        ),
    ]
