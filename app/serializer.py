from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


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
        fields = ['id', 'name','image','image_toper','video', 'catchy_phrase', 'tag_name', 'villas','description1','description2']

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

class ProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    class Meta:
        model = Profile
        fields = ['id','user','user_name', 'firstname','lastname', 'image', 'email','phone','date_joined']
    


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user