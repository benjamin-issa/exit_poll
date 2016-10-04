# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0008_auto_20161001_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='call_one_phone',
        ),
        migrations.AddField(
            model_name='voter',
            name='call_one_phone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone for call one+', to='voters.Phone'),
        ),
        migrations.RemoveField(
            model_name='voter',
            name='call_three_phone',
        ),
        migrations.AddField(
            model_name='voter',
            name='call_three_phone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone for call three+', to='voters.Phone'),
        ),
        migrations.RemoveField(
            model_name='voter',
            name='call_two_phone',
        ),
        migrations.AddField(
            model_name='voter',
            name='call_two_phone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone for call two+', to='voters.Phone'),
        ),
    ]
