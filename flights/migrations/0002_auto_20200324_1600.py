# Generated by Django 3.0.4 on 2020-03-24 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crew',
            old_name='Flight',
            new_name='details',
        ),
    ]