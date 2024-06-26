# Generated by Django 4.1.5 on 2023-03-26 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.SmallAutoField(db_column='activity_id', primary_key=True, serialize=False)),
                ('activity_type', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('market_name', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('market_iso_code', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=500)),
                ('product_description', models.CharField(max_length=400)),
                ('evrythng_tag_1', models.CharField(max_length=200)),
                ('evrythng_tag_2', models.CharField(blank=True, max_length=200, null=True)),
                ('evrythng_tag_3', models.CharField(blank=True, max_length=200, null=True)),
                ('evrythng_tag_4', models.CharField(blank=True, max_length=200, null=True)),
                ('code_placement', models.CharField(choices=[('FOP', 'Front of pack'), ('BOP', 'Back of pack'), ('SOP', 'Side of pack'), ('Lid', 'Lid'), ('Sticker', 'Sticker'), ('BackingCard', 'BackingCard'), ('Insert', 'Insert'), ('OuterFOP', 'Outer front of pack'), ('OuterBOP', 'Outer Back of Pack'), ('InsidePack', 'InsidePack'), ('POS', 'Point of Sale'), ('PrintAd', 'PrintAd')], max_length=100)),
                ('requested_by', models.CharField(max_length=200)),
                ('requested_date', models.DateField(auto_now_add=True)),
                ('budget_holder', models.EmailField(max_length=254)),
                ('gs1_link', models.URLField(blank=True, null=True)),
                ('utm_campaign', models.CharField(max_length=200)),
                ('utm_content', models.CharField(max_length=200)),
                ('brand', models.ForeignKey(db_column='brand_code', on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
            ],
            options={
                'unique_together': {('product_name', 'brand')},
            },
        ),
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_unit_sales', models.PositiveBigIntegerField(blank=True, null=True)),
                ('estimated_unit_sales', models.PositiveBigIntegerField(blank=True, null=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('market', models.ForeignKey(db_column='market_name', on_delete=django.db.models.deletion.CASCADE, to='products.market')),
                ('product', models.ForeignKey(db_column='product_name', on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'sales data',
                'verbose_name_plural': 'sales data',
            },
        ),
        migrations.CreateModel(
            name='ProductMarketDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redirect_url', models.URLField()),
                ('launch_volume', models.BigIntegerField()),
                ('launch_date', models.DateField()),
                ('utm_tagged_link', models.URLField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.activity')),
                ('market', models.ForeignKey(db_column='market_name', on_delete=django.db.models.deletion.CASCADE, to='products.market')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'product market detail',
                'verbose_name_plural': 'product market details',
                'unique_together': {('product', 'market')},
            },
        ),
    ]
