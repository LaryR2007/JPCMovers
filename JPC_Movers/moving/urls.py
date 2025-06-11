from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
import uuid

urlpatterns = [
    path("", views.index, name="index"),
    path('services/', views.services_view, name='services'),
    path('contact/', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
    path('reserve/', views.make_reservation, name='make_reservation'),
    path('reservation_success/<str:reservation_number>/', views.reservation_success, name='reservation_success'),
    path('lookup/', views.lookup_reservation, name='lookup_reservation'),
    path('edit/<uuid:reservation_number>/', views.edit_reservation, name='edit_reservation'),
]
