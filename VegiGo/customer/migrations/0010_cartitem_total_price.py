# Generated by Django 5.0.3 on 2024-04-07 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_useraddress_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
