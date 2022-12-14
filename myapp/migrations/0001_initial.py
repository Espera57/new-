# Generated by Django 4.0.6 on 2022-08-06 17:53

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='USER_FAVORITE_VIDEO%Y', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('release_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('main_actors', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('movie_poster', models.FileField(null=True, upload_to='MOVIE_POSTER')),
                ('movie_trailer_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('profile_image', models.ImageField(null=True, upload_to='photoes')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
