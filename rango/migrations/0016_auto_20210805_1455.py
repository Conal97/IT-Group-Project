# Generated by Django 2.1.5 on 2021-08-05 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0015_auto_20210805_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baggedmunros',
            name='user',
        ),
        migrations.AddField(
            model_name='baggedmunros',
            name='on',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rango.Hiker'),
        ),
    ]
