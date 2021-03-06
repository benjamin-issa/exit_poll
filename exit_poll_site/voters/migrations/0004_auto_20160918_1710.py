# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0003_auto_20160918_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='user_marking_invalid',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='call_one_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time of first call'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='call_one_user',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='call_three_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time of third call'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='call_three_user',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='call_two_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time of second call'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='call_two_user',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='phone_no_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone number one+', to='voters.Phone'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='phone_no_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone number two+', to='voters.Phone'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='respondent_id',
            field=models.CharField(default=None, max_length=15, null=True),
        ),
    ]
