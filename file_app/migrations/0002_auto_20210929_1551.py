# Generated by Django 3.2.7 on 2021-09-29 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='file',
            name='timestamp',
        ),
    ]
