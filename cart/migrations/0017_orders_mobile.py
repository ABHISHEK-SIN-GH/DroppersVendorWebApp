# Generated by Django 4.0 on 2021-12-26 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='mobile',
            field=models.CharField(default='', max_length=10),
        ),
    ]
