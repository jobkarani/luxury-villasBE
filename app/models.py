from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
# Create your models here.

class Villa(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.FloatField()
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    image4 = ImageField(blank=True,null=True, manual_crop="")
    heading = models.TextField(max_length=500)
    description = models.TextField(max_length=4000)
    offer1 = models.TextField(max_length=500)
    offer2 = models.TextField(max_length=500)
    offer3 = models.TextField(max_length=500)
    offer4 = models.TextField(max_length=500)
    roomSize = models.IntegerField()
    capacity = models.IntegerField()
    is_available = models.BooleanField(default = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Blogs(models.Model):
    image = ImageField( manual_crop="")
    heading = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=False)

    def __str__(self):
        return self.heading

class Destination(models.Model):
    country = models.TextField(max_length=500)
    villa = models.ForeignKey(Villa,on_delete=models.CASCADE)

    def __str__(self):
        return self.country