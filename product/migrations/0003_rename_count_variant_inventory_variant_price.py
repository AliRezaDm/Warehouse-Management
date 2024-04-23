# Generated by Django 5.0.3 on 2024-04-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_variant_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variant',
            old_name='count',
            new_name='inventory',
        ),
        migrations.AddField(
            model_name='variant',
            name='price',
            field=models.PositiveIntegerField(default=1, verbose_name='قیمت محصول'),
            preserve_default=False,
        ),
    ]
