# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-14 09:18
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('supplies_tracker', '0021_auto_20180113_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='whatever'),
        ),
        migrations.AlterField(
            model_name='space',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='whatever'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='whatever'),
        ),
    ]
