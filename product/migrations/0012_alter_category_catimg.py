# Generated by Django 4.2.7 on 2023-12-02 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0011_product_prdimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="CATImg",
            field=models.ImageField(
                blank=True, null=True, upload_to="category/", verbose_name="Image"
            ),
        ),
    ]