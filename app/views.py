from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404, render

from app.models import *
from .serializer import *
from .pagination import *

# Create your views here.

def index(request):
    return render(request, 'products.html')


@api_view(['GET',])
def get_villas(request):
    if request.method == "GET":
        villas = Villa.objects.all()
        serializer = VillaSerializer(villas, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getVillaDetails(request, villa_id):
    if request.method == "GET":
        villas= Villa.objects.filter(id = villa_id)
        serializer = VillaSerializer(villas, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_blogs(request):
    if request.method == "GET":
        blogs = Blogs.objects.all()
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getBlogDetails(request, blog_id):
    if request.method == "GET":
        blogs= Blogs.objects.filter(id = blog_id)
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def get_country(request):
    if request.method == "GET":
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getCountryDetails(request, country_id):
    if request.method == "GET":
        country = Country.objects.filter(id = country_id)
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def get_offer(request):
    if request.method == "GET":
        offer = Offer.objects.all()
        serializer = OfferSerializer(offer, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getOfferDetails(request, offer_id):
    if request.method == "GET":
        offer = Offer.objects.filter(id = offer_id)
        serializer =OfferSerializer(offer, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def get_dining(request):
    if request.method == "GET":
        dining = Restaurant.objects.all()
        serializer = DiningSerializer(dining, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getDiningDetails(request, dining_id):
    if request.method == "GET":
        dining = Restaurant.objects.filter(id = dining_id)
        serializer = DiningSerializer(dining, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def get_sustainability(request):
    if request.method == "GET":
        sustainability = Contact.objects.all()
        serializer = SustainabilitySerializer(sustainability, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getSustainabilityDetails(request, sustainability_id):
    if request.method == "GET":
        sustainability = Contact.objects.filter(id = sustainability_id)
        serializer = SustainabilitySerializer(sustainability, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getVillasByCountry(request, country_id):
    if request.method == "GET":
        country = get_object_or_404(Country, id=country_id)
        villa = Villa.objects.filter(country=country)
        serializer = VillaSerializer(villa, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getCountriesAndVillas(request):
    if request.method == "GET":
        countries = Country.objects.all().prefetch_related('villa_set')
        data = []
        for country in countries:
            villa = Villa.objects.filter(country=country)
            serializer = CountrySerializer(country)
            country_data = serializer.data
            country_data['villa'] = VillaSerializer(villa, many=True).data
            data.append(country_data)
        return Response(data)
    
@api_view(['POST'])
def create_booking(request):
    if request.method == "POST":
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['POST'])
def create_profile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profile_detail(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


@api_view(['POST'])
def registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = serializer.instance
        payload = api_settings.JWT_PAYLOAD_HANDLER(user)
        token = api_settings.JWT_ENCODE_HANDLER(payload)
        return Response({'token': token}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = JSONWebTokenSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.object.get('user') or request.user
        payload = api_settings.JWT_PAYLOAD_HANDLER(user)
        token = api_settings.JWT_ENCODE_HANDLER(payload)
        return Response({'token': token})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)