from django.urls import path
from . import views
from .views import VenueCreateView, VenueUpdateView, VenueDeleteView


urlpatterns = [
    path('', views.landing_view, name='home'),

    path('events/', views.events_view, name='events_list_view'),
    path('events/<int:pk>/', views.event_details_view, name='event_details_view'),

    path('venues/', views.venues_view, name='venues')
    path('venues/<int:pk>/', views.venue_details_view, name='venue_details_view'),

    
    path('register/', views.registration, name='register'),

    path('create/', VenueCreateView.as_view(), name='venue_create_view'),
    path('venues/<int:pk>/update/', VenueUpdateView.as_view(), name='venue_update_view'),
    path('delete/', VenueDeleteView.as_view(), name='venue_delete_view')
]
