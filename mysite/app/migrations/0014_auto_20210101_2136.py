# Generated by Django 3.1.3 on 2021-01-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210101_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='files',
            name='public',
            field=models.BooleanField(default='False'),
        ),
    ]
