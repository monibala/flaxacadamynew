# Generated by Django 3.2.6 on 2022-03-12 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0013_auto_20220304_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('msgby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msgby', to=settings.AUTH_USER_MODEL)),
                ('msgto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msgto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]