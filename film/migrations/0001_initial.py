# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=500)),
                ('gatunek', models.CharField(max_length=250)),
                ('rok', models.CharField(max_length=4)),
                ('nota', models.CharField(max_length=4)),
                ('gdzie', models.CharField(max_length=100)),
            ],
        ),
    ]
