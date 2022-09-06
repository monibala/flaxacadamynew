# Generated by Django 3.2.6 on 2022-03-10 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0013_auto_20220304_1953'),
        ('blog', '0011_auto_20220204_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog_detail',
            name='blog_instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_instructor_detail', to='user_profile.instructor'),
        ),
        migrations.AlterField(
            model_name='blog_detail',
            name='element',
            field=models.ManyToManyField(to='blog.blogdetail_element'),
        ),
        migrations.AlterField(
            model_name='blog_detail',
            name='imgs',
            field=models.ManyToManyField(to='blog.blogdetail_img'),
        ),
        migrations.AlterField(
            model_name='review',
            name='blog_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_review', to='blog.blog_detail'),
        ),
    ]
