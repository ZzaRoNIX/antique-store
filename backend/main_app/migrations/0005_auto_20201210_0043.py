# Generated by Django 3.1.2 on 2020-12-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201210_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(blank=True, verbose_name='Цена по скидке'),
        ),
    ]
