# Generated by Django 5.0.3 on 2024-04-23 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 23, 8, 36, 45, 821437, tzinfo=datetime.timezone.utc)),
        ),
    ]