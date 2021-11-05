# Generated by Django 3.2.6 on 2021-10-21 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tunes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubePlaythrough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Title of video playthrough.')),
                ('youtube_playthrough_url', models.URLField(verbose_name='Youtube Embeded URL for Playthrough')),
                ('date_recorded', models.DateField(verbose_name='Date Recorded')),
                ('tune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tunes.tune', verbose_name='Tune that is being played')),
            ],
        ),
    ]