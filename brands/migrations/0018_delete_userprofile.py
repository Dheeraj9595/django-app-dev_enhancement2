# Generated by Django 4.1.5 on 2024-05-06 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("brands", "0017_userprofile"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]