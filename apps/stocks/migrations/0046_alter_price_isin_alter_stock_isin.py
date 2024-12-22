# Generated by Django 5.1.4 on 2024-12-22 21:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0045_remove_price_exchange_remove_price_ticker_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="isin",
            field=models.CharField(
                default=None,
                max_length=12,
                validators=[django.core.validators.MinLengthValidator(12)],
                verbose_name="ISIN",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stock",
            name="isin",
            field=models.CharField(
                default=None,
                max_length=12,
                validators=[django.core.validators.MinLengthValidator(12)],
                verbose_name="ISIN",
            ),
            preserve_default=False,
        ),
    ]
