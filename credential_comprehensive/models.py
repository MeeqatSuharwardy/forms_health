from django.db import models

class CredentialApplication(models.Model):
    caqh_id = models.CharField(max_length=100)
    caqh_login = models.CharField(max_length=100)
    caqh_password = models.CharField(max_length=100)
    npi_registration = models.CharField(max_length=100)
    npi_number = models.CharField(max_length=100)
    npi_password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    ssn = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    home_address = models.TextField()
    email = models.EmailField()
    specialty = models.CharField(max_length=255)
    taxonomy = models.CharField(max_length=255)
    fl_license_number = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    document = models.FileField(upload_to='credential_comprehensive/')
    reason_if_no_document = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.date_of_birth}"
