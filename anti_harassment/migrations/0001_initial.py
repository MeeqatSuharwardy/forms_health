# Generated by Django 5.0.6 on 2024-05-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AntiHarassmentRecord",
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
                ("printed_name", models.CharField(max_length=255)),
                ("signature_image", models.ImageField(upload_to="signatures/")),
                ("submission_date", models.DateField()),
                ("pdf_file", models.FileField(upload_to="anti_harassment_pdfs/")),
            ],
        ),
    ]
