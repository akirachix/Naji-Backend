# # 

# from django.test import TestCase
# from farmer.models import Farmer
# from .models import Device
# from django.utils import timezone

# class DeviceModelTest(TestCase):
    
#     def setUp(self):
#         # Create a Farmer instance for foreign key relationship
#         self.farmer = Farmer.objects.create(name='Test Farmer')

#     def test_device_status_too_long(self):
#         # Attempt to create a Device with a status that exceeds max length
#         long_status = 'a' * 21  # 21 characters, exceeding the max length
#         device = Device.objects.create(
#             device_status=long_status,
#             last_updated=timezone.now(),
#             farmer=self.farmer
#         )
#         self.assertEqual(device.device_status, long_status[:20])  # Should truncate to 20 characters

#     def test_device_creation_without_farmer(self):
#         # Attempt to create a Device without a farmer (should raise an IntegrityError)
#         with self.assertRaises(Exception):  # This should be a more specific exception
#             Device.objects.create(
#                 device_status='Active',
#                 last_updated=timezone.now()
#             )

#     def test_device_last_updated_in_future(self):
#         # Create a Device with a last_updated date in the future
#         future_date = timezone.now().date() + timezone.timedelta(days=1)
#         device = Device.objects.create(
#             device_status='Inactive',
#             last_updated=future_date,
#             farmer=self.farmer
#         )
#         self.assertEqual(device.last_updated, future_date)

#     def test_device_status_empty_string(self):
#         # Create a Device with an empty string for device_status
#         device = Device.objects.create(
#             device_status='',
#             last_updated=timezone.now(),
#             farmer=self.farmer
#         )
#         self.assertEqual(device.device_status, '')  # Should accept empty string

#     def test_device_string_representation(self):
#         # Test the string representation of the Device
#         device = Device.objects.create(
#             device_status='Active',
#             last_updated=timezone.now(),
#             farmer=self.farmer
#         )
#         self.assertEqual(str(device), str(device.device_id))  # Ensure it returns the device_id




# from django.test import TestCase
# from .models import Device
# from datetime import date

# class DeviceModelTest(TestCase):

#     def setUp(self):
#         # Set up a test device for the "happy" path
#         self.device = Device.objects.create(
#             device_status='Active',
#             last_updated=date.today()
#         )

#     # Happy Path Test: Ensure device creation is successful
#     def test_device_creation(self):
#         device = Device.objects.get(device_id=self.device.device_id)
#         self.assertEqual(device.device_status, 'Active')
#         self.assertEqual(device.last_updated, date.today())
#         self.assertEqual(str(device), str(device.device_id))

#     # Unhappy Path Test: Ensure an invalid device status raises error
#     def test_invalid_device_status(self):
#         with self.assertRaises(ValueError):
#             Device.objects.create(device_status='', last_updated=date.today())

#     # Unhappy Path Test: Ensure creation fails without last_updated
#     def test_device_without_last_updated(self):
#         with self.assertRaises(ValueError):
#             Device.objects.create(device_status='Inactive', last_updated=None)

#     # Unhappy Path Test: Ensure setting too long a status raises error
#     def test_device_status_too_long(self):
#         with self.assertRaises(ValueError):
#             Device.objects.create(device_status='A' * 21, last_updated=date.today())

#     # Unhappy Path Test: Ensure invalid date format raises error
#     def test_invalid_last_updated_date(self):
#         with self.assertRaises(ValueError):
#             Device.objects.create(device_status='Inactive', last_updated='invalid-date')

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
            device.full_clean()  # Manually trigger validation

    def test_device_without_last_updated(self):
        with self.assertRaises(IntegrityError):
            Device.objects.create(device_status='Inactive', last_updated=None)

    def test_device_status_too_long(self):
        device = Device(device_status='A' * 21, last_updated=date.today())
        with self.assertRaises(ValidationError):
            device.full_clean()  # Manually trigger validation

    def test_invalid_last_updated_date(self):
        device = Device(device_status='Inactive', last_updated='invalid-date')
        with self.assertRaises(ValidationError):
            device.full_clean()  # Manually trigger validation
