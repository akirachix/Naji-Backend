from django.test import TestCase
from .models import PestIncident
from django.core.exceptions import ValidationError
from datetime import date

class PestIncidentModelTests(TestCase):

    def test_create_valid_pest_incident(self):
        incident = PestIncident.objects.create(
            leaf_status='Healthy',
            affected_area_percentage=0.0,
            detection_date=date.today()
        )
        self.assertEqual(incident.leaf_status, 'Healthy')
        self.assertEqual(incident.affected_area_percentage, 0.0)
        self.assertEqual(incident.detection_date, date.today())

    def test_str_representation(self):
        incident = PestIncident.objects.create(
            leaf_status='Infected',
            affected_area_percentage=25.0,
            detection_date=date.today()
        )
        self.assertEqual(str(incident), f"Incident {incident.incident_id} -leaf_status: Infected")

    def test_affected_area_percentage_validation(self):
        incident = PestIncident(
            leaf_status='Infected',
            affected_area_percentage=-5.0,  
            detection_date=date.today()
        )
        with self.assertRaises(ValidationError):
            incident.full_clean()  

    def test_affected_area_percentage_zero(self):
        incident = PestIncident(
            leaf_status='Healthy',
            affected_area_percentage=0.0,
            detection_date=date.today()
        )
        try:
            incident.full_clean()  #
        except ValidationError:
            self.fail("ValidationError raised when affected_area_percentage is zero.")

    def test_required_fields(self):
        with self.assertRaises(ValidationError):
            PestIncident(affected_area_percentage=10.0, detection_date=date.today()).full_clean()
        with self.assertRaises(ValidationError):
            PestIncident(leaf_status='Infected', affected_area_percentage=10.0).full_clean()
        with self.assertRaises(ValidationError):
            PestIncident(leaf_status='Infected', detection_date=date.today()).full_clean()

                