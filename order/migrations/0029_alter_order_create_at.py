# Generated by Django 4.2.7 on 2024-05-09 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0028_alter_order_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 9, 17, 58, 36, 398385, tzinfo=datetime.timezone.utc)),
        ),
    ]
