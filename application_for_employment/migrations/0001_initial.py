# Generated by Django 5.0.6 on 2024-05-12 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmploymentApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position_applying_for", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zip", models.CharField(max_length=10)),
                ("home_telephone", models.CharField(max_length=15)),
                ("business_telephone", models.CharField(max_length=15)),
                ("cellular", models.CharField(max_length=15)),
                ("start_date", models.DateField()),
                ("salary_desired", models.CharField(max_length=100)),
                ("hours", models.CharField(max_length=100)),
                ("days", models.CharField(max_length=100)),
                ("authorized", models.CharField(max_length=3)),
                ("special_skills", models.TextField()),
                ("date_of_birth", models.DateField()),
                ("pdf_file", models.FileField(upload_to="employment_applications/")),
            ],
        ),
    ]