# Generated by Django 3.1.3 on 2021-01-03 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20210101_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='public',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='uploaded_by',
            field=models.CharField(choices=[('admin', 'admin'), ('Greg', 'Greg')], default='None', max_length=50),
        ),
    ]