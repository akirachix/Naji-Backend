# Generated by Django 5.1.2 on 2024-10-22 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pestincident', '0003_alter_pestincident_leaf_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pestincident',
            name='device',
        ),
    ]
