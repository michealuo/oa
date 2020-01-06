# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-01-04 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='账号')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('email', models.EmailField(default=None, max_length=32, verbose_name='邮箱')),
            ],
        ),
    ]
