# Generated by Django 4.1 on 2022-09-12 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_rename_image_urls_product_images_urls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='images_urls',
            new_name='image_urls',
        ),
    ]
