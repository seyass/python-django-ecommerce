# Generated by Django 5.0.3 on 2024-05-14 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0026_alter_product_unit_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='special_discount',
            field=models.DecimalField(decimal_places=2, default=models.DecimalField(decimal_places=2, max_digits=10), max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_type',
            field=models.CharField(choices=[('kg', 'Kg'), ('l', 'L'), ('g', 'G')], default='kg', max_length=10),
        ),
    ]
