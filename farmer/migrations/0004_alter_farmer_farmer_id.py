# Generated by Django 5.1.1 on 2024-09-25 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmer", "0003_alter_farmer_farmer_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farmer",
            name="farmer_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
