# Generated by Django 4.2.3 on 2023-08-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='', max_length=100),
        ),
    ]
