from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
import uuid


# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor')
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=False)
    avatar = CloudinaryField('avatar', default='ibhuo9ahkqa8kxbg211l')
    is_doctor_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    unique_verify_string = models.CharField(max_length=256, default=uuid.uuid4)
    passwordChangeField = models.CharField(max_length=128, null=True, blank=True)
    
