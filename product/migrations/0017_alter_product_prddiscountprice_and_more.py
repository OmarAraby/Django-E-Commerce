# Generated by Django 4.2.7 on 2023-12-03 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0016_alter_product_prdisbestseller"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="PRDDiscountPrice",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Discount Price",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="PRDISBestSeller",
            field=models.BooleanField(default=False, verbose_name="Best Seller"),
        ),
        migrations.AlterField(
            model_name="product",
            name="PRDISNew",
            field=models.BooleanField(default=True, verbose_name="New Product"),
        ),
        migrations.AlterField(
            model_name="product",
            name="PRDSlug",
            field=models.SlugField(blank=True, null=True, verbose_name="Product URL"),
        ),
    ]
