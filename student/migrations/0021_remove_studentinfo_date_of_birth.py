# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-14 09:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_merge_20171014_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='date_of_birth',
        ),
    ]
