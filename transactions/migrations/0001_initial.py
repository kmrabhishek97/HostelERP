# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-22 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import transactions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0013_auto_20171014_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_Details',
            fields=[
                ('transaction_id', models.CharField(default=transactions.models.increment_transaction_id, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('transaction_date', models.DateTimeField(auto_now=True)),
                ('payment_mode', models.CharField(editable=False, max_length=20)),
                ('fees_paid', models.FloatField(max_length=7)),
                ('fine_paid', models.FloatField(max_length=7)),
                ('remaining_fees', models.FloatField(max_length=7)),
                ('remaining_fine', models.FloatField(max_length=7)),
                ('remaining_total', models.FloatField(max_length=7)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Studentinfo')),
            ],
        ),
    ]
