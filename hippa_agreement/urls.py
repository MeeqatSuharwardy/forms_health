from django.urls import path
from .views import submit_hipaa_agreement

urlpatterns = [
    path('submit_hipaa_agreement/', submit_hipaa_agreement, name='submit_hipaa_agreement'),
]
