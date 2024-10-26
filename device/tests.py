
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from .models import Device
from datetime import date

class DeviceModelTest(TestCase):

    def setUp(self):
        self.device = Device.objects.create(
            device_status='Active',
            last_updated=date.today()
        )

    def test_device_creation(self):
        device = Device.objects.get(device_id=self.device.device_id)
        self.assertEqual(device.device_status, 'Active')
        self.assertEqual(device.last_updated, date.today())
        self.assertEqual(str(device), str(device.device_id))

    def test_invalid_device_status(self):
        device = Device(device_status='', last_updated=date.today())
        with self.assertRaises(ValidationError):
            device.full_clean() 

    def test_device_without_last_updated(self):
        with self.assertRaises(IntegrityError):
            Device.objects.create(device_status='Inactive', last_updated=None)

    def test_device_status_too_long(self):
        device = Device(device_status='A' * 21, last_updated=date.today())
        with self.assertRaises(ValidationError):
            device.full_clean()  

    def test_invalid_last_updated_date(self):
        device = Device(device_status='Inactive', last_updated='invalid-date')
        with self.assertRaises(ValidationError):
            device.full_clean() 