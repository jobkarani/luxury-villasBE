from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class VillaSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')
    class Meta:
        model = Villa
        fields = ['id', 'name', 'country','country_name', 'price', 'image', 'image2', 'image3','image4','heading', 'description', 'feature1','feature2','feature3','feature4','feature5', 'check_in','check_out', 'complimentary1', 'complimentary2', 'is_available']

class BlogsSerializer(serializers.ModelSerializer):
    tag_name = serializers.CharField(source='tag.name')
    class Meta:
        model = Blogs
        fields = ['id','image_cover', 'image', 'heading', 'tag','tag_name', 'text1','text2','text3']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CountrySerializer(serializers.ModelSerializer):
    tag_name = serializers.CharField(source='tag.name')
    villas = VillaSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['id', 'name','image','image_toper','video_url', 'catchy_phrase', 'tag_name', 'villas','description1','description2']

class OfferSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name')
    villa_name = serializers.CharField(source='villa.name')
    class Meta:
        model = Offer
        fields = ['id', 'name', 'country','country_name', 'villa', 'villa_name', 'image', 'offerDetails_image', 'old_price','description', 'inclusion1', 'inclusion2', 'inclusion3','inclusion4','inclusion5','complimentary1','complimentary2','complimentary3','complimentary4','term1','term2','term3','term4','term5']

class DiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name','heading', 'image','catchy_phrase', 'description','timeline','email', 'phone', 'info1','gallery1', 'gallery2', 'gallery3']

class SustainabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'villa', 'description']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'firstname', 'lastname', 'email', 'phone', 'start_date', 'end_date', 'guestsnumber', 'villa', 'special_requests']

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'firstname', 'lastname', 'image', 'email', 'phone')
    
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        user = validated_data.pop('user')
        profile = Profile.objects.create(user=user, **validated_data)
        return profile
    
    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        instance.user = user
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user