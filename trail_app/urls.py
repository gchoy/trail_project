from django.urls import path
from . import views


urlpatterns = [
    path('locations', views.locations_list, name='locations_list'),
    path('locations/<int:id>/', views.location_detail, name='location_detail'),
    path('locations/new/', views.location_new, name='location_new'),
    path('locations/<int:id>/edit/', views.location_edit, name='location_edit'),
    
    path('spots', views.spots_list, name='spots_list'),
    path('spots/<int:id>/', views.spot_detail, name='spot_detail'),
    path('spots/new/', views.spot_new, name='spot_new'),
]
