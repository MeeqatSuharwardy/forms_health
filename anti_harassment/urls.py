from django.urls import path
from .views import submit_anti_harassment_form, search_anti_harassment_records

urlpatterns = [
    path('anti_harassment_submit_form/', submit_anti_harassment_form, name='submit_anti_harassment_form'),
    path('anti_harassment_submit_form_search/', search_anti_harassment_records, name='search_anti_harassment_records')
]