# Generated by Django 5.0.3 on 2024-05-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0026_cart_select_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
