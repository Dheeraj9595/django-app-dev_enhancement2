# Generated by Django 4.1.5 on 2023-05-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_qr_code_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmarketdetails',
            name='launch_volume',
            field=models.CharField(max_length=12),
        ),
    ]