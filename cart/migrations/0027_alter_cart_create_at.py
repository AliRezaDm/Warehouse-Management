# Generated by Django 5.0.3 on 2024-05-05 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0026_alter_cart_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 16, 37, 59, 449174, tzinfo=datetime.timezone.utc)),
        ),
    ]
