# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-18 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='balance',
            field=models.FloatField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
