import datetime
import time
from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = ImageField( manual_crop="")
    image_toper = ImageField( manual_crop="")
    video_file = models.FileField(upload_to='videos/',blank=True,null=True)
    catchy_phrase = models.CharField(max_length=100, blank=False)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    description1 = models.TextField(max_length=1500)
    description2 = models.TextField(max_length=1500)

    def __str__(self):
        return self.name

class Villa(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    price = models.FloatField()
    image = ImageField( manual_crop="")
    image2 = ImageField(blank=True, null=True, manual_crop="")
    image3 = ImageField(blank=True,null=True, manual_crop="")
    image4 = ImageField(blank=True,null=True, manual_crop="")
    heading = models.TextField(max_length=500)
    description = models.TextField(max_length=4000)
    feature1 = models.TextField(max_length=500)
    feature2 = models.TextField(max_length=500, blank=True)
    feature3 = models.TextField(max_length=500, blank=True)
    feature4 = models.TextField(max_length=500, blank=True)
    feature5 = models.TextField(max_length=500, blank=True)
    check_in = models.TimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    check_out = models.TimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    complimentary1 = models.TextField(max_length=500, blank=True)
    complimentary2 = models.TextField(max_length=500, blank=True)
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

class Offer(models.Model):
    name = models.CharField(max_length=100, blank=False)
    country = models.ForeignKey(Country,on_delete=models.CASCADE, default="")
    villa = models.ForeignKey(Villa,on_delete=models.CASCADE, default="") 
    image = ImageField( manual_crop="")
    offerDetails_image = ImageField( manual_crop="", default="")
    old_price = models.FloatField()
    description = models.TextField(max_length=4000)
    inclusion1 = models.TextField(max_length=500, default="")
    inclusion2 = models.TextField(max_length=500, blank=True)
    inclusion3 = models.TextField(max_length=500, blank=True)
    inclusion4 = models.TextField(max_length=500, blank=True)
    inclusion5 = models.TextField(max_length=500, blank=True)
    complimentary1 = models.TextField(max_length=500, blank=True)
    complimentary2 = models.TextField(max_length=500, blank=True)
    complimentary3 = models.TextField(max_length=500, blank=True)
    complimentary4 = models.TextField(max_length=500, blank=True)
    term1 = models.TextField(max_length=500, blank=True)
    term2 = models.TextField(max_length=500, blank=True)
    term3 = models.TextField(max_length=500, blank=True)
    term4 = models.TextField(max_length=500, blank=True)
    term5 = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Dining(models.Model):
    name = models.CharField(max_length=100, blank=False)
    heading = models.TextField(max_length=100, blank=False)
    image = ImageField( manual_crop="")
    villa = models.ForeignKey(Villa,on_delete=models.CASCADE) 
    description = models.TextField(max_length=4000)
    timeline = models.TextField(max_length=1000, blank=False)
    email = models.EmailField(max_length=254,blank=False)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Wedding(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=4000, blank=False)

    def __str__(self):
        return self.name

class Sustainability(models.Model):
    name = models.CharField(max_length=100, blank=False)
    villa = models.ForeignKey(Villa,on_delete=models.CASCADE) 
    description = models.TextField(max_length=4000)

    def __str__(self):
        return self.name
