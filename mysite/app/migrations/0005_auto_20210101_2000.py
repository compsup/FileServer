# Generated by Django 3.1.3 on 2021-01-02 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='File',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
