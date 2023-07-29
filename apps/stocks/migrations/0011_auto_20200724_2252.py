# Generated by Django 3.0.3 on 2020-07-24 20:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stocks", "0010_bank_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="depot",
            name="value",
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name="depot",
            name="balance",
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]
