# Generated by Django 5.0.6 on 2024-05-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DirectDeposit",
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
                ("name", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("city_state_zip", models.CharField(max_length=255)),
                ("bank_name", models.CharField(max_length=255)),
                ("account_number", models.CharField(max_length=255)),
                ("routing_number", models.CharField(max_length=255)),
                ("amount", models.CharField(max_length=100)),
                ("percentage", models.CharField(max_length=100)),
                ("account_type", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("pdf_file", models.FileField(upload_to="direct_deposit/")),
                ("signature_image", models.ImageField(upload_to="signatures/")),
            ],
        ),
    ]
