# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-20 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20170117_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_admin',
            name='avatar',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/avatar,', verbose_name='avatar'),
        ),
        migrations.AddField(
            model_name='data_member',
            name='avatar',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/avatar,', verbose_name='avatar'),
        ),
    ]
