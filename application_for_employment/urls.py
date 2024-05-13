from django.urls import path
from .views import submit_employment_application, search_employment_applications

urlpatterns = [
    path('submit_application/', submit_employment_application, name='submit_application'),
    path('search_applications/', search_employment_applications, name='search_applications')
]
