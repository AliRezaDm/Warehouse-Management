# Generated by Django 5.0.3 on 2024-04-23 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_customer_name_order_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 23, 20, 5, 29, 472920, tzinfo=datetime.timezone.utc)),
        ),
    ]