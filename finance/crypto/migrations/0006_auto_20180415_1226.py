# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-15 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import finance.crypto.models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0005_auto_20180414_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depot',
            name='timespan',
            field=models.ForeignKey(null=True, on_delete=models.SET(finance.crypto.models.IntelligentTimespan.get_default_intelligent_timespan), related_name='depots', to='crypto.IntelligentTimespan'),
        ),
    ]
