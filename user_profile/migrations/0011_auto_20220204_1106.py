# Generated by Django 3.2.7 on 2022-02-04 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_auto_20220131_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='img',
            field=models.ImageField(blank=True, upload_to='image/user_profile/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(blank=True, upload_to='image/user_profile/'),
        ),
    ]