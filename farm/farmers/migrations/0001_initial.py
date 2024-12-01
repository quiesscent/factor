# Generated by Django 5.1.2 on 2024-12-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("role", models.CharField(max_length=100)),
                ("workId", models.IntegerField()),
                ("subject", models.CharField(max_length=100)),
                ("message", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="contactimages/")),
            ],
        ),
        migrations.CreateModel(
            name="Farmer",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("username", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=50)),
                ("phone", models.IntegerField()),
                ("profession", models.CharField(max_length=100, null=True)),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("heading", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("days", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Worker",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField()),
                ("worktype", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="workerimages/")),
            ],
        ),
    ]
