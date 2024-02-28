# Generated by Django 4.2.7 on 2024-02-28 21:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("overview", "0003_bucket_wanted_percentage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bucket",
            name="wanted_percentage",
            field=models.FloatField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
