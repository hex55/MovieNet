# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_auto_20161029_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='people', to='movies.Country', verbose_name='represented country'),
        ),
        migrations.AlterField(
            model_name='person',
            name='production_role',
            field=models.ManyToManyField(blank=True, related_name='people', to='movies.ProductionRole', verbose_name='role in movie production'),
        ),
    ]