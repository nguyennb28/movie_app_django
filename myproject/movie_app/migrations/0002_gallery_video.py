# Generated by Django 5.1.4 on 2024-12-19 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='gallery/'),
        ),
    ]
