# Generated by Django 5.1.2 on 2024-10-22 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0003_alter_recommend_incident'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommend',
            name='incident',
        ),
    ]