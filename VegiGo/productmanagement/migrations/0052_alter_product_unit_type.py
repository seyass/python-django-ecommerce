# Generated by Django 5.0.3 on 2024-05-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0051_alter_product_unit_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_type',
            field=models.CharField(choices=[('kg', 'Kg'), ('l', 'L'), ('g', 'G')], default='kg', max_length=10),
        ),
    ]
