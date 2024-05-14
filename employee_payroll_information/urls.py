from django.urls import path
from .views import submit_employee_payroll, search_employee_payroll

urlpatterns = [
    path('submit_employee_payroll/', submit_employee_payroll, name='submit_employee_payroll'),
    path('search_employee_payroll/', search_employee_payroll, name='search_employee_payroll')
]
