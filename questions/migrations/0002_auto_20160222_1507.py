# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='q_img'),
        ),
    ]
