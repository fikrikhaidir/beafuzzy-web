# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-08 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_hasil_kalkulasi_validasi'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_member',
            name='valid',
            field=models.BooleanField(default=False),
        ),
    ]
