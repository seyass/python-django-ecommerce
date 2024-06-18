# Generated by Django 5.0.3 on 2024-06-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanagement', '0052_alter_order_coupon_amount_alter_order_coupon_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='payment_status',
            field=models.CharField(choices=[('completed', 'Completed'), ('failed', 'Failed'), ('pending', 'Pending')], default='pending', max_length=20),
        ),
    ]
