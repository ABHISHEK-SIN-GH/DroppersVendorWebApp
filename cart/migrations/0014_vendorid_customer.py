# Generated by Django 4.0 on 2021-12-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_vendorid'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorid',
            name='Customer',
            field=models.CharField(default='', max_length=50),
        ),
    ]
