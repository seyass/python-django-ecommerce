# Generated by Django 5.0.3 on 2024-05-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanagement', '0047_alter_orderitem_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.AlterField(
            model_name='order',
            name='address_info',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='payment_status',
            field=models.CharField(choices=[('failed', 'Failed'), ('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.JSONField(),
        ),
    ]
