from django.db import models
from django.conf import settings
from department.models import *

# Create your models here.

class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    reg_no = models.CharField(max_length=10, null=True, blank=True)
    specialist = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(max_length=200, default=None, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    hospital = models.CharField(max_length=150, null=True, blank=True)
    hospital_district = models.CharField(max_length=150, null=True, blank=True)
    hospital_state = models.CharField(max_length=150, null=True, blank=True)
    fees = models.CharField(max_length=50, null=True, blank=True)
    avail = models.BooleanField(default=False, null=True, blank=True)
    room_id = models.CharField(max_length=100, null=True, blank=True)

    
    



