# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-17 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_walletpin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletpin',
            name='pin',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
