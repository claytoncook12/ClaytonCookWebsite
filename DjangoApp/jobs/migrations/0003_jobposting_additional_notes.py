# Generated by Django 3.2.4 on 2021-12-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_jobposting_job_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='additional_notes',
            field=models.TextField(blank=True, null=True, verbose_name='Additional Notes'),
        ),
    ]