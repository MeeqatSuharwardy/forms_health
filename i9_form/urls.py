from django.urls import path
from .views import upload_pdf, search_i9_forms

urlpatterns = [
    path('upload_pdf/', upload_pdf, name='upload_pdf'),
    path('search_i9_forms/', search_i9_forms, name='search_i9_forms'),

]
