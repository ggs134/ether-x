# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20160219_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='ethaccount',
            name='account_password',
            field=models.CharField(default=b'password123456789', max_length=300),
        ),
        migrations.AddField(
            model_name='ethaccount',
            name='balance',
            field=models.DecimalField(decimal_places=18, default=0, max_digits=100),
        ),
    ]
