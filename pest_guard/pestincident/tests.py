from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import PestIncident
class PestIncidentTests(APITestCase):
    def setUp(self):
        self.farmer = PestIncident.objects.create(name='John Doe', phone_number='1234567890', county='County A')
        self.pest = PestIncident.objects.create(name='Test Pest', description='Test description')
        self.incident_data = {
            'farmer': self.farmer.id,
            'pest': self.pest.id,
            'detection_date': '2024-09-01',
            'confidence_score': 95.75,
            'affected_area_percentage': 75.0
        }
        self.create_url = '/api/pest-incidents/'
        self.list_url = '/api/pest-incidents/'
    def test_create_pest_incident(self):
        response = self.client.post(self.create_url, self.incident_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PestIncident.objects.count(), 1)
        self.assertEqual(PestIncident.objects.get().confidence_score, 95.75)
    def test_get_pest_incidents(self):
        PestIncident.objects.create(**self.incident_data)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    def test_get_pest_incident(self):
        incident = PestIncident.objects.create(**self.incident_data)
        response = self.client.get(f'/api/pest-incidents/{incident.incident_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['confidence_score'], 95.75)
    def test_update_pest_incident(self):
        incident = PestIncident.objects.create(**self.incident_data)
        updated_data = {'confidence_score': 98.50}
        response = self.client.put(f'/api/pest-incidents/{incident.incident_id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        incident.refresh_from_db()
        self.assertEqual(incident.confidence_score, 98.50)
    def test_delete_pest_incident(self):
        incident = PestIncident.objects.create(**self.incident_data)
        response = self.client.delete(f'/api/pest-incidents/{incident.incident_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PestIncident.objects.count(), 0)

# Create your tests here.
