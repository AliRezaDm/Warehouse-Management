# Generated by Django 5.0.3 on 2024-04-13 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variant',
            options={'verbose_name': 'محصول با ویژگی', 'verbose_name_plural': ' محصولات با ویژگی'},
        ),
    ]