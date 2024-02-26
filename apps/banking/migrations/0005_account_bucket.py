# Generated by Django 4.2.7 on 2024-02-26 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("overview", "0001_initial"),
        ("banking", "0004_remove_account_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="bucket",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="banking_items",
                to="overview.bucket",
            ),
        ),
    ]
