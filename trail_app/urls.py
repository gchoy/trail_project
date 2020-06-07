from django.urls import path
from . import views


urlpatterns = [
    path('locations', views.locations_list, name='locations_list'),
    path('locations/<int:id>/', views.location_detail, name='location_detail'),
    path('locations/new/', views.location_new, name='location_new'),
    path('location/<int:id>/edit/', views.location_edit, name='location_edit'),
]
