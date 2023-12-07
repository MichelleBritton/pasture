# Generated by Django 3.2.3 on 2023-12-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_booking_no_of_guests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(1, 'Starter'), (2, 'Main'), (3, 'Dessert')], default='Please select a type', max_length=4)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
