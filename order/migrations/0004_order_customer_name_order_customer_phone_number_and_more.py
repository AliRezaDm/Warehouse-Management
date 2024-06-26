# Generated by Django 5.0.3 on 2024-04-23 09:18

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_create_at'),
        ('product', '0003_rename_count_variant_inventory_variant_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم مشتری'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_phone_number',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='شماره مشتری'),
        ),
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='پرداخت انجام شد؟'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.PositiveIntegerField(default=1, verbose_name='قیمت محصول'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 23, 9, 18, 37, 45486, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_supply', to='product.variant', verbose_name='نام محصول'),
        ),
    ]
