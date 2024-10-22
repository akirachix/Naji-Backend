from django.db import models

class Device(models.Model):
    device_id = models.AutoField(primary_key=True)  
    device_status = models.CharField(max_length=20)
    last_updated = models.DateField()

    def __str__(self):
        return f"{self.device_id}"


