# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 20:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0024_auto_20161204_2222'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
    ]