# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0006_auto_20160918_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='phone_no_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone number three+', to='voters.Phone'),
        ),
        migrations.AddField(
            model_name='voter',
            name='spanish_speaking',
            field=models.BooleanField(default=False),
        ),
    ]
