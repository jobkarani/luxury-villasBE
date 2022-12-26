from rest_framework import serializers
from .models import *

class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villa
        fields = ['id', 'name', 'slug','price', 'image', 'image2', 'image3','image4','heading', 'description', 'offer1','offer2','offer3','offer4','roomSize', 'capacity','is_available']

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ['id', 'image', 'heading', 'created_at', 'text']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'slug', 'villa']

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'name', 'slug','image', 'villa','price','description']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'name', 'slug','image', 'country','description']

class DiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dining
        fields = ['id', 'name', 'slug','heading', 'image','villa', 'description','timeline','email', 'phone']

class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = ['id', 'name', 'slug', 'description']

class SustainabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sustainability
        fields = ['id', 'name', 'slug', 'villa', 'description']