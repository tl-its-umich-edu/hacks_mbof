# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mbof', '0009_auto_20160303_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mbof.Role'),
        ),
    ]