# Generated by Django 4.0.4 on 2022-05-27 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passangers', '0002_alter_passenger_options_alter_reservation_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='created',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='created',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='modified',
        ),
    ]