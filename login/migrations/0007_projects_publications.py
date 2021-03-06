# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 21:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0006_teachings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=500)),
                ('Sponser', models.CharField(default='', max_length=300)),
                ('start_year', models.CharField(default='', max_length=200)),
                ('end_year', models.CharField(default='', max_length=200)),
                ('Role', models.CharField(default='', max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default='', max_length=300)),
                ('Title', models.CharField(default='', max_length=300)),
                ('Description', models.CharField(default='', max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
