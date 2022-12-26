from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='productsPage'),
    path('villas/', views.get_villas, name='villas'),
    path('blogs/', views.get_blogs, name='blogs'),
    path('getBlogDetails/<int:blog_id>/', views.getBlogDetails, name='Blog Details' ),
    path('country/', views.get_country, name='country'),
    path('offer/', views.get_offer, name='offer'),
    path('experience/', views.get_experience, name='experience'),
    path('dining/', views.get_dining, name='dining'),
    path('wedding/', views.get_wedding, name='wedding'),
    path('sustainability/', views.get_sustainability, name='sustainability'),
    # path('api_products/', views.api_products, name='apiProducts' ),
    # path('getProductDetails/<int:product_id>/', views.getProductDetails, name='getProductDetails' ),
    # path('api_categoryproducts/<int:category_id>/', views.getProductsByCategory, name='apiCategoryproducts' ),
    
]