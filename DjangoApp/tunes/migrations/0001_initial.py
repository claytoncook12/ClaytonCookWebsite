# Generated by Django 3.2.6 on 2021-10-20 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ABCTune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BPM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bpm', models.CharField(default='1/4=120', max_length=50, unique=True, verbose_name='Beats Per Minute')),
            ],
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_type_char', models.CharField(max_length=15, unique=True, verbose_name='Key')),
            ],
        ),
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_type_char', models.CharField(default='4/4', max_length=15, unique=True, verbose_name='Meter')),
            ],
        ),
        migrations.CreateModel(
            name='TuneType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tune_type_char', models.CharField(max_length=50, unique=True, verbose_name='Tune Type')),
            ],
        ),
        migrations.CreateModel(
            name='UnitNoteLength',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_note_length', models.CharField(default='1/4', max_length=50, unique=True, verbose_name='Unit Note Length')),
            ],
        ),
        migrations.CreateModel(
            name='Tune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Tune Name')),
                ('parts', models.IntegerField(default=2, verbose_name='Number of Parts')),
                ('tune_info', models.CharField(blank=True, max_length=300, null=True, verbose_name='Information about the tune')),
                ('composer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tunes.composer', verbose_name='Composer')),
                ('tune_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tunes.tunetype', verbose_name='Tune Type')),
            ],
        ),
        migrations.CreateModel(
            name='ABCTunePiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_order', models.IntegerField(default=1, verbose_name='Part Number')),
                ('part_title', models.CharField(blank=True, default='Part #', max_length=30, null=True, verbose_name='Title of Part')),
                ('default', models.BooleanField(default=True, verbose_name='Default Part?')),
                ('abc_piece', models.TextField(verbose_name='ABC text for part of Tune')),
                ('abc_tune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tunes.abctune', verbose_name='ABC Tune')),
            ],
            options={
                'ordering': ['part_order'],
            },
        ),
        migrations.AddField(
            model_name='abctune',
            name='bpm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tunes.bpm', verbose_name='Beats Per Minute'),
        ),
        migrations.AddField(
            model_name='abctune',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tunes.key', verbose_name='Key of Tune'),
        ),
        migrations.AddField(
            model_name='abctune',
            name='meter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tunes.meter', verbose_name='Meter'),
        ),
        migrations.AddField(
            model_name='abctune',
            name='tune',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tunes.tune', verbose_name='Tune'),
        ),
        migrations.AddField(
            model_name='abctune',
            name='unit_note_length',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tunes.unitnotelength', verbose_name='Unit Note Length'),
        ),
    ]