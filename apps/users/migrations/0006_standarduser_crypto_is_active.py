# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_auto_20180531_2153"),
    ]

    operations = [
        migrations.AddField(
            model_name="standarduser",
            name="crypto_is_active",
            field=models.BooleanField(default=False),
        ),
    ]
