from rest_framework import serializers
from .models import *

class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villa
        fields = ['id', 'name', 'country', 'price', 'image', 'image2', 'image3','image4','heading', 'description', 'offer1','offer2','offer3','offer4','roomSize', 'capacity','is_available']

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ['id', 'image', 'heading', 'created_at', 'text']

class CountrySerializer(serializers.ModelSerializer):
    villas = VillaSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['id', 'name','villas']

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'name','image', 'price','description']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'name','image', 'country','description']

class DiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dining
        fields = ['id', 'name','heading', 'image','villa', 'description','timeline','email', 'phone']

class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = ['id', 'name', 'description']

class SustainabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sustainability
        fields = ['id', 'name', 'villa', 'description']