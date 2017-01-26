# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160220_1214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participant',
            options={'ordering': ('-level', 'points', 'created')},
        ),
        migrations.AddField(
            model_name='participant',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
    ]
