# Generated by Django 3.2.3 on 2023-12-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_rename_menus_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='type',
            field=models.CharField(choices=[(1, 'Starter'), (2, 'Main'), (3, 'Dessert')], max_length=4),
        ),
    ]
