# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-23 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbof', '0006_auto_20160223_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='likes',
            new_name='participantCount',
        ),
        migrations.AddField(
            model_name='message',
            name='hashtag',
            field=models.CharField(max_length=40, null=True),
        ),
    ]