# Generated by Django 3.2.4 on 2021-12-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='job_short_description',
            field=models.CharField(default='Needed', max_length=50, verbose_name='Job Short Description'),
            preserve_default=False,
        ),
    ]