

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User as DjangoUser
from .models import User
class UserModelTest(TestCase):
    def setUp(self):
    
        self.django_user = DjangoUser.objects.create_user(
            username="Mary John",
            password="#mary2002",
            email="maryjohn@gmail.com"
        )
        self.user = User.objects.create(
            user=self.django_user,
            first_name="John",
            last_name="Doe",
            email="johndoe@gmail.com",
            password="password123"
        )
    def test_user_creation(self):
        
        user = User.objects.get(user=self.django_user)
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "johndoe@gmail.com")
    def test_user_str_method(self):
        
        expected_str = "John Doe (johndoe@gmail.com)"
        self.assertEqual(str(self.user), expected_str)
    def test_user_update(self):
        
        self.user.first_name = "Jane"
        self.user.last_name = "Smith"
        self.user.save()
        updated_user = User.objects.get(user=self.django_user)
        self.assertEqual(updated_user.first_name, "Jane")
        self.assertEqual(updated_user.last_name, "Smith")
    def test_user_deletion(self):
        
        self.user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(user=self.django_user)
    def test_unique_email(self):
        
        duplicate_django_user = DjangoUser.objects.create_user(
            username="Cynthia",
            password="#cybnthia2002",
            email="cynthia@gmail.com"  
        )
        User.objects.create(
            user=duplicate_django_user,
            first_name="Alice",
            last_name="Wonderland",
            email="alicewonderland@gmail.com", 
            password="newpassword"
        )
        
        duplicate_email_user = User(
            user=DjangoUser.objects.create_user(
                username="NewUser",
                password="#newpassword2002",
                email="cynthia@gmail.com"  
            ),
            first_name="Another",
            last_name="Person",
            email="cynthia@gmail.com",
            password="anotherpassword"
        )
       
    def test_first_name_max_length(self):
        
        long_first_name = "A" * 31
        long_first_name_user = User(
            user=self.django_user,
            first_name=long_first_name,  
            last_name="Doe",
            email="anotheremail@gmail.com",
            password="password123"
        )
      
    def test_last_name_max_length(self):
        
        long_last_name = "B" * 31
        long_last_name_user = User(
            user=self.django_user,
            first_name="John",
            last_name=long_last_name,  
            email="anotheremail@gmail.com",
            password="password123"
        )
     
    def test_password_max_length(self):
    
        long_password_user = User(
            user=self.django_user,
            first_name="John",
            last_name="Doe",
            email="johndoe@gmail.com",
            password="A" * 17  
        )
      
    def test_missing_email(self):
        
        missing_email_user = User(
            user=self.django_user,
            first_name="John",
            last_name="Doe",
            email="", 
            password="password123"
        )
       
