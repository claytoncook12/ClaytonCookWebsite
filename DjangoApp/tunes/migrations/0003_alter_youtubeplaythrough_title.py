# Generated by Django 3.2.6 on 2021-10-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunes', '0002_youtubeplaythrough'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubeplaythrough',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title of video playthrough.'),
        ),
    ]