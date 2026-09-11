from django.urls import path
from . import views 

urlpatterns = [
   
    path('api/rest/',views.api_users,name='api_users'),
    path('api/rest/<int:pk>/',views.details_users,name='detail_users')



]