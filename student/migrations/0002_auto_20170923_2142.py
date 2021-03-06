# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-23 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='refundable_security',
            field=models.FloatField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='running_dues',
            field=models.FloatField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='running_fine',
            field=models.FloatField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='total_dues',
            field=models.FloatField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
