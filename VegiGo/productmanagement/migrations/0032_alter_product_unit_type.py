# Generated by Django 5.0.3 on 2024-05-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0031_alter_product_unit_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_type',
            field=models.CharField(choices=[('l', 'L'), ('kg', 'Kg'), ('g', 'G')], default='kg', max_length=10),
        ),
    ]
