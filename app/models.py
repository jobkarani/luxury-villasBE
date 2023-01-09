import datetime
import time
from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField, FileField
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = ImageField( manual_crop="320x147")
    image_toper = ImageField( manual_crop="")
    video_url = models.URLField( blank=True, null=True, default="")
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
    image_cover = ImageField(blank=True, null=True, manual_crop="", default="")
    image = ImageField( manual_crop="")
    heading = models.CharField(max_length=100, blank=False)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE, default="")
    text1 = models.TextField(max_length=3000, blank=False)
    text2 = models.TextField(max_length=3000,null=True, blank=False, default="")
    text3 = models.TextField(max_length=3000,null=True, blank=False, default="")

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

class Restaurant(models.Model):
    name = models.CharField(max_length=100, blank=False)
    heading = models.TextField(max_length=100, blank=False)
    image = ImageField( manual_crop="")
    catchy_phrase = models.CharField(max_length=100, blank=False,default="")
    description = models.TextField(max_length=4000)
    timeline = models.TextField(max_length=1000, blank=False)
    email = models.EmailField(max_length=254,blank=False)
    phone = models.CharField(max_length=100)
    info1 = models.TextField(max_length=100, blank=False, default="")
    gallery1 = ImageField(blank=True, null=True, manual_crop="", default="")
    gallery2 = ImageField(blank=True, null=True, manual_crop="", default="")
    gallery3 = ImageField(blank=True, null=True, manual_crop="", default="")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    villa = models.ForeignKey(Villa,on_delete=models.CASCADE) 
    description = models.TextField(max_length=4000)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    image = ImageField( manual_crop="")
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def save_profile(self):
        self.save()

    def update(self):
        self.save()

    def create_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    def __str__(self):
        return self.user.username
