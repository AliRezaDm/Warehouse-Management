# Generated by Django 5.0.3 on 2024-05-12 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0033_alter_cart_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 12, 17, 9, 29, 819923, tzinfo=datetime.timezone.utc)),
        ),
    ]
