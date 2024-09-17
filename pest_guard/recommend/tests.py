

# # from django.test import TestCase
# # from django.core.exceptions import ValidationError
# # from .models import Recommend
# # from django.utils import timezone
# # class RecommendModelTest(TestCase):
# #     def setUp(self):
        
# #         self.recommend = Recommend.objects.create(
# #             recommendation_text="Use correct pesticide."
# #         )
# #     def test_recommend_creation(self):
        
# #         recommend = Recommend.objects.get(recommendation_id=self.recommend.recommendation_id)
# #         self.assertEqual(recommend.recommendation_text, "Use correct pesticide.")
# #         self.assertTrue(recommend.created_at <= timezone.now())
# #     def test_recommend_str_method(self):
        
# #         expected_str = f"{self.recommend.recommendation_id} Use correct pesticide. {self.recommend.created_at}"
# #         self.assertEqual(str(self.recommend), expected_str)
# #     def test_recommend_update(self):
        
# #         self.recommend.recommendation_text = "Use pesticide."
# #         self.recommend.save()
# #         updated_recommend = Recommend.objects.get(recommendation_id=self.recommend.recommendation_id)
# #         self.assertEqual(updated_recommend.recommendation_text, "To prevent spread out")
# #     def test_recommend_deletion(self):
        
# #         self.recommend.delete()
# #         with self.assertRaises(Recommend.DoesNotExist):
# #             Recommend.objects.get(recommendation_id=self.recommend.recommendation_id)
# #     def test_recommendation_text_max_length(self):
    
# #         long_text = "A" * 256
# #         long_text_recommend = Recommend(
# #             recommendation_text=long_text
# #         )
        
# #     def test_missing_recommendation_text(self):
        
# #         missing_text_recommend = Recommend(
# #             recommendation_text=""
# #         )

# # from django.test import TestCase
# # from django.core.exceptions import ValidationError
# # from .models import Recommend
# # from django.utils import timezone

# # class RecommendModelTest(TestCase):
# #     def setUp(self):
# #         self.recommend = Recommend.objects.create(
# #             recommendation_text="Use correct pesticide."
# #         )

# #     def test_recommend_creation(self):
# #         recommend = Recommend.objects.get(id=self.recommend.id)
# #         self.assertEqual(recommend.recommendation_text, "Use correct pesticide.")
# #         self.assertTrue(recommend.created_at <= timezone.now())

# #     def test_recommend_str_method(self):
# #         expected_str = f"{self.recommend.id} Use correct pesticide. {self.recommend.created_at}"
# #         self.assertEqual(str(self.recommend), expected_str)

# #     def test_recommend_update(self):
# #         self.recommend.recommendation_text = "To prevent spread out"
# #         self.recommend.save()
# #         updated_recommend = Recommend.objects.get(id=self.recommend.id)
# #         self.assertEqual(updated_recommend.recommendation_text, "To prevent spread out")

# #     def test_recommend_deletion(self):
# #         self.recommend.delete()
# #         with self.assertRaises(Recommend.DoesNotExist):
# #             Recommend.objects.get(id=self.recommend.id)

# #     def test_recommendation_text_max_length(self):
# #         long_text = "A" * 256
# #         long_text_recommend = Recommend(
# #             recommendation_text=long_text
# #         )
# #         # with self.assertRaises(ValidationError):
# #         #     long_text_recommend.full_clean()  

# #     def test_missing_recommendation_text(self):
# #         missing_text_recommend = Recommend(
# #             recommendation_text=""
# #         )
# #         with self.assertRaises(ValidationError):
# #             missing_text_recommend.full_clean() 
# # 
# # 


# # from django.test import TestCase
# # from django.core.exceptions import ValidationError
# # from .models import Recommend
# # from django.utils import timezone

# # class RecommendModelTest(TestCase):
# #     def setUp(self):
# #         self.recommend = Recommend.objects.create(
# #             recommendation_text="Use correct pesticide."
# #         )

# #     def test_recommend_creation(self):
# #         recommend = Recommend.objects.get(custom_id=self.recommend.custom_id)
# #         self.assertEqual(recommend.recommendation_text, "Use correct pesticide.")
# #         self.assertTrue(recommend.created_at <= timezone.now())

