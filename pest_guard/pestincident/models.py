from django.db import models
from django.db import models

class PestIncident(models.Model):
    incident_id = models.AutoField(primary_key=True)
   
    detection_date = models.DateField()
    confidence_score = models.DecimalField(max_digits=5, decimal_places=2)
    affected_area_percentage = models.FloatField()
    def __str__(self):
        return f"Incident {self.incident_id} - Pest: {self.pest.name} - Farmer: {self.farmer.name}"
# Create your models here.
