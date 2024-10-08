from django.db import models
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    slug = AutoSlugField(unique=True, null=True, populate_from = 'name', default=None)
    dept_img = CloudinaryField('department', default='jkicyfesnzkvgxqx9lve')

    def __str__(self) -> str:
        return self.name
    