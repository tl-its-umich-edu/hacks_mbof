# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-03 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbof', '0010_auto_20160303_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='loginName',
            field=models.CharField(max_length=80, primary_key=True, serialize=False),
        ),
    ]
