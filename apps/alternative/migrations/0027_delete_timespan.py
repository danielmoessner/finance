# Generated by Django 3.0.3 on 2020-03-26 11:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("alternative", "0026_delete_stats"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Timespan",
        ),
    ]
