# Generated by Django 5.0.3 on 2024-04-26 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_alter_cart_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 10, 54, 46, 659862, tzinfo=datetime.timezone.utc)),
        ),
    ]