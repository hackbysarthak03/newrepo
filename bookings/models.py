from django.db import models
from patient.models import PatientProfile
from doctor.models import DoctorProfile
# Create your models here.

class Booking(models.Model):
    STATUS_CHOICES = [
        (0, 'Waiting'),
        (1, 'Under Treatment'),
        (2, 'Checkup Done')
    ]

    patient_profile = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor_profile = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    booked_on = models.DateTimeField(auto_now_add=True)
    review = models.TextField(max_length=200, null=True, blank=True)
    prescription = models.TextField(max_length=400, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    prescribed_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    pr_no = models.CharField(max_length=40, default='--', blank=True, null=True)
