# Generated by Django 4.2.7 on 2023-12-03 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0012_alter_category_catimg"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="PRDSlug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
