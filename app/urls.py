from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='productsPage'),
    path('villas/', views.get_villas, name='villas'),
    path('villaDetails/<int:villa_id>/', views.getVillaDetails, name='Villa Details' ),
    path('blogs/', views.get_blogs, name='blogs'),
    path('blogDetails/<int:blog_id>/', views.getBlogDetails, name='Blog Details' ),
    path('country/', views.get_country, name='country'),
    path('countryDetails/<int:country_id>/', views.getCountryDetails, name='Country Details' ),
    path('offer/', views.get_offer, name='offer'),
    path('offerDetails/<int:offer_id>/', views.getOfferDetails, name='Offer Details' ),
    path('experience/', views.get_experience, name='experience'),
    path('experienceDetails/<int:experience_id>/', views.getExperienceDetails, name='Experience Details' ),
    path('dining/', views.get_dining, name='dining'),
    path('diningDetails/<int:dining_id>/', views.getDiningDetails, name='Dining Details' ),
    path('wedding/', views.get_wedding, name='wedding'),
    path('weddingDetails/<int:wedding_id>/', views.getWeddingDetails, name='Wedding Details' ),
    path('sustainability/', views.get_sustainability, name='sustainability'),
    # path('countryDetails/<int:country_id>/', views.getCountryDetails, name='Country Details' ),
    # path('api_products/', views.api_products, name='apiProducts' ),
    # path('getProductDetails/<int:product_id>/', views.getProductDetails, name='getProductDetails' ),
    # path('api_categoryproducts/<int:category_id>/', views.getProductsByCategory, name='apiCategoryproducts' ),
]