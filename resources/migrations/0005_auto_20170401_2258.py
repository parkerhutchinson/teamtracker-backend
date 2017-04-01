# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 22:58
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_auto_20170331_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resources',
            name='group',
        ),
        migrations.AddField(
            model_name='resources',
            name='file',
            field=models.FileField(default='settings.MEDIA_ROOT/resources/default.jpg', storage=django.core.files.storage.FileSystemStorage(location='/Users/parker/Sites/prplapi/files/'), upload_to='resources/'),
        ),
        migrations.AddField(
            model_name='resources',
            name='resources_group',
            field=models.CharField(blank=True, choices=[('Statement of Work / Legal', [('CAG', 'Consulting Services Agreement'), ('FAG', 'Facility License Agreement'), ('MAG', 'Master Services Agreement'), ('NAG', 'Non-Disclosure Agreement (NDA)'), ('OTH', 'Other')]), ('Project Process', [('KOF', 'Kick Off'), ('DEV', 'Development'), ('LAU', 'Launch'), ('SUP', 'Support'), ('OTH', 'Other')]), ('Sales / Marketing', [('OSH', 'One-Sheets'), ('PDE', 'Pitch / Capabilities Decks'), ('PRO', 'Proposals'), ('OTH', 'Other')]), ('PRPL Brand', [('ASS', 'Assets'), ('SGU', 'Style Guides'), ('TEM', 'Templates'), ('OTH', 'Other')]), ('HR & Paperwork', [('OTH', 'Other')])], max_length=3),
        ),
    ]
