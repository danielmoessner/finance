# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-14 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crypto", "0004_remove_timespan_test"),
    ]

    operations = [
        migrations.AlterField(
            model_name="depot",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
