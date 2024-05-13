# Generated by Django 5.0.6 on 2024-05-12 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application_for_employment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employmentapplication",
            name="pdf_file",
            field=models.FileField(upload_to="application_for_employment/"),
        ),
        migrations.CreateModel(
            name="Qualification",
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
                ("school_name", models.CharField(max_length=255)),
                ("degree", models.CharField(max_length=255)),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qualifications",
                        to="application_for_employment.employmentapplication",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkHistory",
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
                ("job_title", models.CharField(max_length=255)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("company_name", models.CharField(max_length=255)),
                ("supervisor_name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=15)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zip", models.CharField(max_length=10)),
                ("duties", models.TextField()),
                ("reason_for_leaving", models.TextField()),
                ("starting_salary", models.CharField(max_length=100)),
                ("ending_salary", models.CharField(max_length=100)),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work_history",
                        to="application_for_employment.employmentapplication",
                    ),
                ),
            ],
        ),
    ]