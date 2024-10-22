
from django.db import models
from django.core.validators import MinValueValidator

class PestIncident(models.Model):
    incident_id = models.AutoField(primary_key=True)
    leaf_status = models.CharField(max_length=20)
    affected_area_percentage = models.FloatField(validators=[MinValueValidator(0)])
    detection_date = models.DateField()

    def __str__(self):
        return f"Incident {self.incident_id} - detection_date: {self.detection_date} - confidence_score: {self.confidence_score}"



