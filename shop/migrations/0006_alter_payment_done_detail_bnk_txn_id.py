# Generated by Django 3.2.6 on 2022-02-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20220221_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_done_detail',
            name='bnk_txn_id',
            field=models.IntegerField(),
        ),
    ]
