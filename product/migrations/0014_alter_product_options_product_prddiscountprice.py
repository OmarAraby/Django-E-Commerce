# Generated by Django 4.2.7 on 2023-12-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0013_product_prdslug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Product", "verbose_name_plural": "Products"},
        ),
        migrations.AddField(
            model_name="product",
            name="PRDDiscountPrice",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=8, verbose_name="Discount Price"
            ),
            preserve_default=False,
        ),
    ]