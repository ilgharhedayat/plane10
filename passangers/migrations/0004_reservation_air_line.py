# Generated by Django 4.0.4 on 2022-05-27 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0003_alter_airline_options_alter_airline_logo_and_more'),
        ('passangers', '0003_remove_passenger_created_remove_passenger_modified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='air_line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='air_line_reservation', to='airlines.airline'),
        ),
    ]