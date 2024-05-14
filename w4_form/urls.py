from django.urls import path
from .views import upload_w4, search_w4_forms

urlpatterns = [
    path('upload_w4/', upload_w4, name='upload_w4'),
    path('search_w4_forms/', search_w4_forms, name='search_w4_forms'),
]
