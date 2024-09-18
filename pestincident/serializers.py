from rest_framework import serializers
from .models import PestIncident

class PestIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PestIncident
        fields = '__all__'