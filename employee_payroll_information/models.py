from django.db import models

class EmployeePayroll(models.Model):
    employee_name = models.CharField(max_length=255)
    date_of_hire = models.DateField()
    original_position = models.CharField(max_length=255)
    change_position_date = models.DateField(null=True, blank=True)
    pay_type = models.CharField(max_length=50)
    pay_frequency = models.CharField(max_length=50)
    hire_pay_rate = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField(null=True, blank=True)
    approval_date = models.DateField(null=True, blank=True)
    signature_image = models.ImageField(upload_to='signatures/')
    date_signed = models.DateField()
    pdf_file = models.FileField(upload_to='employee_payroll_information/')

    def __str__(self):
        return f"{self.employee_name} - {self.pay_type}"
