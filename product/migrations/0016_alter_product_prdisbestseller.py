# Generated by Django 4.2.7 on 2023-12-03 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0015_product_prdisbestseller_product_prdisnew"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="PRDISBestSeller",
            field=models.BooleanField(default=False),
        ),
    ]