# Generated by Django 5.0.3 on 2024-05-14 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_supply_size_alter_supply_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variant_size', to='product.size', verbose_name='سایز محصول'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variant_type', to='product.type', verbose_name='نوع محصول'),
        ),
    ]