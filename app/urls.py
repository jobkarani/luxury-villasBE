from django.urls import path
from app import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.index, name='productsPage'),
    path('villas/', views.get_villas, name='villas'),
    path('villaDetails/<int:villa_id>/', views.getVillaDetails, name='Villa Details' ),
    path('villasAndCountries/', views.getCountriesAndVillas, name='Villa Countries' ),
    path('blogs/', views.get_blogs, name='blogs'),
    path('blogDetails/<int:blog_id>/', views.getBlogDetails, name='Blog Details' ),
    path('country/', views.get_country, name='country'),
    path('countryDetails/<int:country_id>/', views.getCountryDetails, name='Country Details' ),
    path('offer/', views.get_offer, name='offer'),
    path('offerDetails/<int:offer_id>/', views.getOfferDetails, name='Offer Details' ),
    path('dining/', views.get_dining, name='dining'),
    path('diningDetails/<int:dining_id>/', views.getDiningDetails, name='Dining Details' ),
    path('sustainability/', views.get_sustainability, name='sustainability'),
    path('sustainabilityDetails/<int:sustainability_id>/', views.getSustainabilityDetails, name='Sustainability Details' ),
    path('countryVillas/<int:country_id>/', views.getVillasByCountry, name='Country Villas' ),
    path('bookings/', views.BookingView.as_view(), name='create_booking'),
    path('profile/<int:profile_id>/', views.view_profile, name='view_profile'),

    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]