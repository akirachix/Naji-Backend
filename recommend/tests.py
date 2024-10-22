# from django.test import TestCase
# from .models import Recommend
# from django.core.exceptions import ValidationError
# from datetime import datetime

# class RecommendModelTest(TestCase):

#     def setUp(self):
#         # Happy path - create a valid Recommend object
#         self.recommendation = Recommend.objects.create(
#             recommendation_text='This is a valid recommendation text'
#         )

#     # Happy Path Test: Ensure the Recommend creation is successful
#     def test_recommend_creation(self):
#         recommendation = Recommend.objects.get(recommendation_id=self.recommendation.recommendation_id)
#         self.assertEqual(recommendation.recommendation_text, 'This is a valid recommendation text')
#         self.assertIsNotNone(recommendation.created_at)  # Checks that created_at is not None
#         self.assertEqual(str(recommendation), f"{recommendation.recommendation_id} {recommendation.recommendation_text} {recommendation.created_at}")

#     # Unhappy Path Test: Test creation with an empty recommendation_text
#     def test_empty_recommendation_text(self):
#         recommendation = Recommend(recommendation_text='')
#         # Trigger validation manually and check for ValidationError
#         with self.assertRaises(ValidationError):
#             recommendation.full_clean()  # This will trigger validation

#     # Unhappy Path Test: Test a very long recommendation_text (if there's a limit)
#     def test_very_long_recommendation_text(self):
#         recommendation = Recommend(recommendation_text='x' * 10001)  # Assuming there's a reasonable text length limit
#         # Trigger validation manually and check for ValidationError if length exceeds limits
#         try:
#             recommendation.full_clean()
#         except ValidationError as e:
#             self.assertIn('recommendation_text', e.message_dict)  # Expect a ValidationError for the text field

#     # Unhappy Path Test: Ensure invalid created_at raises an error (this is unlikely unless forced)
#     def test_invalid_created_at(self):
#         recommendation = Recommend(
#             recommendation_text='Valid recommendation',
#             created_at='invalid-date-format'  # Setting an invalid datetime format
#         )
#         with self.assertRaises(ValueError):  # Expect a ValueError for invalid datetime
#             recommendation.save()

#     # Unhappy Path Test: Check that recommendation_text is not empty (validation in form logic can add more robustness)
#     def test_blank_recommendation_text(self):
#         recommendation = Recommend(recommendation_text='')
#         with self.assertRaises(ValidationError):
#             recommendation.full_clean()
from django.test import TestCase
from .models import Recommend
from django.core.exceptions import ValidationError
from datetime import datetime

class RecommendModelTest(TestCase):

    def setUp(self):
        # Happy path - create a valid Recommend object
        self.recommendation = Recommend.objects.create(
            recommendation_text='This is a valid recommendation text'
        )

    # Happy Path Test: Ensure the Recommend creation is successful
    def test_recommend_creation(self):
        recommendation = Recommend.objects.get(recommendation_id=self.recommendation.recommendation_id)
        self.assertEqual(recommendation.recommendation_text, 'This is a valid recommendation text')
        self.assertIsNotNone(recommendation.created_at)  # Checks that created_at is not None
        self.assertEqual(str(recommendation), f"{recommendation.recommendation_id} {recommendation.recommendation_text} {recommendation.created_at}")

    # Unhappy Path Test: Test creation with an empty recommendation_text
    def test_empty_recommendation_text(self):
        recommendation = Recommend(recommendation_text='')
        # Trigger validation manually and check for ValidationError
        with self.assertRaises(ValidationError):
            recommendation.full_clean()  # This will trigger validation

    # Unhappy Path Test: Test a very long recommendation_text (if there's a limit)
    def test_very_long_recommendation_text(self):
        recommendation = Recommend(recommendation_text='x' * 10001)  # Assuming there's a reasonable text length limit
        # Trigger validation manually and check for ValidationError if length exceeds limits
        try:
            recommendation.full_clean()
        except ValidationError as e:
            self.assertIn('recommendation_text', e.message_dict)  # Expect a ValidationError for the text field

    # Unhappy Path Test: Ensure invalid created_at raises a validation error
    def test_invalid_created_at(self):
        recommendation = Recommend(
            recommendation_text='Valid recommendation',
            created_at='invalid-date-format'  # Setting an invalid datetime format
        )
        # Trigger validation manually to raise ValidationError
        with self.assertRaises(ValidationError):  # Expect a ValidationError
            recommendation.full_clean()  # This will validate the fields and raise an error

    # Unhappy Path Test: Check that recommendation_text is not blank (validation in form logic can add more robustness)
    def test_blank_recommendation_text(self):
        recommendation = Recommend(recommendation_text='')
        with self.assertRaises(ValidationError):
            recommendation.full_clean()  # This will trigger validation
