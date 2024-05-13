from django.db import models

class AntiHarassmentRecord(models.Model):
    printed_name = models.CharField(max_length=255)
    signature_image = models.ImageField(upload_to='signatures/')
    submission_date = models.DateField()
    date_of_birth = models.DateField()
    policy_text = models.TextField()
    pdf_file = models.FileField(upload_to='anti_harassment/')

    def __str__(self):
        return f"{self.printed_name} - {self.submission_date}"
