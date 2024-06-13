# Generated by Django 5.0.3 on 2024-05-14 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_remove_cart_location'),
        ('vgadmin', '0004_rename_discount_coupon_discount_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vgadmin.branches'),
        ),
    ]
