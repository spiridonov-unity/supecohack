# Generated by Django 4.0.4 on 2022-04-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='data',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]