"""
URL configuration for formsbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('i9_form.urls')),
    path('', include('w4_form.urls')),
    path('', include('anti_harassment.urls')),
    path('', include('application_for_employment.urls')),
    path('', include('cell_phone_policy.urls')),
    path('', include('direct_deposit.urls')),
    path('', include('employee_emergency_contacts.urls')),
    path('', include('employee_payroll_information.urls')),
    path('', include('hippa_agreement.urls')),
    path('', include('credential_comprehensive.urls')),
    path('', include('sendEmail.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
