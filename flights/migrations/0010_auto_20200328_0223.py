# Generated by Django 3.0.4 on 2020-03-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0009_auto_20200328_0213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domestic',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='international',
            name='Date',
        ),
        migrations.AddField(
            model_name='domestic',
            name='Destination_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='domestic',
            name='Starting_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='international',
            name='Destination_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='international',
            name='Starting_date',
            field=models.DateTimeField(null=True),
        ),
    ]
