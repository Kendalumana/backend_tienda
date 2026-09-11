from django.urls import path
from . import views 

urlpatterns = [
    path('home/',views.home,name='home_product'),
    path('api/all/',views.api_products01,name='api_products01'),
    path('api/',views.api_products_all,name='api_product'),
    path('api/rest/',views.api_products,name='api_products'),
    path('api/rest/<int:pk>/',views.details_products,name='detail_products'),



]