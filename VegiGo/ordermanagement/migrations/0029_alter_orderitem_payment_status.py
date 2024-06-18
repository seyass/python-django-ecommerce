# Generated by Django 5.0.3 on 2024-05-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanagement', '0028_alter_orderitem_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('failed', 'Failed'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
    ]
