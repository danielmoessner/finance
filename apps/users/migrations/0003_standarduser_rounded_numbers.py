# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-14 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_auto_20180413_1649"),
    ]

    operations = [
        migrations.AddField(
            model_name="standarduser",
            name="rounded_numbers",
            field=models.BooleanField(default=True),
        ),
    ]
