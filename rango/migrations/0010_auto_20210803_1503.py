# Generated by Django 2.1.5 on 2021-08-03 14:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_report_report_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='difficulty',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
