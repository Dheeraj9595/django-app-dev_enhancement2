# Generated by Django 4.1.5 on 2024-04-18 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0012_categoryuserlink"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categoryuserlink",
            options={
                "verbose_name": "Category User Link",
                "verbose_name_plural": "Category Access Permissions",
            },
        ),
    ]
