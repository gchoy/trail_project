from django.urls import path
from . import views


urlpatterns = [
    path('locations', views.locations_list, name='locations_list'),
    path('locations/<int:id>/', views.location_detail, name='location_detail'),
    #path('add_location/', views.add_location, name='add_location'),
]
