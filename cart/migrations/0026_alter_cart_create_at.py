# Generated by Django 5.0.3 on 2024-05-04 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0025_alter_cart_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 4, 15, 14, 40, 718923, tzinfo=datetime.timezone.utc)),
        ),
    ]
