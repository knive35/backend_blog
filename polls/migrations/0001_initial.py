# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('categories', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
