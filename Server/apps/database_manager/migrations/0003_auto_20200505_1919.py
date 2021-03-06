# Generated by Django 3.0.3 on 2020-05-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_manager', '0002_auto_20200310_2051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laptop_properties',
            options={'verbose_name': 'Laptop Properties', 'verbose_name_plural': 'Laptop Properties'},
        ),
        migrations.AlterModelOptions(
            name='records',
            options={'verbose_name': 'Records', 'verbose_name_plural': 'Records'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Users', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='laptop_properties',
            name='image_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='laptop_properties',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
