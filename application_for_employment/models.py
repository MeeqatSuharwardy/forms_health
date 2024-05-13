from django.db import models

class EmploymentApplication(models.Model):
    position_applying_for = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    home_telephone = models.CharField(max_length=15)
    business_telephone = models.CharField(max_length=15)
    cellular = models.CharField(max_length=15)
    start_date = models.DateField()
    salary_desired = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    days = models.CharField(max_length=100)
    authorized = models.CharField(max_length=3)
    special_skills = models.TextField()
    date_of_birth = models.DateField()
    pdf_file = models.FileField(upload_to='application_for_employment/')

    def __str__(self):
        return f"{self.name} - {self.position_applying_for}"

class WorkHistory(models.Model):
    application = models.ForeignKey(EmploymentApplication, on_delete=models.CASCADE, related_name='work_history')
    job_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    company_name = models.CharField(max_length=255)
    supervisor_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    duties = models.TextField()
    reason_for_leaving = models.TextField()
    starting_salary = models.CharField(max_length=100)
    ending_salary = models.CharField(max_length=100)

class Qualification(models.Model):
    application = models.ForeignKey(EmploymentApplication, on_delete=models.CASCADE, related_name='qualifications')
    school_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)


class Reference(models.Model):
    application = models.ForeignKey(EmploymentApplication, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    relationship = models.CharField(max_length=100)