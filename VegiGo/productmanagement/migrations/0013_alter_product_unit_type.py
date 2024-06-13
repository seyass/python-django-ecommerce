# Generated by Django 5.0.3 on 2024-04-30 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0012_alter_product_unit_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_type',
            field=models.CharField(choices=[('l', 'L'), ('g', 'G'), ('kg', 'Kg')], default='kg', max_length=10),
        ),
    ]
