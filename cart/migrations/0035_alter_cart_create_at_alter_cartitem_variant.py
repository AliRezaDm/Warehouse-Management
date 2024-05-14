# Generated by Django 5.0.3 on 2024-05-14 06:44

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0034_alter_cart_create_at'),
        ('product', '0013_alter_variant_size_alter_variant_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 6, 44, 25, 973985, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_supply', to='product.variant', unique=True, verbose_name='نام محصول'),
        ),
    ]
