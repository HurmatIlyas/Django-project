# Generated by Django 4.1 on 2022-09-13 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_remove_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='availability',
        ),
    ]