from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

# Location Model
class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.location

# user/member manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# Members Model
class Member(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    username = None
    dob = models.DateField()
    status = models.IntegerField(default=1)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

# Dependants Model
class Dependant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    surname = models.CharField(max_length=255)
    others = models.CharField(max_length=255)
    dob = models.DateField()  # Date of Birth
    reg_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.surname} {self.others}'

# LabTests Model
class LabTest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test_name = models.CharField(max_length=255)
    test_description = models.TextField()
    test_cost = models.IntegerField()
    test_discount = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)
    more_info = models.CharField(max_length=255, blank=True, null=True)
    reg_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.test_name

# Nurses Model
class Nurse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    reg_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Nurse {self.surname}'

# NurseLabTestAllocation Model
class NurseLabTestAllocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=100)
    flag = models.CharField(max_length=20, default='active')
    reg_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Allocation {self.allocation_id} - {self.flag}'

# Payment Model
class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_no = models.ForeignKey('Booking', on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    new_field = models.IntegerField()  # As requested
    reg_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Payment {self.payment_id} for Invoice {self.invoice_no}'

# Bookings Model
class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    booked_for = models.CharField(max_length=255)
    dependant = models.ForeignKey(Dependant, on_delete=models.CASCADE, blank=True, null=True)  # FK to Dependant
    test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    where_taken = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f'Booking {self.booking_id} for {self.booked_for}'