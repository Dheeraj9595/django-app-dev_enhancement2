# Generated by Django 4.1.5 on 2024-04-25 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("brands", "0015_delete_branduserlink"),
    ]

    operations = [
        migrations.CreateModel(
            name="BrandUserLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("local_brands", models.ManyToManyField(to="brands.localbrand")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Brands Access Permissions",
                "verbose_name_plural": "Brands Access Permissions",
            },
        ),
    ]
