# Generated by Django 4.1.3 on 2022-11-01 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_task_edit_at_alter_task_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 13, 27, 3, 486471)),
        ),
    ]
