# models.py
from django.db import models

class CellPhonePolicyRecord(models.Model):
    printed_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    signature_image = models.ImageField(upload_to='cell_phone_policy/signatures/')
    submission_date = models.DateField()
    pdf_file = models.FileField(upload_to='cell_phone_policy/')

    def __str__(self):
        return f"{self.printed_name} - {self.date_of_birth} - {self.submission_date}"
