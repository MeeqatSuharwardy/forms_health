# urls.py
from django.urls import path
from .views import submit_cell_phone_policy_form, search_cell_phone_policy_records

urlpatterns = [
    path('submit_cell_phone_policy_form/', submit_cell_phone_policy_form, name='submit_cell_phone_policy_form'),
    path('search_cell_phone_policy_records/', search_cell_phone_policy_records, name='search_cell_phone_policy_records')
]
