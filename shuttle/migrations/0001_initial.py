# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('query_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'nodes')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raw_data', models.TextField()),
                ('destination', models.ForeignKey(related_name='destination', to='shuttle.Node')),
                ('start', models.ForeignKey(related_name='start', to='shuttle.Node')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
                ('route', models.ForeignKey(related_name='time', to='shuttle.Route')),
            ],
        ),
    ]
