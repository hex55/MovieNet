# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20161019_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date_of_death',
            field=models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True),
        ),
    ]