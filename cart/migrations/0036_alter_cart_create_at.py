# Generated by Django 5.0.3 on 2024-05-14 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0035_alter_cart_create_at_alter_cartitem_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 19, 46, 33, 885788, tzinfo=datetime.timezone.utc)),
        ),
    ]
