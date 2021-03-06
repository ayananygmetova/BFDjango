# Generated by Django 3.1.7 on 2021-03-19 20:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210319_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateField(default=datetime.date(2021, 3, 22)),
        ),
        migrations.AlterField(
            model_name='task',
            name='todo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.todo'),
        ),
    ]
