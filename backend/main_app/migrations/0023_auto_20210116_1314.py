# Generated by Django 3.1.2 on 2021-01-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_category_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отчество'),
        ),
    ]