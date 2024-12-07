# Generated by Django 4.2 on 2024-12-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[
                    ("admin", "Admin"),
                    ("supervisor", "Supervisor"),
                    ("worker", "Worker"),
                ],
                max_length=100,
            ),
        ),
    ]