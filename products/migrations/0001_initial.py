# Generated by Django 5.1.6 on 2025-02-15 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0002_alter_brand_options'),
        ('categories', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('serie_number', models.CharField(blank=True, max_length=200, null=True)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='brands.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='categories.category')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
