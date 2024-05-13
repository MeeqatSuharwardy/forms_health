from django.db import models

class DirectDeposit(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city_state_zip = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    routing_number = models.CharField(max_length=255)
    amount = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    date = models.DateField()
    pdf_file = models.FileField(upload_to='direct_deposit/')
    signature_image = models.ImageField(upload_to='signatures/')

    def __str__(self):
        return f"{self.name} - {self.bank_name}"
