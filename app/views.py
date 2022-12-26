from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
# from simple_mail.mail import send_mail

from app.models import *
from .serializer import *
from .pagination import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


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
def get_experience(request):
    if request.method == "GET":
        experience = Experience.objects.all()
        serializer = ExperienceSerializer(experience, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getExperienceDetails(request, experience_id):
    if request.method == "GET":
        experience = Experience.objects.filter(id = experience_id)
        serializer =ExperienceSerializer(experience, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def get_dining(request):
    if request.method == "GET":
        dining = Dining.objects.all()
        serializer = DiningSerializer(dining, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getDiningDetails(request, dining_id):
    if request.method == "GET":
        dining = Dining.objects.filter(id = dining_id)
        serializer = DiningSerializer(dining, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def get_wedding(request):
    if request.method == "GET":
        wedding = Wedding.objects.all()
        serializer = WeddingSerializer(wedding, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getWeddingDetails(request, wedding_id):
    if request.method == "GET":
        wedding = Dining.objects.filter(id = wedding_id)
        serializer = WeddingSerializer(wedding, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def get_sustainability(request):
    if request.method == "GET":
        sustainability = Sustainability.objects.all()
        serializer = SustainabilitySerializer(sustainability, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getSustainabilityDetails(request, sustainability_id):
    if request.method == "GET":
        sustainability = Dining.objects.filter(id = sustainability_id)
        serializer = SustainabilitySerializer(sustainability, many=True)
        return Response(serializer.data)


# @api_view(['GET'])
# def getProductDetails(request, product_id):
#     if request.method == "GET":
#         product= Product.objects.filter(id = product_id)
#         serializer = ProductSerializer(product, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def getProductsByCategory(request, category_id):
#     if request.method == "GET":
#         category = get_object_or_404(Category, id=category_id)
#         products = Product.objects.filter(category=category)
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

