# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-22 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='jawaban',
            field=models.TextField(default='', max_length=550),
        ),
    ]
