# Generated by Django 2.1.5 on 2021-08-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20210806_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='difficulty',
            field=models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=1),
        ),
    ]
