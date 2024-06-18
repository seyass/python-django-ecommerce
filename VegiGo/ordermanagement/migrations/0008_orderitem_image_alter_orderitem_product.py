# Generated by Django 5.0.3 on 2024-04-30 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanagement', '0007_orderitem_user_cancel_alter_orderitem_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='order_items'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.CharField(max_length=100),
        ),
    ]
