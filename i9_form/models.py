from django.db import models

class UserPDF(models.Model):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    pdf_file = models.FileField(upload_to='i9/')  # Files will be saved in 'media/i9/'
    submitted_year = models.IntegerField()

    def __str__(self):
        return f"{self.full_name}_{self.date_of_birth}"
