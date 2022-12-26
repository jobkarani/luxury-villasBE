from rest_framework import serializers
from .models import *

class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villa
        fields = ['id', 'name', 'slug','price', 'image', 'image2', 'image3','image4','heading' 'description', 'offer1','offer2','offer3','offer4','roomSize', 'capacity','is_available']

# class CategorySerializer(serializers.ModelSerializer):
#     products = ProductSerializer(many=True, read_only=True)
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'slug', 'products']

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ['id', 'image', 'heading', 'created_at', 'text']