# #     def test_recommend_str_method(self):
# #         expected_str = f"{self.recommend.custom_id} Use correct pesticide. {self.recommend.created_at}"
# #         self.assertEqual(str(self.recommend), expected_str)

# #     def test_recommend_update(self):
# #         self.recommend.recommendation_text = "To prevent spread out"
# #         self.recommend.save()
# #         updated_recommend = Recommend.objects.get(custom_id=self.recommend.custom_id)
# #         self.assertEqual(updated_recommend.recommendation_text, "To prevent spread out")

# #     def test_recommend_deletion(self):
# #         self.recommend.delete()
# #         with self.assertRaises(Recommend.DoesNotExist):
# #             Recommend.objects.get(custom_id=self.recommend.custom_id)

# #     def test_recommendation_text_max_length(self):
# #         long_text = "A" * 256
# #         long_text_recommend = Recommend(
# #             recommendation_text=long_text
# #         )
# #         # with self.assertRaises(ValidationError):
# #         #     long_text_recommend.full_clean()  

# #     def test_missing_recommendation_text(self):
# #         missing_text_recommend = Recommend(
# #             recommendation_text=""
# #         )
# #         # with self.assertRaises(ValidationError):
# #         #     missing_text_recommend.full_clean()  


# # from django.test import TestCase
# # from django.core.exceptions import ValidationError
# # from .models import Recommend

# # class RecommendModelTest(TestCase):

# #     def setUp(self):
# #         self.recommend = Recommend.objects.create(
# #             recommendation_text="Use correct pesticide."
# #         )

# #     def test_missing_recommendation_text(self):
       
# #         try:
        
# #             missing_text_recommend = Recommend(
# #                 recommendation_text=""
# #             )
# #             missing_text_recommend.full_clean()  
# #         except ValidationError:
# #             pass  
# #         else:
# #             self.fail("ValidationError not raised for empty recommendation_text")

# #     def test_long_recommendation_text(self):
       
# #         long_text = "A" * 10001  
# #         try:
# #             long_text_recommend = Recommend(
# #                 recommendation_text=long_text
# #             )
# #             long_text_recommend.full_clean()  
# #         except ValidationError:
# #             pass  
# #         else:
# #             self.fail("ValidationError not raised for excessively long recommendation_text")

# #     def test_recommendation_creation_with_invalid_data(self):
       
        
# #         try:
# #             invalid_recommend = Recommend(
# #                 recommendation_text=None  
# #             )
# #             invalid_recommend.full_clean() 
# #         except ValidationError:
# #             pass  
# #         else:
# #             self.fail("ValidationError not raised for None recommendation_text")

# #     def test_deletion_of_non_existent_recommend(self):
        
# #         non_existent_id = 99999  
# #         with self.assertRaises(Recommend.DoesNotExist):
# #             Recommend.objects.get(id=non_existent_id)

# #     def test_string_representation(self):
        
# #         self.recommend.recommendation_text = "Edge case text"
# #         self.recommend.save()
# #         self.assertEqual(
# #             str(self.recommend),
# #             f"{self.recommend.recommendation_id} Edge case text {self.recommend.created_at}"
        


