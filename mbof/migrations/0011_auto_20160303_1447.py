# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbof', '0010_auto_20160303_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.CharField(max_length=80),
        ),
    ]
