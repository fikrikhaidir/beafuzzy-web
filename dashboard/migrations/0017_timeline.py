# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-21 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20170120_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul1', models.CharField(default='', max_length=120)),
                ('judul2', models.CharField(default='', max_length=120)),
                ('judul3', models.CharField(default='', max_length=120)),
                ('judul4', models.CharField(default='', max_length=120)),
                ('judul5', models.CharField(default='', max_length=120)),
                ('judul6', models.CharField(default='', max_length=120)),
                ('content1', models.TextField(max_length=320)),
                ('content2', models.TextField(max_length=120)),
                ('content3', models.TextField(max_length=120)),
                ('content4', models.TextField(max_length=120)),
                ('content5', models.TextField(max_length=120)),
                ('content6', models.TextField(max_length=120)),
            ],
        ),
    ]
