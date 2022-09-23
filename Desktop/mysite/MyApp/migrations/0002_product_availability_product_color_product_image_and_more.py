# Generated by Django 4.1 on 2022-09-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='care',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_urls',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='retailer_sku',
            field=models.CharField(max_length=1000),
        ),
    ]
