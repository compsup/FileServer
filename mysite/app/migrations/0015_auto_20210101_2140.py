# Generated by Django 3.1.3 on 2021-01-02 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210101_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='file',
        ),
        migrations.RemoveField(
            model_name='files',
            name='public',
        ),
    ]