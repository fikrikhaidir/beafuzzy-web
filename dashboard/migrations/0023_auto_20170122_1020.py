# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-22 03:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_auto_20170122_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesan_admin',
            name='penerima',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
