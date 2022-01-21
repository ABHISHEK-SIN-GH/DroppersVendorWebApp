# Generated by Django 4.0 on 2021-12-17 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_product_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(default='', max_length=100)),
                ('Product_SellingPrice', models.CharField(default='0', max_length=100)),
                ('Product_Quantity', models.CharField(default='1', max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.product')),
            ],
        ),
    ]
