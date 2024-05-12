# Generated by Django 4.1.5 on 2023-05-24 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_qrcodecutomizationtemplates_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcodecutomizationtemplates',
            name='sample_qr_code',
            field=models.FileField(blank=True, null=True, upload_to='products_qr_codes'),
        ),
        migrations.AlterField(
            model_name='qrcodecutomizationtemplates',
            name='qr_code_logo_image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]