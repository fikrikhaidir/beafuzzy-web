# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-08 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_data_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='hasil_kalkulasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(default='', max_length=35)),
                ('nim', models.CharField(default='', max_length=10)),
                ('tan', models.FloatField(default=0)),
                ('pot', models.FloatField(default=0)),
                ('pre', models.FloatField(default=0)),
                ('org', models.FloatField(default=0)),
                ('ipk', models.FloatField(default=0)),
                ('rek', models.FloatField(default=0, null=True)),
                ('validasi', models.BooleanField(default=False)),
                ('diterima', models.BooleanField(default=False)),
                ('tidak_diterima', models.BooleanField(default=False)),
                ('akun', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.data_member')),
            ],
        ),
    ]
