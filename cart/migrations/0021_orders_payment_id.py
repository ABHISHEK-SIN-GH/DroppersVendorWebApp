# Generated by Django 4.0 on 2022-01-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0020_orders_confirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_id',
            field=models.CharField(default='Not_Paid', max_length=100),
        ),
    ]