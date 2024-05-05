from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_site_tour, name='liste_site_tour'),
    path('ticket/', views.ticket, name='ticket'),
    path('ticket/create/', views.create_ticket, name='create_ticket'),
    path('hebergement/', views.hebergement, name='hebergement'),
    path('location/', views.location, name='location'),
    path('ticketHotel/', views.ticketHotel, name='ticketHotel'),
]
