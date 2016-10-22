# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0011_auto_20161016_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='call_five',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_five_outcome',
            field=models.CharField(blank=True, choices=[('TS', 'Respondent took the Survey'), ('NH', 'Not Home'), ('CB', 'Requested Call Back'), ('LV', 'Left a Voicemail'), ('SD', 'Soft Decline'), ('HD', 'Hard Decline')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_five_phone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone for call four+', to='voters.Phone'),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_five_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time of fourth call'),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_five_user',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_four',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_four_outcome',
            field=models.CharField(blank=True, choices=[('TS', 'Respondent took the Survey'), ('NH', 'Not Home'), ('CB', 'Requested Call Back'), ('LV', 'Left a Voicemail'), ('SD', 'Soft Decline'), ('HD', 'Hard Decline')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_four_phone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone for call four+', to='voters.Phone'),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_four_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time of fourth call'),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_four_user',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_seven',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_seven_outcome',
            field=models.CharField(blank=True, choices=[('TS', 'Respondent took the Survey'), ('NH', 'Not Home'), ('CB', 'Requested Call Back'), ('LV', 'Left a Voicemail'), ('SD', 'Soft Decline'), ('HD', 'Hard Decline')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_seven_phone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone for call four+', to='voters.Phone'),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_seven_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time of fourth call'),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_seven_user',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_six',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_six_outcome',
            field=models.CharField(blank=True, choices=[('TS', 'Respondent took the Survey'), ('NH', 'Not Home'), ('CB', 'Requested Call Back'), ('LV', 'Left a Voicemail'), ('SD', 'Soft Decline'), ('HD', 'Hard Decline')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_six_phone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone for call four+', to='voters.Phone'),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_six_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time of fourth call'),
        ),
        migrations.AddField(
            model_name='voter',
            name='call_six_user',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='supervisor_hold_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='last time of display'),
        ),
    ]