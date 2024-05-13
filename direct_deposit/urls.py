from django.urls import path
from .views import submit_direct_deposit, search_direct_deposits

urlpatterns = [
    path('submit_direct_deposit/', submit_direct_deposit, name='submit_direct_deposit'),
    path('search_direct_deposits/', search_direct_deposits, name='search_direct_deposits')
]
