# Generated by Django 3.0.4 on 2020-03-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0008_auto_20200328_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pilot',
            name='Passenegers_limit',
        ),
        migrations.AddField(
            model_name='flight',
            name='Passengers_limit',
            field=models.IntegerField(default=0),
        ),
    ]
