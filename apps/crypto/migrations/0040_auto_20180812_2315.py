# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-12 21:15
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crypto", "0039_auto_20180625_1258"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="depot",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="accounts",
                to="crypto.Depot",
            ),
        ),
    ]
