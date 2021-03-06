# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='gatunek',
            field=models.CharField(choices=[('Akcja', 'Akcja'), ('Dramat', 'Dramat'), ('Horror', 'Horror'), ('Komedia', 'Komedia'), ('Sci-fi', 'Sci-fi'), ('Thriller', 'Thriller'), ('Western', 'Western'), ('Wojenny', 'Wojenny')], max_length=10),
        ),
        migrations.AlterField(
            model_name='film',
            name='gdzie',
            field=models.CharField(choices=[('Dysk', 'Dysk'), ('Netflix', 'Netflix')], max_length=8),
        ),
        migrations.AlterField(
            model_name='film',
            name='nota',
            field=models.FloatField(blank=True, default=7.0, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='rok',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
