# Generated by Django 3.0.3 on 2020-07-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stocks", "0017_auto_20200729_1503"),
    ]

    operations = [
        migrations.AddField(
            model_name="depot",
            name="inflow_total",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="depot",
            name="outflow_total",
            field=models.FloatField(null=True),
        ),
    ]
