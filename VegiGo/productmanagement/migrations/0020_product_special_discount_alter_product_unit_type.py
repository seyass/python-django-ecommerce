# Generated by Django 5.0.3 on 2024-05-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0019_alter_product_unit_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='special_discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_type',
            field=models.CharField(choices=[('l', 'L'), ('kg', 'Kg'), ('g', 'G')], default='kg', max_length=10),
        ),
    ]