# Generated by Django 5.0.3 on 2024-05-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0024_cartitem_max_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]