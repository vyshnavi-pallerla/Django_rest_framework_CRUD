# Generated by Django 5.0.2 on 2024-04-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybasket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]