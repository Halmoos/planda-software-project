# Generated by Django 2.2.5 on 2019-11-15 11:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0005_auto_20191112_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='users_list',
            field=models.ManyToManyField(related_name='users_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
