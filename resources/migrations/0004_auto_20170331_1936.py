# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20170331_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='filename',
            field=models.CharField(max_length=1024),
        ),
    ]
