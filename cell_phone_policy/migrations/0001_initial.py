# Generated by Django 5.0.6 on 2024-05-12 22:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CellPhonePolicyRecord",
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
                ("date_of_birth", models.DateField()),
                (
                    "signature_image",
                    models.ImageField(upload_to="cell_phone_policy/signatures/"),
                ),
                ("submission_date", models.DateField()),
                ("pdf_file", models.FileField(upload_to="cell_phone_policy/")),
            ],
        ),
    ]