# Generated by Django 5.0.3 on 2024-05-16 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0037_alter_order_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 16, 16, 9, 32, 138049, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(blank=True, default='مشتری گذری', max_length=255, null=True, verbose_name='اسم مشتری'),
        ),
    ]
