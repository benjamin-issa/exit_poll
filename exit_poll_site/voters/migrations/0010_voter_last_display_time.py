# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0009_auto_20161003_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='last_display_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last time of display'),
        ),
    ]
