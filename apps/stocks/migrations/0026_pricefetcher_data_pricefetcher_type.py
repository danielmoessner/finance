# Generated by Django 4.2.3 on 2023-07-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stocks", "0025_auto_20210501_1839"),
    ]

    operations = [
        migrations.AddField(
            model_name="pricefetcher",
            name="data",
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="pricefetcher",
            name="type",
            field=models.CharField(
                choices=[("WEBSITE", "Website"), ("MARKETSTACK", "Marketstack")],
                default="WEBSITE",
                max_length=250,
            ),
            preserve_default=False,
        ),
    ]
