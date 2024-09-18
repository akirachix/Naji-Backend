from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Recommend
from django.utils import timezone
class RecommendModelTest(TestCase):
    def setUp(self):
        
        self.recommend = Recommend.objects.create(
            recommendation_text="Use correct pesticide."
        )
    def test_recommend_creation(self):
        
        recommend = Recommend.objects.get(recommendation_id=self.recommend.recommendation_id)
        self.assertEqual(recommend.recommendation_text, "Use correct pesticide.")
        self.assertTrue(recommend.created_at <= timezone.now())
    def test_recommend_str_method(self):
        
        expected_str = f"{self.recommend.recommendation_id} Use correct pesticide. {self.recommend.created_at}"
        self.assertEqual(str(self.recommend), expected_str)
    def test_recommend_update(self):
        
        self.recommend.recommendation_text = "Use correct pesticide."
        self.recommend.save()
        updated_recommend = Recommend.objects.get(recommendation_id=self.recommend.recommendation_id)
        self.assertEqual(updated_recommend.recommendation_text, "Use correct pesticide.")
    def test_recommend_deletion(self):
        
        self.recommend.delete()
        with self.assertRaises(Recommend.DoesNotExist):
            Recommend.objects.get(recommendation_id=self.recommend.recommendation_id)
    def test_recommendation_text_max_length(self):
    
        long_text = "A" * 256
        long_text_recommend = Recommend(
            recommendation_text=long_text
        )
     
    def test_missing_recommendation_text(self):
        
        missing_text_recommend = Recommend(
            recommendation_text=""
        )
        with self.assertRaises(ValidationError):
            missing_text_recommend.full_clean()