from django.urls import path
from .views import submit_credential_application

urlpatterns = [
    path('submit_credential_application/', submit_credential_application, name='submit_credential_application'),
]
