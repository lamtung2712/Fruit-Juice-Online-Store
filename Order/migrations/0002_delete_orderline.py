# Generated by Django 4.2.3 on 2023-09-09 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderLine',
        ),
    ]
