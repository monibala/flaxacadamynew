# Generated by Django 3.2.7 on 2022-01-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
