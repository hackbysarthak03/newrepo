from django.db import models
from doctor.models import *
from django.utils import timezone
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField
from django.conf import settings


# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    category = models.JSONField(default=list, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True, null=True, blank=True)
    cover_img = CloudinaryField('cover_img', default='ibhuo9ahkqa8kxbg211l')

    def __str__(self) -> str:
        return f'{self.user} -- {self.created_on}'

class Comment(models.Model):
    blog_post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.first_name} on {self.blog_post.title}'
