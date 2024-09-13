from django.db import models

class Recommend(models.Model):
    # Define fields for the model
    recommendation_id = models.AutoField(primary_key=True)
    recommendation_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return a string representation of the model instance
        return f"{self.recommendation_id} {self.recommendation_text} {self.created_at}"

# Create your models here.
