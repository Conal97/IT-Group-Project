# Generated by Django 2.1.5 on 2021-08-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='area',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='munro',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='munro',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]