# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20161021_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]