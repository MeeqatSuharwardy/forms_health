from django.urls import path
from .views import submit_emergency_contact, search_emergency_contacts

urlpatterns = [
    path('submit_emergency_contact/', submit_emergency_contact, name='submit_direct_deposit'),
    path('search_emergency_contacts/', search_emergency_contacts, name='search_direct_deposits')
]