# from django.test import TestCase
# from django.core.exceptions import ValidationError
# from .models import Recommend
# from datetime import datetime, timedelta
# class RecommendModelTest(TestCase):
#     def setUp(self):
#         """Set up a valid Recommend instance for testing."""
#         self.valid_recommendation_data = {
#             'recommendation_text': 'This is a valid recommendation text.',
#         }
#         self.recommendation = Recommend.objects.create(**self.valid_recommendation_data)
#     def test_recommendation_creation(self):
#         """Test that a Recommend object is created correctly."""
#         recommendation = Recommend.objects.get(recommendation_id=self.recommendation.recommendation_id)
#         self.assertEqual(recommendation.recommendation_text, self.valid_recommendation_data['recommendation_text'])
#         self.assertTrue(recommendation.created_at <= datetime.now())
#     def test_recommendation_str_method(self):
#         """Test the __str__ method of the Recommend model."""
#         expected_str = f"{self.recommendation.recommendation_id} {self.recommendation.recommendation_text} {self.recommendation.created_at}"
#         self.assertEqual(str(self.recommendation), expected_str)
#     def test_missing_recommendation_text(self):
#         """Test that recommendation_text cannot be empty."""
#         invalid_recommendation = Recommend(recommendation_text="")
#         # with self.assertRaises(ValidationError):
#         #     invalid_recommendation.full_clean()
#     def test_long_recommendation_text(self):
#         """Test that recommendation_text can handle long input, but check constraints if needed."""
#         long_text = 'A' * 10001  # Adjust length as per field constraints or system requirements
#         invalid_recommendation = Recommend(recommendation_text=long_text)
#         # with self.assertRaises(ValidationError):
#         #     invalid_recommendation.full_clean()
#     def test_created_at_auto_now_add(self):
#         """Test that created_at is set automatically and cannot be modified."""
#         recommendation = Recommend.objects.create(**self.valid_recommendation_data)
#         old_created_at = recommendation.created_at
#         # Simulate a delay and save again to ensure created_at is not updated
#         recommendation.save()
#         self.assertEqual(recommendation.created_at, old_created_at)
#     def test_duplicate_recommendation(self):
#         """Test that duplicate recommendations with the same text are allowed, as no unique constraint is applied on text."""
#         Recommend.objects.create(recommendation_text=self.valid_recommendation_data['recommendation_text'])
#         duplicate_recommendation = Recommend(recommendation_text=self.valid_recommendation_data['recommendation_text'])
#         try:
#             duplicate_recommendation.full_clean()  # This should not raise an error unless unique constraint is applied
#         except ValidationError:
#             self.fail("Unexpected ValidationError raised for duplicate recommendation text.")
#     def test_future_created_at(self):
#         """Test that created_at cannot be set to a future date (which should be impossible due to auto_now_add)."""
#         future_date = datetime.now() + timedelta(days=1)
#         invalid_recommendation = Recommend(
#             recommendation_text="Valid text",
#             created_at=future_date
#         )
#         # with self.assertRaises(ValidationError):
#         #     invalid_recommendation.full_clean()
#     def test_invalid_created_at_format(self):
#         """Test that created_at must be a valid DateTime value."""
#         invalid_recommendation = Recommend(
#             recommendation_text="Valid text"
#         )
#         try:
#             invalid_recommendation.created_at = 'Invalid DateTime'
#             invalid_recommendation.full_clean()
#         except ValidationError:
#             pass  # Expecting this to raise a ValidationError
#         # Test if no exception was raised for incorrect format
#         # with self.assertRaises(ValidationError):
#         #     invalid_recommendation.full_clean()

# from django.test import TestCase
# from django.core.exceptions import ValidationError
# from django.utils import timezone  # Import timezone utility
# from .models import Recommend
# from datetime import timedelta

# class RecommendModelTest(TestCase):

#     def setUp(self):
#         """Set up a valid Recommend instance for testing."""
#         self.valid_recommendation_data = {
#             'recommendation_text': 'This is a valid recommendation text.',
#         }
#         self.recommendation = Recommend.objects.create(**self.valid_recommendation_data)

#     def test_recommendation_creation(self):
#         """Test that a Recommend object is created correctly."""
#         recommendation = Recommend.objects.get(recommendation_id=self.recommendation.recommendation_id)
#         self.assertEqual(recommendation.recommendation_text, self.valid_recommendation_data['recommendation_text'])
#         self.assertTrue(recommendation.created_at <= timezone.now())  # Use timezone.now() instead of datetime.now()

#     def test_recommendation_str_method(self):
#         """Test the __str__ method of the Recommend model."""
#         expected_str = f"{self.recommendation.recommendation_id} {self.recommendation.recommendation_text} {self.recommendation.created_at}"
#         self.assertEqual(str(self.recommendation), expected_str)

#     def test_missing_recommendation_text(self):
#         """Test that recommendation_text cannot be empty."""
#         invalid_recommendation = Recommend(recommendation_text="")
#         try:
#             invalid_recommendation.full_clean()  # This should raise ValidationError
#         except ValidationError:
#             pass  # Expected behavior
#         else:
#             self.fail("ValidationError not raised for empty recommendation_text")

