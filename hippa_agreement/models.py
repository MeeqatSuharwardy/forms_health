from django.db import models

class HIPAAAgreement(models.Model):
    employee_name = models.CharField(max_length=255)
    agreement_date = models.TextField()
    agreement_month = models.TextField()
    agreement_year = models.TextField()
    signature_image = models.ImageField(upload_to='signatures/')
    pdf_file = models.FileField(upload_to='hippa_agreement/')

    def __str__(self):
        return f"{self.employee_name} - {self.agreement_date}"
