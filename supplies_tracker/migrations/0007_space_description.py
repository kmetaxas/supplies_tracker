# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-30 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies_tracker', '0006_auto_20171230_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='description',
            field=models.TextField(null=True),
        ),
    ]