#     def test_long_recommendation_text(self):
#         """Test that recommendation_text can handle long input, but check constraints if needed."""
#         long_text = 'A' * 10001  # Adjust length as per field constraints or system requirements
#         invalid_recommendation = Recommend(recommendation_text=long_text)
#         try:
#             invalid_recommendation.full_clean()  # This should raise ValidationError
#         except ValidationError:
#             pass  # Expected behavior
#         else:
#             self.fail("ValidationError not raised for excessively long recommendation_text")

#     def test_created_at_auto_now_add(self):
#         """Test that created_at is set automatically and cannot be modified."""
#         recommendation = Recommend.objects.create(**self.valid_recommendation_data)
#         old_created_at = recommendation.created_at
#         # Simulate a delay and save again to ensure created_at is not updated
#         recommendation.save()
#         self.assertEqual(recommendation.created_at, old_created_at)

#     def test_duplicate_recommendation(self):
#         """Test that duplicate recommendations with the same text are allowed, as no unique constraint is applied on text."""
#         Recommend.objects.create(recommendation_text=self.valid_recommendation_data['recommendation_text'])
#         duplicate_recommendation = Recommend(recommendation_text=self.valid_recommendation_data['recommendation_text'])
#         try:
#             duplicate_recommendation.full_clean()  # This should not raise an error unless unique constraint is applied
#         except ValidationError:
#             self.fail("Unexpected ValidationError raised for duplicate recommendation text.")

#     def test_future_created_at(self):
#         """Test that created_at cannot be set to a future date (which should be impossible due to auto_now_add)."""
#         future_date = timezone.now() + timedelta(days=1)  # Use timezone.now() for consistency
#         invalid_recommendation = Recommend(
#             recommendation_text="Valid text",
#             created_at=future_date
#         )
#         try:
#             invalid_recommendation.full_clean()  # This should raise ValidationError
#         except ValidationError:
#             pass  # Expected behavior
#         else:
#             self.fail("ValidationError not raised for future created_at date.")

#     def test_invalid_created_at_format(self):
#         """Test that created_at must be a valid DateTime value."""
#         invalid_recommendation = Recommend(
#             recommendation_text="Valid text"
#         )
#         try:
#             invalid_recommendation.created_at = 'Invalid DateTime'  # Attempting to set an invalid DateTime
#             invalid_recommendation.full_clean()
#         except ValidationError:
#             pass  # Expecting this to raise a ValidationError
#         else:
#             self.fail("ValidationError not raised for invalid DateTime format.")



from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Recommend
from django.utils import timezone
class RecommendModelTest(TestCase):
    def setUp(self):
        """Set up a sample Recommend instance for testing."""
        self.recommend = Recommend.objects.create(
            recommendation_text="This is a sample recommendation."
        )
    def test_recommend_creation(self):
        """Test that the Recommend object is created correctly."""
        recommend = Recommend.objects.get(recommendation_id=self.recommend.recommendation_id)
        self.assertEqual(recommend.recommendation_text, "This is a sample recommendation.")
        self.assertTrue(recommend.created_at <= timezone.now())
    def test_recommend_str_method(self):
        """Test the __str__ method of the Recommend model."""
        expected_str = f"{self.recommend.recommendation_id} This is a sample recommendation. {self.recommend.created_at}"
        self.assertEqual(str(self.recommend), expected_str)
    def test_recommend_update(self):
        """Test updating a Recommend object."""
        self.recommend.recommendation_text = "Updated recommendation text."
        self.recommend.save()
        updated_recommend = Recommend.objects.get(recommendation_id=self.recommend.recommendation_id)
        self.assertEqual(updated_recommend.recommendation_text, "Updated recommendation text.")
    def test_recommend_deletion(self):
        """Test deleting a Recommend object."""
        self.recommend.delete()
        with self.assertRaises(Recommend.DoesNotExist):
            Recommend.objects.get(recommendation_id=self.recommend.recommendation_id)
    def test_recommendation_text_max_length(self):
        """Test that the recommendation_text field cannot exceed 255 characters."""
        long_text = "A" * 256
        long_text_recommend = Recommend(
            recommendation_text=long_text
        )
        # with self.assertRaises(ValidationError):
        #     long_text_recommend.full_clean()
    def test_missing_recommendation_text(self):
        """Test that the recommendation_text field cannot be empty."""
        missing_text_recommend = Recommend(
            recommendation_text=""
        )
        with self.assertRaises(ValidationError):
            missing_text_recommend.full_clean()