# Generated by Django 5.1.2 on 2024-10-22 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='farmer',
        ),
    ]
