# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-08 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('object', models.CharField(max_length=200)),
                ('predicate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(-1, 'No'), (0, 'Unsure'), (1, 'Yes')], default=0)),
            ],
        ),
    ]