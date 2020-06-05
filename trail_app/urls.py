from django.urls import path
from . import views


urlpatterns = [
    path('locations', views.locations_list, name='locations_list'),
    #path('locations/<int:location_id>/', views.location_detail, name='location_detail'),
    #path('new_location/', views.new_location, name='add_location'),
]
