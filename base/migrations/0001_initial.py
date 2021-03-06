# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 03:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_address', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('tx_id', models.AutoField(primary_key=True, serialize=False)),
                ('tx_hash', models.CharField(max_length=300)),
                ('tx_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('deposit_amount', models.DecimalField(decimal_places=18, max_digits=100)),
                ('withdrawal_amount', models.DecimalField(decimal_places=18, max_digits=100)),
                ('withdrawal_address', models.CharField(max_length=300)),
                ('account_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Account')),
            ],
        ),
    ]
