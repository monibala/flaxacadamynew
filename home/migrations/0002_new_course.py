# Generated by Django 4.0.4 on 2022-08-24 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_price', models.IntegerField()),
                ('c_image', models.ImageField(upload_to='')),
                ('c_name', models.CharField(max_length=100)),
                ('c_description', models.TextField(max_length=500)),
            ],
        ),
    ]
