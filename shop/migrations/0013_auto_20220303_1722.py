# Generated by Django 3.2.6 on 2022-03-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20220303_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses_purchase_order',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='course_pyment_id'),
        ),
        migrations.AlterField(
            model_name='products_purchase_order',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='product_pyment_id'),
        ),
        migrations.AlterField(
            model_name='update_order',
            name='crs_orders',
            field=models.ManyToManyField(to='shop.courses_purchase_order', verbose_name='course_order'),
        ),
        migrations.AlterField(
            model_name='update_order',
            name='prod_orders',
            field=models.ManyToManyField(to='shop.products_purchase_order', verbose_name='product_order'),
        ),
        migrations.AlterField(
            model_name='update_order',
            name='updt_id',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True, verbose_name='updt_pyment_id'),
        ),
    ]
