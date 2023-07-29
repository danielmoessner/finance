# Generated by Django 3.0.3 on 2020-03-29 19:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("crypto", "0052_price_symbol"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="price",
            unique_together={("symbol", "date", "currency")},
        ),
        migrations.RemoveField(
            model_name="price",
            name="asset",
        ),
    ]
