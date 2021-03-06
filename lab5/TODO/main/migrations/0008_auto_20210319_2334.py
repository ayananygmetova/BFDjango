# Generated by Django 3.1.7 on 2021-03-19 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210319_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['id', 'name'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['id', 'name'], 'verbose_name': 'Список задач', 'verbose_name_plural': 'Списки задач'},
        ),
        migrations.AlterField(
            model_name='task',
            name='todo',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.todo'),
        ),
    ]
