# Generated by Django 4.1.5 on 2023-05-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0006_alter_campaignadditionaldetails_utm_medium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignadditionaldetails',
            name='utm_medium',
            field=models.CharField(choices=[('QR', 'QR'), ('AQR', 'AQR'), ('RFID', 'RFID'), ('NFC', 'NFC')], max_length=13),
        ),
    ]
