# Generated by Django 5.0.6 on 2024-10-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisanApp', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
