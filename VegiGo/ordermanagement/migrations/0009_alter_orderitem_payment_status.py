# Generated by Django 5.0.3 on 2024-05-01 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanagement', '0008_orderitem_image_alter_orderitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='payment_status',
            field=models.CharField(choices=[('completed', 'Completed'), ('pending', 'Pending'), ('failed', 'Failed')], default='pending', max_length=20),
        ),
    ]
