from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
# Create your models here.

class Blogs(models.Model):
    image = ImageField( manual_crop="")
    heading = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=False)

    def __str__(self):
        return self.heading
