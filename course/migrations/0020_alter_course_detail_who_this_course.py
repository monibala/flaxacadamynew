# Generated by Django 3.2.7 on 2022-01-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_alter_course_detail_course_duration_in_weeks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_detail',
            name='who_this_course',
            field=models.ManyToManyField(blank=True, to='course.who_this_crs_for'),
        ),
    ]