# Generated by Django 2.1.5 on 2021-08-06 19:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField()),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='BaggedMunros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Bagged Munros',
            },
        ),
        migrations.CreateModel(
            name='Hiker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bagged', models.CharField(blank=True, default='', max_length=300)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Hikers',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=2048)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Munro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField()),
                ('difficulty', models.IntegerField(default=0)),
                ('elevation', models.IntegerField(default=0)),
                ('coordinates', models.CharField(default='', max_length=128)),
                ('duration', models.CharField(default='', max_length=2048)),
                ('length', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=2048)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('mapslink', models.CharField(default='', max_length=2048)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Area')),
            ],
            options={
                'verbose_name_plural': 'Munros',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='report_images')),
                ('report_text', models.CharField(max_length=3000)),
                ('difficulty', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('munro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Munro')),
            ],
            options={
                'verbose_name_plural': 'Reports',
            },
        ),
        migrations.CreateModel(
            name='UserLikeArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_liked', models.BooleanField(default=False)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rango.Area')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserLikeMunro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_liked', models.BooleanField(default=False)),
                ('munro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rango.Munro')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='munro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rango.Munro'),
        ),
        migrations.AddField(
            model_name='hiker',
            name='munro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rango.Munro'),
        ),
        migrations.AddField(
            model_name='hiker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='baggedmunros',
            name='hiker_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rango.Hiker'),
        ),
        migrations.AddField(
            model_name='baggedmunros',
            name='munro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rango.Munro'),
        ),
    ]
