# Generated by Django 3.1.3 on 2021-01-02 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210101_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
