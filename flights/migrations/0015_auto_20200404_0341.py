# Generated by Django 3.0.4 on 2020-04-03 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0014_auto_20200404_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Passenger_flight', to='flights.Flight'),
        ),
    ]