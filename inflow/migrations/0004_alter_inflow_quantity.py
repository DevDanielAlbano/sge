# Generated by Django 5.1.6 on 2025-02-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflow', '0003_alter_inflow_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inflow',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
