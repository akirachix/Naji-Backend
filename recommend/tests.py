
from django.test import TestCase
from .models import Recommend
from django.core.exceptions import ValidationError
from datetime import datetime

class RecommendModelTest(TestCase):

    def setUp(self):
        self.recommendation = Recommend.objects.create(
            recommendation_text='This is a valid recommendation text'
        )

    def test_recommend_creation(self):
        recommendation = Recommend.objects.get(recommendation_id=self.recommendation.recommendation_id)
        self.assertEqual(recommendation.recommendation_text, 'This is a valid recommendation text')
        self.assertIsNotNone(recommendation.created_at)  # Checks that created_at is not None
        self.assertEqual(str(recommendation), f"{recommendation.recommendation_id} {recommendation.recommendation_text} {recommendation.created_at}")

    def test_empty_recommendation_text(self):
        recommendation = Recommend(recommendation_text='')
        with self.assertRaises(ValidationError):
            recommendation.full_clean() 

    def test_very_long_recommendation_text(self):
        recommendation = Recommend(recommendation_text='x' * 10001)  
        try:
            recommendation.full_clean()
        except ValidationError as e:
            self.assertIn('recommendation_text', e.message_dict)  

    def test_invalid_created_at(self):
        recommendation = Recommend(
            recommendation_text='Valid recommendation',
            created_at='invalid-date-format'  
        )
        with self.assertRaises(ValidationError):  
            recommendation.full_clean()  
    def test_blank_recommendation_text(self):
        recommendation = Recommend(recommendation_text='')
        with self.assertRaises(ValidationError):
            recommendation.full_clean()