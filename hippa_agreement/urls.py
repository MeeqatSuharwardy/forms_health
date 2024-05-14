from django.urls import path
from .views import submit_hipaa_agreement, search_hipaa_agreements

urlpatterns = [
    path('submit_hipaa_agreement/', submit_hipaa_agreement, name='submit_hipaa_agreement'),
    path('search_hipaa_agreements/', search_hipaa_agreements, name='search_hipaa_agreements')
]
