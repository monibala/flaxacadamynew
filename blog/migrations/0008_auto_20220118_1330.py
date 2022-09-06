# Generated by Django 3.2.7 on 2022-01-18 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_detail',
            name='element',
            field=models.ManyToManyField(related_name='blog_element', to='blog.blogdetail_element'),
        ),
        migrations.AlterField(
            model_name='blog_detail',
            name='imgs',
            field=models.ManyToManyField(related_name='blog_img', to='blog.blogdetail_img'),
        ),
    ]