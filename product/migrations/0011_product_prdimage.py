# Generated by Django 4.2.7 on 2023-12-01 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0010_product_prdbrand_product_prdcategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="PRDImage",
            field=models.ImageField(
                blank=True, null=True, upload_to="product_image/", verbose_name="Image"
            ),
        ),
    ]
