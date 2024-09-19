from django.db import models

# Create your models here.


class Farmer(models.Model):
    farmer_id = models.AutoField()
    farmer_name = models.CharField(max_length=20)
    farmer_county = models.CharField()
    farmer_phone_number=models.CharField(max_length=10)
    
    

    def __str__(self):
        return f"{self.farmer_name}"

 