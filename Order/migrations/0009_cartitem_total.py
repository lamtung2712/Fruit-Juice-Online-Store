# Generated by Django 4.2.3 on 2023-10-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0008_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
