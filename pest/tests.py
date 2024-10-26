from django.test import TestCase
from django.test import TestCase
from .models import Pest
from django.core.exceptions import ValidationError

class PestModelTests(TestCase):
    def test_create_pest_without_required_fields(self):
        with self.assertRaises(ValidationError):
            pest = Pest(pest_name='Test Pest')
            pest.full_clean()  

    def test_create_pest_with_negative_pest_id(self):
        pest = Pest(pest_id=-1, pest_name='Test Pest', pest_description='Description')
       

    def test_create_pest_with_long_name(self):
        long_name = 'A' * 26  
        pest = Pest(pest_id=1, pest_name=long_name, pest_description='Description')
     

    def test_create_pest_with_long_description(self):
        long_description = 'A' * 256 
        pest = Pest(pest_id=1, pest_name='Test Pest', pest_description=long_description)
     

    def test_create_duplicate_pest_id(self):
        Pest.objects.create(pest_id=1, pest_name='Aphid', pest_description='Causes holes in leaves')
        duplicate_pest = Pest(pest_id=1, pest_name='Coffee borer', pest_description='Causes harmful to leaves')
      



 