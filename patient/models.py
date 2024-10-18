from django.db import models
from django.conf import settings

# Create your models here.

class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    district = models.CharField(max_length=120, default=None, null=True, blank=True)
    state = models.CharField(max_length=100, default=None, null=True, blank=True)
    healthCard = models.CharField(max_length=100, default=None, null=True, blank=True)
    desc = models.TextField(max_length=150, default=None, null=True, blank=True)

