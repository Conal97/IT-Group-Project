# Generated by Django 2.1.5 on 2021-08-04 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_munro_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='munro',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]