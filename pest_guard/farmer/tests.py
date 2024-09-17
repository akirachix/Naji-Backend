from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Farmer
class FarmerModelTest(TestCase):
    def setUp(self):
    
        self.farmer = Farmer.objects.create(
            farmer_id=1,
            farmer_name="John Doe",
            farmer_county="Mombasa",  
            farmer_phone_number="1234567890"
        )
    def test_farmer_creation(self):
        
        farmer = Farmer.objects.get(farmer_id=1)
        self.assertEqual(farmer.farmer_name, "John Doe")
        self.assertEqual(farmer.farmer_county, "Mombasa") 
        self.assertEqual(farmer.farmer_phone_number, "1234567890")
    def test_farmer_str_method(self):
        
        self.assertEqual(str(self.farmer), "John Doe")
    def test_farmer_update(self):
        
        self.farmer.farmer_name = "Jane Doe"
        self.farmer.save()
        updated_farmer = Farmer.objects.get(farmer_id=1)
        self.assertEqual(updated_farmer.farmer_name, "Jane Doe")
    def test_farmer_deletion(self):
    
        self.farmer.delete()
        with self.assertRaises(Farmer.DoesNotExist):
            Farmer.objects.get(farmer_id=1)
    def test_farmer_phone_number_length(self):
        
        valid_farmer = Farmer(
            farmer_id=2,
            farmer_name="Alice Smith",
            farmer_county="Kisumu",
            farmer_phone_number="0987654321"
        )
        try:
            valid_farmer.full_clean()
        except ValidationError:
            self.fail("Validation failed for a valid phone number")
        invalid_farmer = Farmer(
            farmer_id=3,
            farmer_name="8",
            farmer_county="Pokot",
            farmer_phone_number="12345"
        )
       
        
        invalid_farmer_long = Farmer(
            farmer_id=4,
            farmer_name="Eve Black",
            farmer_county="Bungoma",
            farmer_phone_number="123456789012345"
        )
     
      
    def test_farmer_name_max_length(self):
    
        long_name_farmer = Farmer(
            farmer_id=5,
            farmer_name="A" * 21,
            farmer_county="Busia",
            farmer_phone_number="1234567890"
        )
     
    def test_farmer_phone_number_non_numeric(self):
        
        non_numeric_farmer = Farmer(
            farmer_id=6,
            farmer_name="Chris Green",
            farmer_county="Kwale",
            farmer_phone_number="abcd123456"
        )
       
    def test_missing_farmer_phone_number(self):
        
        missing_phone_farmer = Farmer(
            farmer_id=7,
            farmer_name="Pat White",
            farmer_county="Eldoret",
            farmer_phone_number=""
        )
        with self.assertRaises(ValidationError):
            missing_phone_farmer.full_clean()
 
 
