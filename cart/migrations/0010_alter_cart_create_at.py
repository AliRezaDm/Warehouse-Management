# Generated by Django 5.0.3 on 2024-04-24 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_alter_cart_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 24, 7, 17, 23, 919433, tzinfo=datetime.timezone.utc)),
        ),
    ]