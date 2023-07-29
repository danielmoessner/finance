# Generated by Django 3.0.3 on 2020-03-18 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("alternative", "0024_auto_20200317_2219"),
    ]

    operations = [
        migrations.CreateModel(
            name="Stats",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="depot",
            name="latest_picture",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="alternative.Picture",
            ),
        ),
    ]
