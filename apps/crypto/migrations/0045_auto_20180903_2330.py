# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crypto", "0044_picture_f"),
    ]

    operations = [
        migrations.AlterField(
            model_name="picture",
            name="d",
            field=models.DateField(),
        ),
    ]
