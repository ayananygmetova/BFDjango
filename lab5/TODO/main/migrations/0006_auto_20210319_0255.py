# Generated by Django 3.1.7 on 2021-03-18 20:55

import auth_.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20210318_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateField(default=datetime.date(2021, 3, 21)),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(auto_created=auth_.models.MainUser, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
