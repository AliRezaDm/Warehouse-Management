# Generated by Django 5.0.3 on 2024-04-26 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_order_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 10, 54, 46, 661830, tzinfo=datetime.timezone.utc)),
        ),
    ]
