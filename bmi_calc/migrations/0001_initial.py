# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bmi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmi', models.FloatField()),
                ('counter', models.IntegerField(default=1)),
            ],
        ),
    ]
