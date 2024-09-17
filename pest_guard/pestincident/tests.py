

from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import PestIncident
from datetime import date
class PestIncidentModelTest(TestCase):
    def setUp(self):
        
        self.valid_incident_data = {
            'detection_date': date.today(),
            'confidence_score': 85.50,
            'affected_area_percentage': 25.5
        }
        self.incident = PestIncident.objects.create(**self.valid_incident_data)
    def test_incident_creation(self):
    
        incident = PestIncident.objects.get(incident_id=self.incident.incident_id)
        self.assertEqual(incident.detection_date, self.valid_incident_data['detection_date'])
        self.assertEqual(incident.confidence_score, self.valid_incident_data['confidence_score'])
        self.assertEqual(incident.affected_area_percentage, self.valid_incident_data['affected_area_percentage'])
    def test_incident_str_method(self):
    
        expected_str = f"Incident {self.incident.incident_id} - detection_date: {self.incident.detection_date} - confidence_score: {self.incident.confidence_score}"
        self.assertEqual(str(self.incident), expected_str)
    def test_confidence_score_validation(self):
        
        invalid_incident = PestIncident(
            detection_date=date.today(),
            confidence_score=105.00,
            affected_area_percentage=25.5
        )
      
    def test_affected_area_percentage_validation(self):
        
        invalid_incident = PestIncident(
            detection_date=date.today(),
            confidence_score=85.50,
            affected_area_percentage=105.0
        )
      
    def test_future_detection_date(self):
        
        future_date_incident = PestIncident(
            detection_date=date.today().replace(year=date.today().year + 1),
            confidence_score=85.50,
            affected_area_percentage=25.5
        )
     
    def test_invalid_confidence_score(self):
        
        invalid_incident = PestIncident(
            detection_date=date.today(),
            confidence_score='Invalid',
            affected_area_percentage=25.5
        )
      
    def test_invalid_affected_area_percentage(self):
        
        invalid_incident = PestIncident(
            detection_date=date.today(),
            confidence_score=85.50,
            affected_area_percentage='Invalid'
        )
      
    def test_no_detection_date(self):
        
        invalid_incident = PestIncident(
            detection_date=None,
            confidence_score=85.50,
            affected_area_percentage=25.5
        )
      
    def test_no_confidence_score(self):
        
        invalid_incident = PestIncident(
            detection_date=date.today(),
            confidence_score=None,
            affected_area_percentage=25.5
        )
      
    def test_no_affected_area_percentage(self):
        
        invalid_incident = PestIncident(
            detection_date=date.today(),
            confidence_score=85.50,
            affected_area_percentage=None
        )
     
