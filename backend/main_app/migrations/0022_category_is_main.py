# Generated by Django 3.1.2 on 2021-01-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_product_img_mini'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Является основной категорией?'),
        ),
    ]
