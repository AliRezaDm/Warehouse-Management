# Generated by Django 5.0.3 on 2024-05-11 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0031_alter_cart_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 11, 5, 14, 45, 226379, tzinfo=datetime.timezone.utc)),
        ),
    ]