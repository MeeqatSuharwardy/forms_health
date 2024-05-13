from django.db import models

class EmergencyContact(models.Model):
    employee_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    address = models.TextField()
    city_state_zip = models.CharField(max_length=100)
    primary_contact_name = models.CharField(max_length=255)
    primary_contact_relationship = models.CharField(max_length=100)
    primary_contact_phone = models.CharField(max_length=50)
    primary_contact_alt_phone = models.CharField(max_length=50, blank=True)
    secondary_contact_name = models.CharField(max_length=255)
    secondary_contact_relationship = models.CharField(max_length=100)
    secondary_contact_phone = models.CharField(max_length=50)
    secondary_contact_alt_phone = models.CharField(max_length=50, blank=True)
    doctor_name = models.CharField(max_length=255)
    doctor_phone = models.CharField(max_length=50)
    doctor_address = models.TextField()
    date_signed = models.DateField()
    pdf_file = models.FileField(upload_to='emergency_contacts/')
    signature_image = models.ImageField(upload_to='signatures/')

    def __str__(self):
        return f"{self.employee_name} - Emergency Contacts"
