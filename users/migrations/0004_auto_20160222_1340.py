# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 13:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160222_1335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participant',
            options={'ordering': ('-level', 'points')},
        ),
        migrations.RemoveField(
            model_name='participant',
            name='created',
        ),
    ]
