# Generated by Django 4.2 on 2024-12-07 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("farmers", "0002_supervisorcreatetask_supervisorcreateworker"),
    ]

    operations = [
        migrations.CreateModel(
            name="MainProfile",
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
                ("phone", models.IntegerField()),
                ("image", models.ImageField(upload_to="profileimages/")),
            ],
        ),
        migrations.CreateModel(
            name="SupervisorProfile",
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
                (
                    "email",
                    models.EmailField(default="default@example.com", max_length=254),
                ),
                ("role", models.CharField(max_length=100)),
                ("phone", models.IntegerField()),
                ("image", models.ImageField(upload_to="profileimages/")),
            ],
        ),
        migrations.CreateModel(
            name="WorkerProfile",
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
                (
                    "email",
                    models.EmailField(default="default@example.com", max_length=254),
                ),
                ("role", models.CharField(max_length=100)),
                ("phone", models.IntegerField()),
                ("image", models.ImageField(upload_to="profileimages/")),
            ],
        ),
        migrations.RenameField(
            model_name="supervisorcreateworker",
            old_name="days",
            new_name="phone",
        ),
        migrations.RenameField(
            model_name="supervisorcreateworker",
            old_name="description",
            new_name="status",
        ),
        migrations.RenameField(
            model_name="supervisorcreateworker",
            old_name="heading",
            new_name="worktype",
        ),
        migrations.AddField(
            model_name="supervisorcreateworker",
            name="email",
            field=models.EmailField(default="default@example.com", max_length=254),
        ),
        migrations.AddField(
            model_name="supervisorcreateworker",
            name="image",
            field=models.ImageField(
                default=django.utils.timezone.now, upload_to="workerimages/"
            ),
            preserve_default=False,
        ),
    ]