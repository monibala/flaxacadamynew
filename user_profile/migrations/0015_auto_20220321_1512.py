# Generated by Django 3.2.6 on 2022-03-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0014_chats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='msgby',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='chats',
            name='msgto',
            field=models.CharField(max_length=200),
        ),
    ]
