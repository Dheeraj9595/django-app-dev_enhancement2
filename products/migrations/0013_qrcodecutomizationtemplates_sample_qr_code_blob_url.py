# Generated by Django 4.1.5 on 2023-05-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_qr_code_img_blob_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcodecutomizationtemplates',
            name='sample_qr_code_blob_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]