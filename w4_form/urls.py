from django.urls import path
from .views import upload_w4

urlpatterns = [
    path('upload_w4/', upload_w4, name='upload_w4'),
]
