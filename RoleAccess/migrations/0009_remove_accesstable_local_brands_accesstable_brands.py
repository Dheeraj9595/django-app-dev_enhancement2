# Generated by Django 4.1.5 on 2024-05-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brands", "0018_delete_userprofile"),
        ("RoleAccess", "0008_rename_brands_accesstable_local_brands"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="accesstable",
            name="local_brands",
        ),
        migrations.AddField(
            model_name="accesstable",
            name="brands",
            field=models.ManyToManyField(blank=True, to="brands.brand"),
        ),
    ]
