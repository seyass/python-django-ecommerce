# Generated by Django 5.0.3 on 2024-05-09 02:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_rename_whishlist_wishlist_and_more'),
        ('vgadmin', '0004_rename_discount_coupon_discount_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vgadmin.branches'),
        ),
    ]