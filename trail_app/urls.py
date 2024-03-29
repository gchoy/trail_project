from django.urls import path
from . import views


urlpatterns = [

    #path('', views.frontpage, name='frontpage'),
    
    path('locations', views.locations_list, name='locations_list'),
    path('locations/<int:id>/', views.location_detail, name='location_detail'),
    path('locations/new/', views.location_new, name='location_new'),
    path('locations/<int:id>/edit/', views.location_edit, name='location_edit'),
    path('locations/<int:id>/delete/', views.location_delete, name='location_delete'),
    
    path('spots', views.spots_list, name='spots_list'),
    path('spots/<int:id>/', views.spot_detail, name='spot_detail'),
    path('spots/new/', views.spot_new, name='spot_new'),
    path('spots/<int:id>/edit/', views.spot_edit, name='spot_edit'),
    path('spots/<int:id>/delete/', views.spot_delete, name='spot_delete'),
    
    path('trails', views.trails_list, name='trails_list'),
    path('trails/<int:id>/', views.trail_detail, name='trail_detail'),
    path('trails/new/', views.trail_new, name='trail_new'),
    path('trails/<int:id>/edit/', views.trail_edit, name='trail_edit'),
    path('trails/<int:id>/delete/', views.trail_delete, name='trail_delete'),
]
