# Generated by Django 2.2.4 on 2020-04-28 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_task_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='users',
            new_name='user',
        ),
    ]