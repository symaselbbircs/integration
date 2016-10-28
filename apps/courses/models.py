from __future__ import unicode_literals
from django.db import models
from ..registration.models import Users


# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    users = models.ManyToManyField(Users)

class Descriptions(models.Model):
    description = models.TextField()
    course = models.ForeignKey('Courses', related_name="coursedescription")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
