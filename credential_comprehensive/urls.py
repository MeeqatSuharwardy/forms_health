from django.urls import path
from .views import submit_credential_application, search_credential_applications

urlpatterns = [
    path('submit_credential_application/', submit_credential_application, name='submit_credential_application'),
    path('search_credential_applications/', search_credential_applications, name='search_credential_applications'),

]
