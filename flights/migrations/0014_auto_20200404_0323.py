# Generated by Django 3.0.4 on 2020-04-03 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0013_auto_20200404_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Passenger_flight', to='flights.Flight'),
        ),
    ]
