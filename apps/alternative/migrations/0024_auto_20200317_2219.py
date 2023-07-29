# Generated by Django 3.0.3 on 2020-03-17 21:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("alternative", "0023_alternative_latest_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alternative",
            name="latest_picture",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="alternative.Picture",
            ),
        ),
    ]
