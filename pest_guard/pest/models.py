from django.db import models


class Pest(models.Model):
    pest_id = models.PositiveSmallIntegerField()
    pest_name = models.CharField(max_length=25)
    pest_description = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.pest_name}"

# Create your models here.
