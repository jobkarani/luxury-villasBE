from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
# from simple_mail.mail import send_mail

from app.models import *
from .serializer import *
from .pagination import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


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
@permission_classes([permissions.IsAuthenticated])
def view_profile(request, profile_id):
    if request.method == "GET":
        profile = get_object_or_404(Profile, id=profile_id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)




class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer