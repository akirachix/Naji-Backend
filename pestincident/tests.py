from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import PestIncident
from datetime import date

class PestIncidentModelTest(TestCase):

    def setUp(self):
        # Setting up data for the happy path test
        self.pest_incident = PestIncident.objects.create(
            leaf_status="Healthy",
            affected_area_percentage=20.5,
            confidence_score=0.9,
            detection_date=date.today()
        )

    def test_pestincident_creation_happy_path(self):
        """
        Happy Path: Test if the PestIncident is created successfully
        """
        incident = PestIncident.objects.get(incident_id=self.pest_incident.incident_id)
        self.assertEqual(incident.leaf_status, "Healthy")
        self.assertEqual(incident.affected_area_percentage, 20.5)
        self.assertEqual(incident.confidence_score, 0.9)
        self.assertEqual(incident.detection_date, date.today())

    def test_pestincident_creation_unhappy_path_missing_leaf_status(self):
        """
        Unhappy Path: Missing leaf_status should raise an IntegrityError
        """
        with self.assertRaises(IntegrityError):
            PestIncident.objects.create(
                affected_area_percentage=15.0,
                confidence_score=0.8,
                detection_date=date.today()
            )

    def test_pestincident_creation_unhappy_path_negative_percentage(self):
        """
        Unhappy Path: Negative affected_area_percentage should raise a ValidationError
        """
        incident = PestIncident(
            leaf_status="Infected",
            affected_area_percentage=-5.0,  # Invalid value
            confidence_score=0.85,
            detection_date=date.today()
        )
        with self.assertRaises(ValidationError):
            incident.full_clean()  # Call validation explicitly to trigger ValidationError

    def test_pestincident_creation_unhappy_path_missing_confidence_score(self):
        """
        Unhappy Path: Missing confidence_score should raise an IntegrityError
        """
        with self.assertRaises(IntegrityError):
            PestIncident.objects.create(
                leaf_status="Infected",
                affected_area_percentage=10.0,
                detection_date=date.today()
            )

    def test_str_method(self):
        """
        Test the __str__ method of PestIncident
        """
        self.assertEqual(
            str(self.pest_incident),
            f"Incident {self.pest_incident.incident_id} - detection_date: {self.pest_incident.detection_date} - confidence_score: {self.pest_incident.confidence_score}"
        )

